from pytube import YouTube
from function.getLink import getLink
from os import listdir

path = 'Seu\\diretorio\\aqui'
#using pytube to downlod the music of teste.txt file
links = getLink('teste.txt')
def download(link):
    try:
        print(f'Starting download for {link}')
        yt = YouTube(link)
        safe_title = yt.title.replace('/', '').replace('\\', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')+'.mp3'
        if safe_title in listdir(path):
            print(f'{yt.title} already exists')
            return
        yt.streams.filter(only_audio=True).first().download(path, filename=safe_title)
        print(f'Download completed for [{yt.title}]')
    except Exception as e:
        print(f'Failed to download {link}: {e}')
def main():
    for link in links:
        download(link)
if __name__ == '__main__':
    main()