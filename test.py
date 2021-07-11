from pyrogram import Client, filters

app = Client("tg_cleaner_bot",
api_id=4307689, api_hash='6b4631130cd2e5e3fbe6690f709c256b', bot_token='1896013920:AAG94P1OsfTe1lY99rnsO8zDClJkGNA1zjc')


@app.on_message()
def clear(client, message):    
    admin = app.get_chat_member(message.chat.id, message.from_user.id)['status']
    
    if message.text == '/clear' and admin != 'member':
     
	    members = app.get_chat_members(message.chat.id)
	    
	    count = 1
	    messages = []
	    idm = message.message_id
	    print(idm)
	    
	    for user in members:	    	
	    	is_admin = user['status']
	    	if is_admin == 'member':
	    		app.kick_chat_member(message.chat.id, user['user']['id'])
	    		messages.append(idm + count)
	    		count+= 1
	    		
	    print(messages)
	    app.delete_messages(chat_id=message.chat.id, message_ids=messages, revoke=False)	    		
	    
	   
app.run()