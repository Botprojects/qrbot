'''
import segno
import cv2
import telebot
from telebot import TeleBot

bot = telebot.TeleBot('5418749173:AAGM1iwM_T_IMaJ-Lh2Dfhd_weNos8IiPQQ')

@bot.message_handler(commands=['start'])
def welcome_message(msg):
    bot.send_message(msg.chat.id,f'Hello {msg.from_user.first_name} this is qrcode generator bot!')

@bot.message_handler(func=lambda m:True)
def generateQr(msg):
    text = msg.text
    qrcode = segno.make(text)
    qrcode.save('qr.png',scale=3)
    img = cv2.imread("qr.png")
    with open('qr.png','rb') as qr:
        decode = cv2.QRCodeDetector()
        read,qrimg,qrd = decode.detectAndDecode(img)
        bot.send_photo(msg.chat.id,qr,reply_to_message_id=msg.message_id)
        if qrimg is not None:
            print(f"result: {read}")
            bot.send_message(msg.chat.id,read)

bot.infinity_polling()
    
'''
import numpy
import segno
import cv2
import telebot
from telebot import TeleBot

bot = telebot.TeleBot('5418749173:AAGM1iwM_T_IMaJ-Lh2Dfhd_weNos8IiPQQ')

@bot.message_handler(commands=['start'])
def welcome_message(msg):
    bot.send_message(msg.chat.id,f'Hello {msg.from_user.first_name} this is qrcode generator bot!')

@bot.message_handler(func=lambda m:True)
def generateQr(msg):
    text = msg.text
    qrcode = segno.make(text)
    qrcode.save('qr.png',scale=3)
    with open('qr.png','rb') as qr:
        bot.send_photo(msg.chat.id,qr,reply_to_message_id=msg.message_id)

@bot.message_handler(func=lambda m:True,content_type=['photo'])
def readQr(msg):
    img = msg.photo
    img_np = numpy.frombuffer(img,numpy.uint8)
    img_data = cv2.imdecode(img_np,cv2.IMREAD_COLOR)
    detector = cv2.QRCodeDetector()
    data,bbox,straight_qrcode = detector.detectAndDecode(img_data)
    if bbox is not None:
        bot.send_message(msg.chat.id,data,reply_to_message_id=msg.message_id)
    else:
        bot.reply_to(msg,"Sorry i could not recognize qrcode!")
        

bot.infinity_polling()
    
