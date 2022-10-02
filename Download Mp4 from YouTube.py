#pip3 install pytube (before running this code)
from turtle import title
from pytube import YouTube


def get_url():
    url = input("Enter the URL of the Video: ")
    return url

def download_video(url):
    yt = YouTube(url)
    title = yt.title
    print("Downloading..." + title)
    yt.streams.filter(progressive = True, file_extension = 'mp4').order_by('resolution').desc().first().download('C:/Users/Ezmond/Desktop/YouTube Downloads')#your folder location that you wan it to download to
    print("Downloaded !!!" + title)
    return title

download_video(get_url())
#try debug and run it if having issues with