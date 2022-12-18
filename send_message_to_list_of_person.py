from telethon.sync import TelegramClient, events
import os, sys
import csv
import traceback
import time
import random

gr="\033[1;32m"
cy="\033[1;36m"
re="\033[1;31m"

name = 'madhu' 
api_id = 23633077
api_hash = "a5ada07a60d492dd665997f10ed05024" 

client = TelegramClient( name , api_id, api_hash)

async def main():
    input_file = sys.argv[1]
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f,delimiter=",",lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {}
            user['user_id'] = int(row[1])
            user['name'] = row[3]
            print(gr+'Sending  '+user['name']+'.........')
            time.sleep(1)
            message_to_send = 'HI '+ user['name']+'!'
            try:
                await client.send_message(int(user['user_id']),message_to_send)
                print(gr+'Sucessfully send')
            except:
                print(re+'not able to send')
 
with client:
    client.loop.run_until_complete(main())

client.disconnect()