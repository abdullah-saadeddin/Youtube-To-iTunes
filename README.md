# Youtube to iTunes

this python code download a video from youtube as mp3 and add it to the iTunes Library.

# Install && Run

```cmd
git clone
cd youtube-to-iTunes
pip install -r requirements.txt
python main.py
```

# How it works

I use the youtubePy Library to get the video from youtube using it URL and download the standard Quality of the video and get the thumbnail, the Library doesn't offer an mp3 file so i use the moviepy Library to convert the video to mp3 file format
download the thumbnail using requests and finally add it to the mp3 file using eyed3 after all that the mp3 file moved to the iTunes music Library folder.
