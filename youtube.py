import yt_dlp


def get_video_info(url):

    options = {
        "quiet": True,
        "skip_download": True
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(
            url,
            download=False
        )

    return {
        "title": info.get("title"),
        "url": url
    }
