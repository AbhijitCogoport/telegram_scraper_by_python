from telethon.sync import TelegramClient
import csv

api_id = your_api_id_integer
api_hash = your_hash_token_string
name = your_name_string 
chat = 'https://t.me/logistics_truck'

f = open('group_message.csv', 'w')
writer = csv.writer(f)
with TelegramClient(name, api_id, api_hash) as client:
    for message in client.iter_messages(chat):
        writer.writerow([message.sender_id,message.message,message.views, message.id, message.date, message.edit_date])
        print('\n\n\n',message,'\n\n')

f.close()