
import segno
from PIL import Image
import pyzbar
from pyzbar.pyzbar import decode
#import lib
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
    read_qr = decode(Image.open('qrImg.png'))
    final = read_qr[0].data.decode('ascii')
    bot.send_message(msg.chat.id,final)
    

bot.infinity_polling()
    