from function.getLink import getLink
from function.download import download

path = 'musics/'
#using pytube to downlod the music of teste.txt file
links = getLink('teste.txt')
def main():
    for link in links:
        download(link, path)
if __name__ == '__main__':
    main()