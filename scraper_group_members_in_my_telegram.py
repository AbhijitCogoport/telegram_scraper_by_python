from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import os, sys
import csv
import time

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

api_id =  23633077
api_hash = "a5ada07a60d492dd665997f10ed05024" 
name = 'madhu' 

client = TelegramClient(name, api_id, api_hash)

client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    client.sign_in(phone, input(gr+'[+] Enter the code: '+re))
 
os.system('clear')
chats = []
last_date = None
chunk_size = 200
groups=[]
 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
 
for chat in chats:
    try:
        if chat.broadcast == True:
            groups.append(chat)
        if chat.gigagroup == True:
            groups.append(chat)
        if chat.megagroup== True:
            groups.append(chat)
        
    except:
        continue
 
print(gr+'[+]  List of groups to scrape members :'+re)
i=0
for g in groups:
    print(gr+'['+cy+str(i)+gr+']'+cy+' - '+ g.title)
    i+=1

it=0
for target_group in groups:
    try:
        all_participants = []
        all_participants = client.get_participants(target_group, aggressive=True)
        print(gr+'[+] Fetching Members...')
        time.sleep(1)
        it+=1

        print(gr+'[+] Saving In file...')
        time.sleep(1)
        with open("group_members/members"+str(it)+".csv","w",encoding='UTF-8') as f:
            writer = csv.writer(f,delimiter=",",lineterminator="\n")
            writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
            for user in all_participants:
                if user.username:
                    username= user.username
                else:
                    username= ""
                if user.first_name:
                    first_name= user.first_name
                else:
                    first_name= ""
                if user.last_name:
                    last_name= user.last_name
                else:
                    last_name= ""
                name= (first_name + ' ' + last_name).strip()
                writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])      
            print(gr+'[+] Members scraped successfully.')

    except:
        print(re+'no permision is grated')
        continue

client.disconnect()