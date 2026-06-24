from flask import Flask, request
import requests
import re

from youtube import get_video_info


app = Flask(__name__)


CHATWORK_TOKEN = "8f2bcd6c8125f5985155de27217b3585"

ROOM_ID = "439704308"


def send_message(text):

    url = f"https://api.chatwork.com/v2/rooms/{ROOM_ID}/messages"

    headers = {
        "X-ChatWorkToken": CHATWORK_TOKEN
    }

    requests.post(
        url,
        headers=headers,
        data={
            "body": text
        }
    )


@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json


    message = data["webhook_event"]["body"]


    urls = re.findall(
        r"https?://[^\s]+",
        message
    )


    for url in urls:

        if "youtube.com" in url or "youtu.be" in url:

            try:

                info = get_video_info(url)


                send_message(
f"""YouTube動画を確認しました！

タイトル:
{info['title']}

リンク:
{info['url']}
"""
                )


            except Exception as e:

                send_message(
                    "動画取得に失敗しました"
                )


    return "ok"



if __name__ == "__main__":
    app.run()
