#####
#### Made with pytelegramApi and telebot module
#### RamailoBOT for https://t.me/Ramailo Community.
#### Github: 0xBibek
####
#####
import telebot
from telebot import types
import time
import sys
import string
import pause
from config import BOT_TOKEN
from utils.timedate import *
from utils.ping import ping
from utils.other import *

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda msg: msg.text == '/ping' or msg.text == '/ping@RamailoBot')
def send_message(message):
	bot.reply_to(message, ping(), parse_mode='HTML')

@bot.message_handler(func=lambda msg: msg.text == '/start' or msg.text == '/start@RamailoBot')
def send_welcome(message):
	bot.reply_to(message, "Welcome\nAccess via /help")

@bot.message_handler(func=lambda msg: msg.text == '/help' or msg.text == '/help@RamailoBot')
def send_welcome(message):
	bot.reply_to(message, helpinvalidmsg, parse_mode='HTML')

@bot.message_handler(commands=['gen'])
def send_welcome(message):
	bot.reply_to(message, geninvalidmsg, parse_mode='HTML')

@bot.message_handler(commands=['fun'])
def send_welcome(message):
	bot.reply_to(message, funinvalidmsg, parse_mode='HTML')

@bot.message_handler(commands=['pass'])
def send_message(message):
	bot.reply_to(message, passGen())

@bot.message_handler(commands=['token'])
def send_message(message):
	bot.reply_to(message, tokenGen())


@bot.message_handler(commands=['quote'])
def send_message(message):
	bot.reply_to(message, quote())

@bot.message_handler(commands=['joke'])
def send_message(message):
	bot.reply_to(message, joke())

@bot.message_handler(commands=['meme'])
def send_message(message):
	bot.reply_to(message, meme())

@bot.message_handler(func=lambda msg: msg.text == '/td' or msg.text == '/td@RamailoBot')
def send_message(message):
	bot.reply_to(message, td(), parse_mode='HTML')

@bot.message_handler(func=lambda msg: msg.text == '/revoke')
def send_message(message):
	if message.chat.type == "private":
		bot.reply_to(message, pvtinvalidmsg, parse_mode='HTML')
	else:
			chat_id = message.chat.id
			bot.export_chat_invite_link(chat_id)
			bot.reply_to(message, 'Invite Link has been <b>Revoked</b>.', parse_mode='HTML')

@bot.message_handler(func=lambda msg: msg.text == '/invitelink')
def send_message(message):
	if message.chat.type == "private":
		bot.reply_to(message, pvtinvalidmsg, parse_mode='HTML')
	else: 
		chat_id = message.chat.id
		ilink = bot.export_chat_invite_link(chat_id)
		bot.reply_to(message, ilink, parse_mode='HTML')

@bot.message_handler(func=lambda msg: msg.text == '/pin')
def send_message(message):
	if message.chat.type == "private":
		bot.reply_to(message, pvtinvalidmsg, parse_mode='HTML')
	else:
			chat_id = message.chat.id
			target_to_pin = message.reply_to_message.message_id
			bot.pin_chat_message(chat_id, target_to_pin)
			bot.reply_to(message, '<b>Pinned !! ;) </b>', parse_mode='HTML')

@bot.message_handler(func=lambda msg: msg.text == '/unpin')
def send_message(message):
	if message.chat.type == "private":
		bot.reply_to(message, pvtinvalidmsg, parse_mode='HTML')
	else:
			chat_id = message.chat.id
			target_to_pin = message.reply_to_message.message_id
			bot.unpin_chat_message(chat_id)
			bot.reply_to(message, '<b>UnPinned !! :( </b>', parse_mode='HTML')


bot.polling()