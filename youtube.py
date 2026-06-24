import yt_dlp


def get_video_info(url):

    options = {

        "quiet": True,

        "format":
        "best[ext=mp4]/best"

    }


    with yt_dlp.YoutubeDL(options) as ydl:

        info = ydl.extract_info(
            url,
            download=False
        )


    return {

        "title":
        info.get("title"),

        "download_url":
        info.get("url")

    }
