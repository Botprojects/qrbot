
import segno

try:
    import cv2
except ImportError:
    cv2 = None
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
        read_qr = cv2.imread(qr)
        detector = cv2.QRCodeDetector()
        read,q,r = detector.detectAndDecode(read_qr)
        bot.send_photo(msg.chat.id,qr,reply_to_message_id=msg.message_id)
        bot.reply_to(msg,read.text)
    
bot.infinity_polling()
    
