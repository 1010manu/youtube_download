from pytube import YouTube
def download(link):
    youtubeObject=YouTube(link)
    youtubeObject=youtubeObject.streams.get_highest_resolution()
##    try:
    youtubeObject.download()
##    except:
##        print('an error')
    print('downloaded')
link=input('enter the url:')
download(link)
