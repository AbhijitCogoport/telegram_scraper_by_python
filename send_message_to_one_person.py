from telethon.sync import TelegramClient, events

gr="\033[1;32m"
cy="\033[1;36m"

api_id = your_api_id_integer
api_hash = your_hash_token_string
name = your_name_string

client = TelegramClient( name , api_id, api_hash)

async def main():

    #you can send message if you have contact number
    mobile_no = input(gr+'Enter mobile number (+91##########):')
    message_to_send = input(gr+'Enter message to Send :')
    try:
        await client.send_message( mobile_no, message_to_send)
        print('>>>>>>>>>>>>>>message is done')
    except:
        print(cy+'not able to send message')

    #we can send message by user_id
    # user_id = input(gr+'Enter  user_id:')
    # message_to_send = input(gr+'Enter message to Send :')
    # await client.send_message(int(user_id),message_to_send)
  
with client:
    client.loop.run_until_complete(main())
 