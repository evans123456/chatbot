
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer
import os


bot = ChatBot('Evans')
bot.set_trainer(ListTrainer) #to train the bot

#first time running you will need to uncomment bellow


# for files in os.listdir('C:/Users/admin/chatbot/conversations'):
# 	data = open('C:/Users/admin/chatbot/conversations/' + files ,'r').readlines()
# 	bot.train(data)

#comments are to prevent it from keeping on training when running

while True:
	message = input('You: ')
	if message.strip() != 'Bye':
		reply = bot.get_response(message)
		print('ChatBot: ',reply)
	else:
		print('ChatBot: Bye')
		break



