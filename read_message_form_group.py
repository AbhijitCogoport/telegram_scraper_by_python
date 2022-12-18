from telethon.sync import TelegramClient
import csv

name = 'madhu' 
api_id = 23633077
api_hash = "a5ada07a60d492dd665997f10ed05024" 
chat = 'https://t.me/logistics_truck'

f = open('group_message.csv', 'w')
writer = csv.writer(f)
with TelegramClient(name, api_id, api_hash) as client:
    for message in client.iter_messages(chat):
        writer.writerow([message.sender_id,message.message,message.views, message.id, message.date, message.edit_date])
        print('\n\n\n',message,'\n\n')

f.close()