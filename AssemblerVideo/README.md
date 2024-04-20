# AssemblerVideo

create i/o folders
```
mkdir input
mkdir output
```

put your base video in with that name
```
./input/video.mp4
$ choco install ffmpeg
```

setup whisper.cpp
```
assure you have node.js v20 or above
cd ./my-video
node sub.mjs
https://github.com/ggerganov/whisper.cpp/releases/tag/v1.5.4
https://github.com/ggerganov/whisper.cpp/releases
https://github.com/ggerganov/whisper.cpp
```

run AssemblerTextContext backend
```
read the other README.nd
$ uvicorn main:app
```

you need to specify the length of your video
```
as admin use the powershell
$ process.ps1 
```
