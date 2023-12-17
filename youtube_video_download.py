from pytube import YouTube

#video link
link = input("YouTube video Link: ")
yt = YouTube(link)
#Shows details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting  highest resolution 
ys = yt.streams.get_highest_resolution()
#Download Path
download_path = '/storage/emulated/0/storag'
#Starting download
print("Downloading...")
ys.download()
print("Download completed!! \naj_0_pius")