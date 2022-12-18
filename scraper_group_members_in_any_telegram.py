import configparser
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.sync import TelegramClient
from telethon import functions, types
import time
import csv

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"


api_id = your_api_id_integer
api_hash = your_hash_token_string
name = your_name_string
client = TelegramClient(name, api_id, api_hash)


async def main():
 
    await client.start()
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    search = str(input(gr+'Enter key for scraping: '))
    result = await client(functions.contacts.SearchRequest(q=search,limit=100))

    groups=[]
    for chat in result.chats:
        try:
            if chat.broadcast == True:
                groups.append(chat)
            if chat.gigagroup == True:
                groups.append(chat)
            if chat.megagroup== True:
                groups.append(chat)
        except:
            continue

    print(gr+'[+] List of groups to scrape members :'+re)
    i=0
    for g in groups:
        print(gr+'['+cy+str(i)+gr+']'+cy+' - '+ g.title)
        i+=1

    it=0
    for target_group in groups:
        try:
            all_participants = []
            all_participants = await client.get_participants(target_group, aggressive=True)
            print(gr+'[+] Fetching Members...')
            time.sleep(1)
            it+=1

            print(gr+'[+] Saving In file...')
            time.sleep(1)
            no=0
            with open("any_group_members/"+search+"_members"+str(it)+".csv","w",encoding='UTF-8') as f:
                writer = csv.writer(f,delimiter=",",lineterminator="\n")
                writer.writerow(['serial_no','username','user_id', 'access_hash','name','group', 'group_id'])
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
                    writer.writerow([no,username,user.id,user.access_hash,name,target_group.title, target_group.id])  
                    no+=1    
            print(gr+'[+] Members scraped successfully.')

        except:
            print(re+'no permision is grated')
            continue


with client:
    client.loop.run_until_complete(main())

client.disconnect()
