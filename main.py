import requests

import token_chatid as env

CHAT_ID = f"{env.CHAT_ID}"
TOKEN = f"{env.TOKEN}"


# def get_all_chat_id(n):
#     url = f"https://api.telegram.org/bot{TOKEN}/get"
#     data = {
#         "chat_id": chat_id,
#         "name" : name
#     }
#     post = requests.get(url)


def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    r = requests.post(url, data=data)
    print(r.json())  # debug response


def send_photo(path, caption=""):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    with open(path, "rb") as img:
        files = {"photo": img}
        data = {"chat_id": CHAT_ID, "caption": caption}
        requests.post(url, files=files, data=data)


def send_video(path, caption=""):
    url = f"https://api.telegram.org/bot{TOKEN}/sendVideo"
    with open(path, "rb") as vid:
        files = {"video": vid}
        data = {"chat_id": CHAT_ID, "caption": caption}
        requests.post(url, files=files, data=data)


send_video("C:/Users/HP/Downloads/bobby2.mp4", "jahak ni hehe")
