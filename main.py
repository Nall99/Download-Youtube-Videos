from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download()
  except:
    print("There has been error in downloading your youtube video")
  print("This download has completed!")
link = input("Put your youtube link here: ")
Download(link)