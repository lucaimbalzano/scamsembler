import {useCallback, useEffect, useState} from 'react';
import {
	AbsoluteFill,
	CalculateMetadataFunction,
	cancelRender,
	continueRender,
	delayRender,
	getStaticFiles,
	OffthreadVideo,
	Sequence,
	useVideoConfig,
	watchStaticFile,
} from 'remotion';
import {z} from 'zod';
import Subtitle from './Subtitle';
import {getVideoMetadata} from '@remotion/media-utils';
import {loadFont} from '../load-font';
import {NoCaptionFile} from './NoCaptionFile';

export type Timestamp = {
    from: string;
    to: string;
}
export type SubtitleProp = {
	timestamps: Timestamp;
	text: string;
};

export const captionedVideoSchema = z.object({
	src: z.string(),
});

export const calculateCaptionedVideoMetadata: CalculateMetadataFunction<
	z.infer<typeof captionedVideoSchema>
> = async ({props}) => {
	const fps = 30;
	const metadata = await getVideoMetadata(props.src);

	return {
		fps,
		durationInFrames: Math.floor(metadata.durationInSeconds * fps),
	};
};

const getFileExists = (file: string) => {
	const files = getStaticFiles();
	const fileExists = files.find((f) => {
		return f.src === file;
	});
	return Boolean(fileExists);
};

export const getSecondsFromTimestamp = (timestamp:string):number => {
    console.log(timestamp);
    const lastIdx = timestamp.lastIndexOf(":");
    const outnum = Number(timestamp.replace(",",".").slice(lastIdx + 1));
    return outnum;
}

export const CaptionedVideo: React.FC<{
	src: string;
}> = ({src}) => {
	const [subtitles, setSubtitles] = useState<SubtitleProp[]>([]);
	const [handle] = useState(() => delayRender());
	const {fps} = useVideoConfig();

	const subtitlesFile = src
		.replace(/.mp4$/, '.json')
		.replace(/.mkv$/, '.json')
		.replace(/.mov$/, '.json')
		.replace(/.webm$/, '.json');

	const fetchSubtitles = useCallback(async () => {
		try {
			await loadFont();
			const res = await fetch(subtitlesFile);
			const data = await res.json();
			setSubtitles(data.transcription);
			continueRender(handle);
		} catch (e) {
			cancelRender(e);
		}
	}, [handle, subtitlesFile]);

	useEffect(() => {
		fetchSubtitles();

		const c = watchStaticFile(subtitlesFile, () => {
			fetchSubtitles();
		});

		return () => {
			c.cancel();
		};
	}, [fetchSubtitles, src, subtitlesFile]);
    console.dir(subtitles);

	return (
		<AbsoluteFill style={{backgroundColor: 'white'}}>
			<AbsoluteFill>
				<OffthreadVideo
					style={{
						objectFit: 'cover',
					}}
					src={src}
				/>
			</AbsoluteFill>
			{subtitles.map((subtitle, index) => { 
				const nextSubtitle = subtitles[index + 1] ?? null;
				const subtitleStartFrame = getSecondsFromTimestamp(subtitle.timestamps.from) * fps;
				const subtitleEndFrame = nextSubtitle ? getSecondsFromTimestamp(nextSubtitle.timestamps.from) * fps : Infinity
				const durationInFrames = subtitleEndFrame - subtitleStartFrame;
				if (durationInFrames <= 0) {
					return null;
				}

				return (
					<Sequence
						from={subtitleStartFrame}
						durationInFrames={durationInFrames}
					>
						<Subtitle key={index} text={subtitle.text} />;
					</Sequence>
				);
			})}
			{getFileExists(subtitlesFile) ? null : <NoCaptionFile />}
		</AbsoluteFill>
	);
};
