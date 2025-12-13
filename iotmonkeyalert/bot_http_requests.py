import os
import sys
from pprint import pprint

import requests
import telepot as tpot
from telepot.loop import MessageLoop

import token_chatid as env

CHAT_ID = f"{env.CHAT_ID}"
TOKEN = f"{env.TOKEN}"

bot = tpot.Bot(f"{TOKEN}")
print("bot.getMe();")
print(bot.getUpdates())
# print("bot.getUpdates(offset=100000001")
# resp = bot.getUpdates(offset=100000001)
# print(resp)

# def get_all_chat_id(n):
#     url = f"https://api.telegram.org/bot{TOKEN}/get"
#     data = {
#         "chat_id": chat_id,
#         "name" : name
#     }
#     post = requests.get(url)


def handle(incoming_message):
    pprint(incoming_message)


def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    r = requests.post(url, data=data)
    print(f"THIS IS SEND MESSAGE JSON:{r.json()}")  # debug response


def send_photo(path, caption=""):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    with open(path, "rb") as img:
        files = {"photo": img}
        data = {"chat_id": CHAT_ID, "caption": caption}
        req = requests.post(url, files=files, data=data)
    print(f"THIS IS PHOTO JSON:{req.content}")


def send_video(path, caption=""):
    url = f"https://api.telegram.org/bot{TOKEN}/sendVideo"
    with open(path, "rb") as vid:
        files = {"video": vid}
        data = {"chat_id": CHAT_ID, "caption": caption}
        req = requests.post(url, files=files, data=data)
    print(f"THIS IS VIDEO JSON:{req.content}")


send_video("C:/Users/HP/Downloads/bobby3.mp4", "jahak ni hehe")
send_message("rilek bang, jangan delete saya ~_~")
send_photo(
    "C:/Users/HP/OneDrive - UNIVERSITY UTARA MALAYSIA/Pictures/Screenshots/Screenshot 2025-12-10 153047.png",
    "hehe",
)

MessageLoop(bot, handle).run_as_thread()
