$random_number = Get-Random -Minimum 1 -Maximum 500
$video_length = 60
try {
    $random_number = Get-Random -Minimum 60 -Maximum 3000
    $video_length = 60
    echo "chiamo il sito"
    $posts = Invoke-RestMethod -Uri "http://127.0.0.1:8000/reddit/get-cycle-reddit/10"
    $i = 0

    foreach ($post in $posts){
        $i = $i + 1
        echo "genero l'audio"
        #.\consoleApp\ConsoleApp1.exe $post
        gtts-cli $post --output test.wav
        cp test.wav .\input\audio.wav

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

        cp .\out\CaptionedVideo.mp4 ..\output\videos\CaptionedVideo_$i.mp4

        cd ..
    }
}
catch {
    Write-Host $_.Exception.Message
        exit
}
