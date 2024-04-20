$random_number = Get-Random -Minimum 500 -Maximum 20000
$video_length = 60



echo "chiamo il sito e genero un audio"
.\consoleApp\ConsoleApp1.exe
cp .\consoleApp\test.wav .\input\audio.wav


echo "genero un video di $video_length secondi partendo dal secondo $random_number"

ffmpeg -i input\video.mp4 -ss $random_number -t $video_length output\subway_clip.mp4 -y
ffmpeg -i input\audio.wav -t $video_length -acodec pcm_s16le -ac 1 -ar 16000 output\audio.wav -y

ffmpeg -i output\subway_clip.mp4 -i output\audio.wav -c:v copy -map 0:v:0 -map 1:a:0 output\video_finale.mp4 -y

cp .\output\audio.wav .\my-video\temp\audio.wav

cd .\my-video\whisper.cpp

.\main.exe -f ..\temp\audio.wav -oj ..\temp\output.json -m .\ggml-medium.en.bin

cd ..

cp .\temp\audio.wav.json .\public\sample-video.json

cp ..\output\video_finale.mp4 .\public\sample-video.mp4

npm run build

cp .\out\CaptionedVideo.mp4 ..\output\CaptionedVideo.mp4

cd ..

