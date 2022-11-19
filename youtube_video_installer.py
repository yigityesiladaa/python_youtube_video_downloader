from pytube import YouTube
line = 1
def goto(linenum):
    global line
    line = linenum

    
def switch(resolution,yt):
        if resolution == "1":
            return yt.streams.get_highest_resolution()
        elif resolution == "2":
            return yt.streams.get_lowest_resolution()
        else:
            return "Invalid Input"

def videoDownloader():
    print("Enter the URL of the video you want to download\nType 'exit' to exit")
    link = input("\nLink:  ")
    if link == "exit":
        exit()
    yt = YouTube(link)
    resolution = input("\nSelect Resolution:  \n\n1.High Resolution\n2.Low Resolution\n\nYour Choice:  ")
    video = switch(resolution,yt)
    if video != "Invalid Input":
        print("Downloading...")
        success = video.download()
        if success:
            print("Video Downloaded Successfully\n")
        else:
            print("Video Download Failed")
    else:
        print("Invalid Input, Please Try Again")



while True:
    if line == 1:
        videoDownloader()
    else:
        goto(1)