#!/usr/bin/env python3
###################
# Made By Cam3r0n #
###################
import sys, os, time, requests, random
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

class Discord:
    
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": token,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "*/*"
        }

    def ChangeStatus(self, status, message, emoji_name, emoji_id):
        jsonData = {
            "status": status,
            "custom_status": {
                "text": message,
                "emoji_name": emoji_name,
                "emoji_id": emoji_id
        }}
        r = requests.patch("https://discord.com/api/v8/users/@me/settings", headers=self.headers, json=jsonData)
        return r.status_code

def Run(discord, status, emoji_name, emoji_id):
    discord = discord
    message = random.choice(list(open('messages.txt')))
    message = message.replace('\r', '').replace('\n', '')
    status_code = discord.ChangeStatus(status, message, emoji_name, emoji_id)
    if status_code == 200:
        print("[===================================]")
        print("  Successfully changed your status!")
        print(f"  Status     : {status}")
        print(f"  Message    : {message}")
        print(f"  Emoji Name : {emoji_name}")
        print(f"  Emoji ID   : {emoji_id}")
        print("[===================================]")
    else:
        print("An error has occurred while attempting to change your status!")

def Main():
    TOKEN = os.environ.get("TOKEN")
    discord = Discord(TOKEN)
    while True:
        Run(discord, "STATUS", "EMOJI_NAME", "EMOJI_ID")
        time.sleep(3600)

if __name__ == "__main__":
    Main()
else:
    filename = os.path.basename(sys.argv[0])
    print(f"{filename} is currently being imported into another module!")
