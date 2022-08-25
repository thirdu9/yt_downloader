from email.mime import audio
from pytube import YouTube
from pytube import Playlist
import time

#*******Video+Audio Download**************#
def video_download(link):
    yt = YouTube(link)
    print(f'Video Name: {yt.title}')

    videos = yt.streams.all()
    vid = list(enumerate(videos))
    for i in vid:
        print(i)

    strm = int(input('Enter: '))
    print(f'Downloading... {yt.title}')
    videos[strm].download()

    print('Done!')
    time.sleep(3)
    

#**************Audio Download**************#

def audio_download(link):
    yt = YouTube(link)
    audios = yt.streams.filter(only_audio=True)
    print(f'Video Name: {yt.title}')
    aud = list(enumerate(audios))
    for i in aud:
        print(i)
    aud_num = int(input('Enter: '))
    print(f'Downloading: {yt.title}')
    audios[aud_num].download()

    print('Done!')
    time.sleep(3)


#**************Playlist Download**************#

def playlist_download(link):
    py = Playlist(link)

    print(f'Playlist Name: {py.title}')

    for k in py.videos:
        pvideos = k.streams.all()
        pvid = list(enumerate(pvideos))
        for j in pvid:
            print(k.title)
            print(j)
        pchoice = int(input('Enter: '))
        pvideos[pchoice].download()

        print(f'{k} successfully Downloaded!')
        time.sleep(3)
        


while True:
    print("""*****************************

1. Download VIDEO & AUDIO
2. Download  AUDIO only
3. Download complete PLAYLIST

    (press 'Exit' 'to exit)
*****************************""")
    option = int(input('Choose: '))

    if option == 1:
        link = input('Enter url - ')
        video_download(link)
    elif option == 2:
        link = input('Enter url - ')
        audio_download(link)
    elif option ==3:
        link = input('Enter url - ')
        playlist_download(link)
    else: 
        print('Enter valid Option!')
        print('-----------------------------\n')
    time.sleep(3)