import youtube_dl


def scrappy(URL):
    url = URL

    print(" [+] Downloading stand by\n")


    ydl = youtube_dl.YoutubeDL({'outtmpl': './%(uploader)s - %(title)s - %(id)s.%(ext)s'}) 

    with ydl:
        result = ydl.extract_info(
            url,
            download = True
        )



#https://www.pornhub.com/view_video.php?viewkey=ph5e80ec51bc6b5



