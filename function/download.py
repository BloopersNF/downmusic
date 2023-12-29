from os import listdir
from pytube import YouTube

def download(link, path):
    try:
        print(f'Starting download for {link}')
        #get the video
        yt = YouTube(link)

        #get the safe title
        safe_title = yt.title.replace('/', '').replace('\\', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')+'.mp3'
        
        #check if the video already exists
        if safe_title in listdir(path):
            print(f'{yt.title} already exists')
            return
        
        #download the video
        yt.streams.filter(only_audio=True).first().download(path, filename=safe_title)
        print(f'Download completed for [{yt.title}]')
        
    except Exception as e:
        print(f'Failed to download {link}: {e}')
pass