

import segno
from cv2 import cv2
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
    qrcode.save('qr.png',scale=3)
    read_qr = cv2.imread('qr.png')
    detector = cv2.QRCodeDetector()
    read = detector.detectAndDecode(read_qr)
    with open('qr.png','rb') as qr:
        bot.send_photo(msg.chat.id,qr,reply_to_message_id=msg.message_id)
        bot.reply_to(msg,read)
    
bot.infinity_polling()
    
