
import qrcode
import telebot
import cv2
from telebot import TeleBot

bot = telebot.TeleBot('5418749173:AAGM1iwM_T_IMaJ-Lh2Dfhd_weNos8IiPQQ')

@bot.message_handler(commands=['start'])
def welcome_message(msg):
    bot.send_message(msg.chat.id,f'Hello {msg.from_user.first_name} this is qrcode generator bot!')

@bot.message_handler(func=lambda m:True)
def generateQr(msg):
    text = msg.text
    img = qrcode.make(text)
    #img.save('qr.png',scale=3)
    img.save("qr.png")
    with open('qr.png','rb') as qr:
        read_qr = cv2.imread(qr)
        detector = cv2.QRCodeDetector()
        read,q,r = detector.detectAndDecode(read_qr)
        bot.send_photo(msg.chat.id,qr,reply_to_message_id=msg.message_id)
        bot.reply_to(msg,read)
    
bot.infinity_polling()
    
