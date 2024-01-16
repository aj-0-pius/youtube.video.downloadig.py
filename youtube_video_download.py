from pytube import YouTube

def seconds_to_minutes(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return minutes, remaining_seconds

def bytes_to_megabytes(bytes_size):
    return bytes_size / (1024 * 1024)

# YouTube video link
link = input("YouTube video Link: ")
yt = YouTube(link)

# Show video details
print("Title: ", yt.title)
print("Number of views: ", yt.views)

# Convert video length to minutes
video_length_minutes, video_length_seconds = seconds_to_minutes(yt.length)
print(f"Length of video: {video_length_minutes} minutes and {video_length_seconds} seconds")

print("----aj_0_pius----")
# Input download path from the user
download_path = '/storage/emulated/0/storag'

# Display available video resolutions
print("\nAvailable video resolutions:")
for i, stream in enumerate(yt.streams.filter(progressive=True).order_by('resolution'), start=1):
    print(f"{i}. Resolution: {stream.resolution}, Size: {bytes_to_megabytes(stream.filesize):.2f} MB")

# Get the desired resolution input from the user
desired_resolution_number = int(input("Enter resolution: "))

# Find desired resolution
ys = list(yt.streams.filter(progressive=True).order_by('resolution'))[desired_resolution_number - 1]

# Starting download
print("Downloading...")
ys.download(download_path)
print("Download completed!! \naj_0_pius")
