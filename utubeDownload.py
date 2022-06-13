from operator import indexOf
from pytube import YouTube
from pytube import Playlist


def download_with_url():
    try:
        url = input("Enter the url of the video : ")
        Youtube_video = YouTube(url)
        resolution = Youtube_video.streams.get_highest_resolution()
        print("\n \t video is Downloading \n")
        resolution.download()
        print("Your video is downloaded successfully \n ")
    except:
        print("\n could not download the video")
        print(" check the url and try again \n")
        
def download_full_playlist():
    try:
        url = input("Enter the url of the playlist : ")
        playlist = Playlist(url)
        print('Number of videos in playlist: %s' % len(playlist.video_urls))
        print("\n \t video is Downloading \n")
        for video in playlist:
            print(video)
            Youtube_video = YouTube(video)
            resolution = Youtube_video.streams.get_highest_resolution()
            print("\n \tDownloading \n",Youtube_video.title)
            resolution.download()
            print("video downloaded")
        print("Playlist downloaded successfully \n ")
    except:
        print("\n could not download the playlist")
        print(" check the url and try again \n")
        
# -----------------------------------------------------------------

print(" \n \t \t Youtube Downloader \n")
print(" \t\t-----------------------\n")
print("\n \t 1. Download with url \n")
print("\t 2. Download full playlist \n")
choice = int(input("Enter your choice : "))
if choice == 1:
    download_with_url()
else:
    download_full_playlist()