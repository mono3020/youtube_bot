import yt_dlp


def get_video_info(url):


    options = {

        "quiet": True,

        "format":
        "best[ext=mp4]/best",

        "nocheckcertificate": True,

        "extractor_args": {

            "youtube": {

                "player_client": [
                    "android"
                ]

            }

        }

    }



    with yt_dlp.YoutubeDL(options) as ydl:


        info = ydl.extract_info(
            url,
            download=False
        )



    size = info.get(
        "filesize"
    )


    if size:

        mb = round(
            size / 1024 / 1024,
            2
        )

    else:

        mb = "不明"



    return {

        "title":
        info.get("title"),


        "download_url":
        info.get("url"),


        "size":
        mb

    }
