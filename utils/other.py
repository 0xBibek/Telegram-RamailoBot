import time
import random
import secrets
import requests
import json
import string

password_length = 10
possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%&*"

pvtinvalidmsg = f'''
<b>Sorry</b>, This command is not available at private.
''' 

helpinvalidmsg = f'''
🅒🅞🅜🅜🅐🅝🅓🅢
—————————————
<b>TimeDate:</b> /td
<b>Gen:</b> /gen 
<b>Fun:</b> /fun 
<b>Sys Ping:</b> /ping
'''

geninvalidmsg = f'''
<b>Token Gen:</b> /token
<b>Pass Gen:</b> /pass 

'''

funinvalidmsg = f'''
<b>Jokes:</b> /joke
<b>Quotes:</b> /quote
<b>Meme:</b> /meme
'''

def passGen():
	random_character_list = [random.choice(possible_characters) for i in range(password_length)]
	random_password = "".join(random_character_list)
	ranPass = random_password
	randomp = 'Random Password::\n' + ranPass
	return randomp

def tokenGen():
	ranToken = secrets.token_hex(32)
	tokenn = 'Random Token::\n' + ranToken
	return tokenn

def quote():
	quote = requests.get('https://api.quotable.io/random')
	quoteContent = quote.json()['content']
	quoteAuthor = quote.json()['author']
	quoteMsg = '' + quoteContent + ' - ' + quoteAuthor
	return quoteMsg

def joke():
	jyok = requests.get('https://official-joke-api.appspot.com/jokes/random')
	jyoksetup = jyok.json()['setup']
	jyokline = jyok.json()['punchline']
	jokeMsg = '' + jyoksetup + '\n' + jyokline
	return jokeMsg


def meme():
	memeget = requests.get('https://meme-api.herokuapp.com/gimme')
	memeSent = memeget.json()['url']
	memeMsg = '' + memeSent
	return memeMsg
