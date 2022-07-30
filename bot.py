'''
import segno
#import cv2
import telebot
from telebot import TeleBot

bot = telebot.TeleBot('5418749173:AAHC7sk38lAoRf9GAD_9LrcmKbvZdVdM0HU')

@bot.message_handler(commands=['start'])
def welcome_message(msg):
    bot.send_message(msg.chat.id,f'Hello {msg.from_user.first_name} this is qrcode generator bot!')

@bot.message_handler(func=lambda m:True)
def generateQr(msg):
    text = msg.text
    qrcode = segno.make(text)
    qrcode.save('qrImg.png',scale=3)
    with open('qrImg.png','rb') as qr:
        bot.send_photo(msg.chat.id,qr,reply_to_message_id=msg.message_id)
        #read_qr = cv2.imread(qr)
        #bot.send_message(msg.chat.id,read_qr)
    

bot.infinity_polling()
'''

    

import pyqrcode
from qrtools import*
import telebot
from telebot import TeleBot

bot = telebot.TeleBot('5418749173:AAHC7sk38lAoRf9GAD_9LrcmKbvZdVdM0HU')

@bot.message_handler(commands=['start'])
def welcome_message(msg):
    bot.send_message(msg.chat.id,f'Hello {msg.from_user.first_name} this is qrcode generator bot!')

@bot.message_handler(func=lambda m:True)
def generateQr(msg):
    text = msg.text
    qrcode = pyqrcode.create(text)
    qrcode.png('result.png',scale=4)
    read_qr = qrtools.QR()
    read_qr.decode('result.png')
    read = read_qr.data
    with open('result.png','rb') as qr:
        bot.send_photo(msg.chat.id,qr,reply_to_message.id)
        bot.send_message(msg.chat.id,read)
 


bot.infinity_polling()
    
