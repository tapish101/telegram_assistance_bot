import telebot
import datetime
from telebot.types import Message

time=datetime.datetime.now()
leave_msg=False
bot = telebot.TeleBot("paste public bot token")
msg_bot = telebot.TeleBot("paste private bot token")

def greeting():
    if time.hour>=14 and time.hour<17:
        return " Good Afternoon."
    if time.hour>=17 and time.hour<20:
        return " Good Evening."
    if time.hour>=20 and time.hour<23:
        return " Good Dark Night:)."
    if time.hour>=23 and time.hour<3:
        return " Its midnight and pretty dark outside, you night owl."
    if time.hour>=3 and time.hour<6:
        return " don't you think it's to early in the morning.."
    if time.hour>=6 and time.hour<11:
        return " Good Morning, Happy staring of the day."
    if time.hour>=11 and time.hour<14:
        return " Good Noon"


@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hey, '+message.chat.first_name+greeting()+"\nI am Tapish's bot here to help,\nHow can i help you?\n\n1.Call-Req a call from Tapish Talan\n2.Msg-Leave a message for Tapish\n\n3.URRGENT/IMPORTANT-Something imp to talk right now")
    
def input(message):
    msg=['1','2','3','call','msg','text','message','urrgent','imp','important']
    if message.text.lower() in msg:
        return True
    else:
        return False


@bot.message_handler(func=input)
def echo_all(message):
    global leave_msg
    msg=message.text.lower()
    if msg in ['1','call']:
        bot.send_message(message.chat.id,"Tapish Talan is requested to make a call to You.\nPlease have patience.")
        msg_bot.send_message("1639318508",message.chat.first_name+' '+message.chat.last_name+" wants to call you. User name is \n@"+message.chat.username)
    if msg in ['2','msg','message','text']:
        bot.send_message(message.chat.id,"OK. Send me the message you want to leave.....")
        leave_msg=True
    if msg in ['3','urrgent','important','imp']:
        bot.send_message(message.chat.id,"Tapish Talan will cantact you ASAP on your telegram account. (Your username @"+message.chat.username+" )")
        msg_bot.send_message("1639318508",message.chat.first_name+' '+message.chat.last_name+". Username @"+message.chat.username+"\nWants to talk to you, Its Urrgent.")


def leave_msgs(message):
    return leave_msg

@bot.message_handler(func=leave_msgs)
def msg(message):
    global leave_msg
    bot.send_message(message.chat.id,"Your message '"+message.text+"' has been forwarded to Tapish Talan.\n\nHappy to help you.")
    leave_msg=False
    msg_bot.send_message("1639318508",message.text+"\n\nMessage leave by "+message.chat.first_name+' '+message.chat.last_name+". Username @"+message.chat.username)



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Sorry, did not unerstand '"+message.text+"'")

bot.infinity_polling()
