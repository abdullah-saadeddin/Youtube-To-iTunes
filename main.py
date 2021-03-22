
from pytube import YouTube
from time import sleep
from shutil import move
from moviepy.video.io.VideoFileClip import VideoFileClip
import sys
import eyed3
from requests import get
import os
import arabic_reshaper
from bidi.algorithm import get_display


def main(ass):
    yt = YouTube(str(ass))
    image = yt.thumbnail_url
    yt = yt.streams.filter(progressive=True, file_extension="mp4")
    fileName = yt.first().default_filename
    reshaped_text = arabic_reshaper.reshape(fileName)    
    bidi_text = get_display(reshaped_text)          
    print("Start Download: " + bidi_text)
    yt.first().download()
    sleep(2)
    print("Finish Download the video")
    video = VideoFileClip(fileName)
    fileNameMp3 = fileName.replace("mp4", "mp3")
    video.audio.write_audiofile(fileNameMp3)
    video.close()
    sleep(2)
    audiofile = eyed3.load(fileNameMp3)

    if (audiofile.tag == None):
        audiofile.initTag()
    response = get(image)
    audiofile.tag.images.set(3, response.content, 'image/jpeg')

    audiofile.tag.save()
    move("./"+fileName, "./mp4s/"+fileName)
    pathToSaveMp3 = "Music/iTunes/iTunes Media/Automatically Add to iTunes/"+fileNameMp3
    move("./"+fileNameMp3, os.path.join(os.path.expanduser("~"), pathToSaveMp3))
    return


if __name__ == "__main__":
    while True:
        i = input("Enter Video Url or E to exit: ")
        if i == 'e' or i == 'E':
            break
        else:
            try:
                main(i)
            except:
                pass
