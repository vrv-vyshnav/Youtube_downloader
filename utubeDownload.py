"""
requirements:

        pip install pytube

"""
# https://www.youtube.com/watch?v=KWOZHbDdOeo

from typing import List
from pytube import YouTube, Playlist
import os

download_directory = os.path.join(os.getcwd(), "Downloads")
os.makedirs(download_directory, exist_ok=True)


def stream_list(video):
    print(video.title)
    list_of_streams = video.streams
    for stream in video.streams.all():
        print(stream)

    stream_number = int(input("\n Enter the iTAG of the stream you want to download : "))
    return  stream_number
    


def download_with_url():
    try:
        url = input("\n  Enter the url of the video : ")
        try:
            Youtube_video = YouTube(url)
        except:
            print("connection failed")

        stream_tag = stream_list(Youtube_video)
        print("\n \t ", Youtube_video.title, " is Downloading \n")
        stream_number = Youtube_video.streams.get_by_itag('137')
        # resolution = Youtube_video.streams.get_highest_resolution()
        stream_number.download(download_directory)
        print(" ",Youtube_video.title," has downloaded successfully \n ")

    except Exception as e:
        print(e)
        print("\n could not download the video")
        print(" check the url and try again \n")


def download_full_playlist():
    try:
        url = input("\n  Enter the url of the video : ")
        try:
            playlist = Playlist(url)
        except:
            print("connection failed")

        print('Number of videos in playlist: %s' % len(playlist.video_urls))
        for video in playlist:
            print(video)
            Youtube_video = YouTube(video)
            resolution = Youtube_video.streams.get_highest_resolution()
            print("\n \tDownloading \n", Youtube_video.title)
            resolution.download(download_directory)
            print(Youtube_video.title, " downloaded")
        print("Playlist downloaded successfully \n ")
    except:
        print("\n could not download the playlist")
        print(" check the url and try again \n")


def download_audio_only():
    try:
        url = input("\n  Enter the url of the video : ")
        try:
            YouTube_video = YouTube(url)
        except:
            print("connection failed")

        print("\n \t video is Downloading \n")
        video = YouTube_video.streams.filter(only_audio=True).first()
        out_file = video.download(download_directory)
        base = os.path.splitext(out_file)
        print("\n \t converting to audio \n")
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("\n \t downlaod successfully \n")

    except:
        print(" check the url and try again \n")


def download_video_only():
    # try:
    #     url = input("\n  Enter the url of the video : ")
    #     try:
    #         YouTube_video = YouTube(url)
    #     except:
    #         print("connection failed")
    #     stream = YouTube_video.streams.filter(file_extension='mp4')
    #     # for i in stream:
    #     #     print(i)
    #     # print("\n")
    #     stream[0].download()
    # except:
    #     pass
    print("working on it")

# -----------------------------------------------------------------


print(" \n \t  Youtube Downloader \n")
print(" \t-----------------------\n")
print("\n \t 1. Download video \n")
print("\t 2. Download full playlist \n")
print("\t 3. Download audio only \n")
print("\t 4. Download video only \n")

choice = int(input("Enter your choice : "))
if choice == 1:
    download_with_url()
elif choice == 2:
    download_full_playlist()
elif choice == 3:
    download_audio_only()
elif choice == 4:
    download_video_only()
else:
    # print("\n Invalid choice \n")
    test()
