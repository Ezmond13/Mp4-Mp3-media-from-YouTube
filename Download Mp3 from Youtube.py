# pip3 install pytube (first before using this code) 
from pytube import YouTube
import os

def get_url():
    url = input("Enter the URL of the Video for convert into Mp3: ")
    return url

def download_video(url):
    video = YouTube(url)
    print("Title", video.title)
    print("Downloading , will take few second... ...")

    out_path = video.streams.filter(only_audio = True).first().download('C:/Users/Ezmond/Desktop/YouTube Downloads')#the file location that you wanna download into
    new_name = os.path.splitext(out_path)
    os.rename(out_path, new_name[0] + ".mp3")
    print(video.title, "Has already downloaded into the file location")

download_video(get_url())