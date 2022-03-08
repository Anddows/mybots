import telebot
import time
import musics
import adminsid
import speech_recognition as sr
from gtts import gTTS
from pyfiglet import Figlet
import mechanicalsoup as ms
import qrcode
import json
import calendar

downl = json.load


bot = telebot.TeleBot('1526588208:AAFWFWAOdl_Lw31phdlrtCAplw2PXSGUqbY')
API = "https://core.telegram.org/bots/api/{}"

button = telebot.types.ReplyKeyboardMarkup(True)
button2 = telebot.types.ReplyKeyboardMarkup(True)
button3 = telebot.types.ReplyKeyboardMarkup(True)
button4 = telebot.types.ReplyKeyboardMarkup(True)
button.row("DW versions", "Commands", "Errors")
button.row("Help")

button2.row("Gipermatn belgilash tili")
button2.row("cascading style sheets")
button2.row("Giper havola")

button3.row("🔗 Telegram")
button3.row("🔗 Instagram")
button3.row("🔗 Web")

@bot.message_handler(commands=['start'])
def start_message(message):
    with open('groupsid.py', 'a') as f:
        f.write(f' {message.chat.id},')
    bot.reply_to(message, "k1ngdw 1.9.4")

@bot.message_handler(commands=['botstartadmin'])
def admin_message(message):
    if message.from_user.id:
       bot.reply_to(message, "done!")

    else:
        bot.leave_chat(message.chat.id)
# @bot.message_handler(commands=['id_ban'])
# def kick_users(message):
#     if message.from_user.id == 696084613:
#         if message.reply_to_message:
#             text = message.reply_to_message.from_user.id
#             bot.kick_chat_member(message.chat.id, text)
#             bot.send_message(message.chat.id, "Done!" .format(message, text))

    # else:
    #     bot.send_message(message.chat.id, "do you not moder")

#kick2 itaci 869582467, saske 1451015386



@bot.message_handler(is_admin = True, commands=['kdban'])
def kick2_users(message):
          if message.reply_to_message:
             text = message.reply_to_message.from_user.id
             bot.kick_chat_member(message.chat.id, text)
             bot.send_message(message.chat.id, "Done!" .format(message, text))

          else:
             bot.send_message(message.chat.id, "do you not moder")

    # else:
    #     bot.send_message(message.chat.id, "do you not moder")

@bot.message_handler(is_admin = True, commands=['kdmute'])
def mute_users(message): 
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.restrict_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Done! user is muted")

        else:
            bot.send_message(message.chat.id, "do you not moder")

@bot.message_handler(commands=['image'])
def img_group(message):
        with open("images8.jpg", "rb") as f:
            img = f.read()
        bot.send_photo(photo = img, chat_id = message.chat.id)

@bot.message_handler(is_admin = True, commands=['kdunmute'])
def unmute_users(message):
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.promote_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Done! user is unmuted")

        else:
            bot.send_message(message.chat.id, "do you not moder")


# @bot.message_handler(commands=['test'])
# def test_users(message):
#     msg = bot.send_message(message.chat.id, "Ism va Familiyangizni kiriting\n\nIsmingiz Familiyangiz")
#     bot.register_next_step_handler(msg, htmltest)


@bot.message_handler(is_admin = True, commands=['kdunban'])
def unban_users(message):
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.unban_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Done! user is unbanned")

@bot.message_handler(commands=['info'])
def spam_users(message):
    if message.from_user.id in adminsid.admins_id:
       spam_message = "DW\n\nName: k1ngdw\nUsername: @mynew885bot\nGroup: yes\nby @Code_Idea\nversion: 1.9.4"
       bot.send_message(message.chat.id, spam_message)

@bot.message_handler(commands=['news'])
def my_message(message):
    bot.send_message(message.chat.id, "пусто")

@bot.message_handler(content_types=['new_chat_members'])
def new_member_text(message):
        bot.reply_to(message, f'Salom <a href="https://t.me/{message.from_user.username}"><b>{message.from_user.first_name}</b></a> Guruhimizga hush kelibsiz.\n\nHurmatingizni bilib yozing.', parse_mode = 'HTML', disable_web_page_preview=True)
        bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(content_types=['left_chat_member'])
def left_member_text(message):
     bot.reply_to(message, f'<a href="https://t.me/{message.from_user.username}"><b>{message.from_user.first_name}</b></a> Guruhni tark etdi', parse_mode = 'HTML', disable_web_page_preview=True)
     bot.delete_message(message.chat.id, message.message_id)

# @bot.message_handler(content_types=['text'])
# def send_message2(message):
#   if message.text.lower() == "new name":
#       mesg = bot.send_message(message.chat.id,'Please send me your new title')
#       bot.register_next_step_handler(mesg,test)

# def test(message):
#     title = message.text
#     bot.set_chat_title(message.chat.id, f"{title}")
#     bot.send_message(message.chat.id,'Done!')

@bot.message_handler(content_types=['text'])
def send_message(message):

 if message.text.lower() == "бан":
    if message.from_user.id in adminsid.admins_id:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.kick_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Полизователь забанен" )





 elif message.text.lower() == "css background code":
        bot.send_message(message.chat.id, "password:")

 elif message.text.lower() == "1515":
       bot.send_message(message.chat.id, "Css backround code\n\nbody {\nbackground-position: center;\nbackground-size: cover;\nbackground-attachment: fixed;")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# admin panel

 elif message.text.lower() == "admin panel":
        if message.from_user.id ==  696084613:
              bot.send_message(message.chat.id, "Welcome Admin Panel", reply_markup = button)

 elif message.text.lower() == "admin panel with password":
       password = bot.send_message(message.chat.id, "enter password Admin Panel")
       bot.register_next_step_handler(password, buttonadmin)

 elif message.text.lower() == "help":
       bot.send_message(message.chat.id, "Help\n\nupdating...")

 elif message.text.lower() == '{bot = l.admin => w.reply}':
     try:
      if message.from_user.id in adminsid.admins_id:
          with open('mybots/adminsid.py', 'a') as f:
             f.write(f'{message.reply_to_message.from_user.id},')
          bot.send_message(message.chat.id, "Done!")
          bot.delete_message(message.chat.id, message.message_id)
     except:
          bot.send_message(message.chat.id, "Commands error:" + " <em>'{bot = [i.r?]}</em>'", parse_mode = 'HTML')

 elif message.text.lower() == 'bot => admin.reply':
     try:
      if message.from_user.id in adminsid.admins_id:
          with open('https://www.pythonanywhere.com/user/ibrohim885/files/home/ibrohim885/bot/adminsid.py', 'a') as f:
             f.write(f'{message.reply_to_message.from_user.id},')
          bot.send_message(message.chat.id, "Done!")
          bot.delete_message(message.chat.id, message.message_id)
     except:
          bot.send_message(message.chat.id, "Commands error:" + " <em>'{bot = [i.r?]}</em>'", parse_mode = 'HTML')

 elif message.text.lower() == "i2":
    if message.from_user.id in adminsid.admins_id:
        bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_delete_messages = True, can_pin_messages = True)
        bot.set_chat_administrator_custom_title(message.chat.id, message.reply_to_message.from_user.id, "i2")
        bot.send_message(message.chat.id, f'<b> {message.reply_to_message.from_user.first_name} </b> siz faqat habarlarni o\'chira olasiz va pin qila olasiz i2', parse_mode = 'HTML')
        bot.delete_message(message.chat.id, message.message_id)
 elif message.text.lower() == "i1":
  try:
    if message.from_user.id in adminsid.admins_id:
        bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_delete_messages = True)
        bot.set_chat_administrator_custom_title(message.chat.id, message.reply_to_message.from_user.id, "i1")
        bot.send_message(message.chat.id,f'<b> {message.reply_to_message.from_user.first_name} </b> siz faqat habarlarni o\'chira olasiz i1', parse_mode='HTML')
        bot.delete_message(message.chat.id, message.message_id)
  except:
      bot.send_message(message.chat.id, "Error")
 elif message.text.lower() == "i3":
  try:
    if message.from_user.id in adminsid.admins_id:
        bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_delete_messages=True, can_pin_messages=True, can_restrict_members = True)
        bot.set_chat_administrator_custom_title(message.chat.id, message.reply_to_message.from_user.id, "i3")
        bot.send_message(message.chat.id, f'<b> {message.reply_to_message.from_user.first_name} </b> siz faqat habarlarni o\'chira olasiz va pin qila olasiz, foydalanuvchilarni mute qila olasiz', parse_mode='HTML')
        bot.delete_message(message.chat.id, message.message_id)
  except:
      bot.send_message(message.chat.id, "Error")
 elif message.text.lower() == "i4":
  try:
    if message.from_user.id in adminsid.admins_id:
        bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_delete_messages=True, can_pin_messages=True, can_restrict_members=True, can_manage_chat = True)
        bot.set_chat_administrator_custom_title(message.chat.id, message.reply_to_message.from_user.id, "i4")
        bot.send_message(message.chat.id, f'<b> {message.reply_to_message.from_user.first_name} </b> siz faqat habarlarni o\'chira olasiz va pin qila olasiz, foydalanuvchilarni mute, chatni boshqara olasiz', parse_mode='HTML')
        bot.delete_message(message.chat.id, message.message_id)
  except:
      bot.send_message(message.chat.id, "Error")
 elif message.text.lower() == "i5":
  try:
    if message.from_user.id in adminsid.admins_id:
        bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_delete_messages=True,
                                can_pin_messages=True, can_restrict_members=True, can_manage_chat=True, can_manage_voice_chats = True)
        bot.send_message(message.chat.id,
                         f'<b> {message.reply_to_message.from_user.first_name} </b> siz faqat habarlarni o\'chira olasiz va pin qila olasiz, foydalanuvchilarni mute, chatni, oavozli chatlarni boshqara olasiz',
                         parse_mode='HTML')
        bot.set_chat_administrator_custom_title(message.chat.id, message.reply_to_message.from_user.id, "i5")
        bot.delete_message(message.chat.id, message.message_id)
  except:
       bot.send_message(message.chat.id, "Error")
 elif message.text.lower() == "i6":
  try:
    if message.from_user.id in adminsid.admins_id:
        bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_delete_messages=True, can_pin_messages=True, can_restrict_members=True, can_manage_chat=True, can_manage_voice_chats = True, can_promote_members=True)
        bot.send_message(message.chat.id, f'<b> {message.reply_to_message.from_user.first_name} </b> admin i6 habar o\'chira olasiz\npin qila olasiz\nfoydalanuvchilarni mute qila olasiz\nchatni, ovozli chatlarni boshqara olasiz\nfoydalanuvchini admin qila olasiz', parse_mode='HTML')
        bot.delete_message(message.chat.id, message.message_id)
        bot.set_chat_administrator_custom_title(message.chat.id, message.reply_to_message.from_user.id, "i6")
  except:
       bot.send_message(message.chat.id, "Error")
 elif message.text.lower() == "i7":
  try:
    if message.from_user.id in adminsid.admins_id:
        bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_delete_messages=True, can_pin_messages=True, can_restrict_members=True, can_manage_chat=True, can_manage_voice_chats = True, can_promote_members=True, can_edit_messages = True)
        bot.set_chat_administrator_custom_title(message.chat.id, message.reply_to_message.from_user.id, "i7")
        bot.send_message(message.chat.id, f'<b> {message.reply_to_message.from_user.first_name} </b> admin i7 hamma imkoniyatlarga egasiz', parse_mode='HTML')
        bot.delete_message(message.chat.id, message.message_id)
  except:
       bot.send_message(message.chat.id, "Error")
 elif message.text.lower() == "i0":
  try:
    if message.from_user.id in adminsid.admins_id:
        bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_delete_messages=None, can_pin_messages=None, can_restrict_members=None, can_manage_chat=None, can_manage_voice_chats = None, can_promote_members=None, can_edit_messages = None)
        bot.send_message(message.chat.id, f'<b> {message.reply_to_message.from_user.first_name} </b> admindan olindingiz',parse_mode='HTML')
        bot.delete_message(message.chat.id, message.message_id)
  except:
        bot.send_message(message.chat.id, '<b>error</b>', parse_mode='HTML')
        


 elif message.text.lower() == "admin = w.reply":
#     if message.from_user.id in adminsid.admins_id:
        bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id,can_delete_messages=True, can_pin_messages=True, can_restrict_members=True,  can_promote_members=True, can_change_info=True, can_invite_users = True)
        bot.send_message(message.chat.id, f'<b> {message.reply_to_message.from_user.first_name} </b> successfully you are admin', parse_mode='HTML')
        bot.delete_message(message.chat.id, message.message_id)
        bot.set_chat_administrator_custom_title(message.chat.id, message.reply_to_message.from_user.id, "admin")



# ----------------------------------------------------------------------------------------------------------------------------------------------------------

 elif message.text.lower() == "разбан":
     if message.from_user.id in adminsid.admins_id:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.unban_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Полизователь разбанен" )



 elif message.text.lower() == "мут":
     if message.from_user.id in adminsid.admins_id:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.restrict_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Полизователь замутен" )

 elif message.text.lower() == "мут 01":
    if message.from_user.id in adminsid.admins_id:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.restrict_chat_member(message.chat.id, text, message.date + 60)
            bot.send_message(message.chat.id, "Полизователь замутен" )

    # while True:
    #       bot.send_message(message.chat.id, '🤦‍♂️')


 elif message.text.lower() == "размут":
    if message.from_user.id in adminsid.admins_id:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.promote_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Полизователь размутен" )

 elif message.text.lower() == 'dw':
    bot.send_message(message.chat.id, 'I am here')


 elif message.text.lower() == 'my id':
    bot.send_message(message.chat.id, 'id: {}'.format(message.from_user.id))

 elif message.text.lower() == 'your id':
   try:
     if message.reply_to_message:
        text = message.reply_to_message.from_user.id
        bot.send_message(message.chat.id, 'id: {}'.format(message.reply_to_message.from_user.id))
   except:
       bot.send_message(message.chat.id, "Siz reply orqali kiritmagansiz")

 elif message.text.lower() == '{bot p.admin => del}':
     try:
      if message.reply_to_message:
          message.reply_to_message.from_user.id
          bot.promote_chat_member(message.reply_to_message.from_user.id, can_delete_messages = True)
     except:
         bot.send_message(message.chat.id, "Xatolik yuz berdi")
 elif message.text.lower() == '!m':
     bot.send_message(message.chat.id, f'first name: {message.from_user.first_name}\nusername: @{message.from_user.username}\nid: {message.from_user.id}')

 elif message.text.lower() == '!y':
   try:
     if message.reply_to_message:
        text = message.reply_to_message.from_user.id
        bot.send_message(message.chat.id, f'first name: {message.reply_to_message.from_user.first_name}\nusername: @{message.reply_to_message.from_user.username}\nid: {message.reply_to_message.from_user.id}')
   except:
        bot.send_message(message.chat.id, "Siz reply orqali kiritmagansiz")

 elif message.text.lower() == 'your uname':
   try:
     if message.reply_to_message:
        text = message.reply_to_message.from_user.id
        bot.send_message(message.chat.id, 'username: @{}'.format(message.reply_to_message.from_user.username))
   except:
       bot.send_message(message.chat.id, "Siz reply orqali kiritmagansiz")

 elif message.text.lower() == 'your fname':
   try:
     if message.reply_to_message:
        text = message.reply_to_message.from_user.id
        bot.send_message(message.chat.id, 'first name: {}'.format(message.reply_to_message.from_user.first_name))
   except:
       bot.send_message(message.chat.id, "Siz reply orqali kiritmagansiz")

 elif message.text.lower() == 'my uname':
    bot.send_message(message.chat.id, 'username: @{}'.format(message.from_user.username))

 elif message.text.lower() == 'my fname':
    bot.send_message(message.chat.id, 'first name: {}'.format(message.from_user.first_name))

 elif message.text.lower() == 'group id':
    bot.send_message(message.chat.id, 'group id: {}'.format(message.chat.id))

 elif message.text.lower() == 'group fname':
    bot.send_message(message.chat.id, 'group name: {}'.format(message.chat.title))


 elif message.text.lower() == 'group uname':
    bot.send_message(message.chat.id, 'group username: @{}'.format(message.chat.username))

 elif message.text.lower() == 'commands danger wolf':
    bot.send_message(message.chat.id, 'commands:\n\nkd ban - ban berish\nkd unban - bandan chiqarish\nkd mute - mute berish\nkd unmute - mutedan chiqarish\n?kd mute to 1 - 1 soat mute berish\n?kd mute to 01 - 1 min mute berish\n?kd kick - guruhdan chiqarish\n?kd ban id - id orqali ban berish')


#  elif message.text.lower() == "mute":
#     bot.set_chat_permissions(message.chat.id, can_send_messages=None, can_send_media_messages=None, can_send_stickers=True, can_send_animations=True)
#     bot.send_message(message.chat.id, "Done! group is muted")

 elif message.text.lower() == 'unmute':
    bot.send_message(message.chat.id, 'group unmuted to 8:00')

 elif message.text.lower().startswith('!rek '):
   try:
     bot.pin_chat_message(message.chat.id, message.message_id)
     print("pinned")
   except:
         bot.send_message(message.chat.id, "Xatolik yuz berdi")

#  elif message.text.lower().startswith('https'):
#      bot.send_message(message.chat.id, '@{} Reklama yuborish Taqiqlangan'.format(message.from_user.username))
#      bot.delete_message(message.chat.id, message.message_id)
#      bot.restrict_chat_member(message.chat.id, message.from_user.id, message.date + 60)

#  elif message.text.lower().startswith('http'):
#      bot.send_message(message.chat.id, '@{} Reklama yuborish Taqiqlangan '.format(message.from_user.username))
#      bot.delete_message(message.chat.id, message.message_id)
#      bot.restrict_chat_member(message.chat.id, message.from_user.id, message.date + 60)

# #  elif message.text.lower().startswith('@'):
# #      bot.send_message(message.chat.id, '@{} Пожалуйста, не размещайте рекламу '.format(message.from_user.username))
# #      bot.delete_message(message.chat.id, message.message_id)

#  elif message.text.lower().startswith('t.me/'):
#      bot.send_message(message.chat.id, '@{} Reklama yuborish Taqiqlangan'.format(message.from_user.username))
#      bot.delete_message(message.chat.id, message.message_id)
#      bot.restrict_chat_member(message.chat.id, message.from_user.id, message.date + 60)

#  elif message.text.lower().startswith('telegram/me'):
#      bot.send_message(message.chat.id, '@{} Reklama yuborish Taqiqlangan '.format(message.from_user.username))
#      bot.delete_message(message.chat.id, message.message_id)
#      bot.restrict_chat_member(message.from_user.id, message.from_user.id, message.date + 60)

#  elif message.text.lower().startswith('сук'):
#      bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
#      bot.delete_message(message.chat.id, message.message_id)

#  elif message.text.lower().startswith('cучка'):
#      bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
#      bot.delete_message(message.chat.id, message.message_id)

# #  elif message.text.lower().startswith('бл'):
# #      bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
# #      bot.delete_message(message.chat.id, message.message_id)

#  elif message.text.lower().startswith('нах'):
#      bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
#      bot.delete_message(message.chat.id, message.message_id)

#  elif message.text.lower().startswith('иди н'):
#      bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
#      bot.delete_message(message.chat.id, message.message_id)

#  elif message.text.lower().startswith('мат'):
#      bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
#      bot.delete_message(message.chat.id, message.message_id)

#  elif message.text.lower().startswith('Ма'):
#      bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
#      bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('пащол'):
     bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо  '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('пашол'):
     bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('suk'):
     bot.send_message(message.chat.id, '@{} iltimos odob saqlang! '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('sek'):
     bot.send_message(message.chat.id, '@{} Iltimos odob saqlang '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('jala'):
     bot.send_message(message.chat.id, '@{} пожалуйста, говорите хорошо '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('dnx'):
     bot.send_message(message.chat.id, '@{} Iltimos odob saqlang '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('idi n'):
     bot.send_message(message.chat.id, '@{} Iltimos odob saqlang '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('pawol n'):
     bot.send_message(message.chat.id, '@{} Iltimos odob saqlang '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('pashol n'):
     bot.send_message(message.chat.id, '@{} Iltimos odob saqlang '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('pida'):
     bot.send_message(message.chat.id, '@{} Iltimos odob saqlang '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('eneni'):
     bot.send_message(message.chat.id, '@{} Iltimos odob saqlang '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('ayen'):
     bot.send_message(message.chat.id, '@{} Iltimos odob saqlang '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower().startswith('onen'):
     bot.send_message(message.chat.id, '@{} Iltimos odob saqlang '.format(message.from_user.username))
     bot.delete_message(message.chat.id, message.message_id)



 elif message.text.lower() == "info id bot":
     bot.send_message(message.chat.id, "Please input your password:")
     bot.send_message(message.chat.id, "password:")

 elif message.text.lower() == "well":
     if message.chat.type == "private":
      text = "thanks"
      bot.send_chat_action(message.chat.id, 'typing')
      time.sleep(3)
      bot.send_message(message.chat.id, text)

     #chat ceper bot id 553147242

#-1001430159008 id test bots group
 elif message.text.lower() == "привет всем":
     bot.send_message(-1001430159008, "привет")

 elif message.text.lower() == "5555":
     bot.send_message(message.chat.id, "Yor password is true. For get info write /info")
     bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower() == "hacking...":
     bot.send_message(message.chat.id, "hacking... 10%")
     time.sleep(10)
     bot.delete_message(message.chat.id, message.message_id +1)

     bot.send_message(message.chat.id, "hacking... 50%")
     time.sleep(10)
     bot.delete_message(message.chat.id, message.message_id +2)

     bot.send_message(message.chat.id, "hacking... 80%")
     time.sleep(10)
     bot.delete_message(message.chat.id, message.message_id +3)

     bot.send_message(message.chat.id, "hacking... 100%")
     bot.send_message(message.chat.id, "send me password")


 elif message.text.lower() == "1111":
     bot.send_message(message.chat.id, "Hacking password is true. For get info write /info, commands id bot, info h5 id bot")
     bot.delete_message(message.chat.id, message.message_id)


 elif message.text.lower() == "kd ban":
    if message.from_user.id in adminsid.admins_id:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.kick_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "ok. User guruhdan chiqarildi" )



            #kick command


#  elif message.text.lower() == "dcommandban":
#     # if message.from_user.id == 696084613:
#         if message.reply_to_message:
#             text = message.reply_to_message.from_user.id
#             bot.kick_chat_member(message.chat.id, text)
#             bot.kick_chat_member(message.chat.id, text)
#             bot.kick_chat_member(message.chat.id, text)
#             bot.kick_chat_member(message.chat.id, text)
#             bot.kick_chat_member(message.chat.id, text)
#             bot.send_message(message.chat.id, "dcommandban" )
#             bot.send_message(message.chat.id, "dcommandban" )
#             bot.send_message(message.chat.id, "dcommandban" )
#             bot.send_message(message.chat.id, "dcommandban" )
#             bot.send_message(message.chat.id, "dcommandban" )
#             bot.send_message(message.chat.id, "getting ban..." )
#             time.sleep(3)
#             bot.send_message(message.chat.id, "getting ban..., else try again" )



 elif message.text.lower() == "?kd ban":
     try:
      if message.from_user.id in adminsid.admins_id:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.kick_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Done! User is banned" )
     except:
         bot.send_message(message.chat.id, "Siz adminga ban bera olmaysiz")
            
 
 elif message.text.lower() == "?kd vban":
     try:
        if message.reply_to_message:
            text = bot.send_message(message.chat.id, "you can vote with reply")
            bot.register_next_step_handler(text, ban2)
     except:
         bot.send_message(message.chat.id, "Siz adminga ban bera olmaysiz")
            
 elif message.text.lower() == "?kd vmute":
     try:
        if message.reply_to_message:
            text = bot.send_message(message.chat.id, "you can vote with reply")
            bot.register_next_step_handler(text, mute2)
     except:
         bot.send_message(message.chat.id, "Siz adminga mute bera olmaysiz")

 elif message.text.lower() == "?kd kick":
    if message.from_user.id in adminsid.admins_id:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.kick_chat_member(message.chat.id, text, message.date + 1 )
            bot.send_message(message.chat.id, "Done! User is kicked" )

 elif message.text.lower() == "?kd unban":
    if message.from_user.id in adminsid.admins_id:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.unban_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Done! User is unbanned" )

 elif message.text.lower() == "kd unban":
    if message.from_user.id in adminsid.admins_id:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.unban_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "ok. User guruhga yana qayta oladi" )

 elif message.text.lower() == "kd mute":
    if message.from_user.id in adminsid.admins_id:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.restrict_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "ok. User yozishdan cheklab qo'yildi" )


 elif message.text.lower() == "kd mute 01":
    if message.from_user.id in adminsid.admins_id:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.restrict_chat_member(message.chat.id, text, message.date + 60)
            bot.send_message(message.chat.id, "ok. User yozishdan vaqtincha cheklab qo'yildi" )


 elif message.text.lower() == "kd unmute":
    if message.from_user.id in adminsid.admins_id:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.promote_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "ok. User yana yoza oladi" )



 elif message.text.lower() == "?kd mute to 01":
    if message.from_user.id in adminsid.admins_id:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.restrict_chat_member(message.chat.id, text, message.date + 60)
            bot.send_message(message.chat.id, "Well Done! user is muted" )
            time.sleep(60)
            bot.send_message(message.chat.id, "User is unmuted")


 elif message.text.lower() == "?kd mute to 1":
    if message.from_user.id in adminsid.admins_id:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.restrict_chat_member(message.chat.id, text, message.date + 600)
            bot.send_message(message.chat.id, "Well Done! user is muted")


 elif message.text.lower() == "?kd unmute":
    if message.from_user.id in adminsid.admins_id:
        if message.reply_to_message:
            text = message.reply_to_message.from_user.id
            bot.promote_chat_member(message.chat.id, text)
            bot.send_message(message.chat.id, "Done! user is unmuted" )


 elif message.text.lower().startswith('save note '):
    text = message.text
    with open('db.json', 'a') as f:
       f.write(text)
    bot.send_message(message.chat.id, "Done! your note is saved!")

 elif message.text.lower() == "history note":
    bot.get_text(text = data.txt, chat_id=message.chat.id)



 elif message.text.lower() == "danger wolf":
     text = "Shu yerda"
     bot.send_chat_action(message.chat.id, 'typing')
     time.sleep(3)
     bot.send_message(message.chat.id, text)

 elif message.text.lower() == "!pydroid":
     bot.send_chat_action(message.chat.id, 'typing')
     text = "hi"
     bot.edit_message_text(message.edit.id, text)


 elif message.text.lower() == "k1ngdw":
     text = "Shu yerda"
     bot.send_chat_action(message.chat.id, 'typing')
     time.sleep(3)
     bot.send_message(message.chat.id, text)

 elif message.text.lower() == "salom":
     text = "+"
     bot.send_chat_action(message.chat.id, 'typing')
     time.sleep(3)
     bot.send_message(message.chat.id, text)

 elif message.text.lower() == "!scan group":
     text = "kim dir bizni kuzatmoqda"
     bot.send_chat_action(message.chat.id, 'typing')
     time.sleep(3)
     bot.send_message(message.chat.id, text)

 elif message.text.lower() == "salom":
     text = "salom szga ham"
     bot.send_chat_action(message.chat.id, 'typing')
     time.sleep(3)
     bot.send_message(message.chat.id, text)

 elif message.text.lower() == "more info dwbot":
     text = "Danger Wolf bot h5"
     bot.send_chat_action(message.chat.id, 'typing')
     time.sleep(3)
     bot.send_message(message.chat.id, text)


 elif message.text.lower() == "!get spys":
     text = "getting..."
     bot.send_chat_action(message.chat.id, 'typing')
     time.sleep(3)
     bot.send_message(message.chat.id, text)
     time.sleep(5)
     bot.send_message(message.chat.id, text)
     time.sleep(5)
     bot.send_message(message.chat.id, text)
     time.sleep(5)
     bot.send_message(message.chat.id, text)
     bot.send_message(message.chat.id, 'error, try again')

 elif message.text.lower() == "commands":
     bot.send_message(message.chat.id, '<b><em>Danger Wolf Commands</em></b>\n\n<a href="https://anddows.github.io/dwnews.html">1.11 beta</a>', parse_mode = 'HTML')

#  elif message.text.lower() == "weather":
#      bot.send_messsage(message.chat.id, "Weather:\n\n")



 elif message.text.lower() == "!?get spys id":
     text = "getting id..."
     bot.send_chat_action(message.chat.id, 'typing')
     time.sleep(3)
     bot.send_message(message.chat.id, text)
     time.sleep(5)
     bot.send_message(message.chat.id, text)
     time.sleep(5)
     bot.send_message(message.chat.id, text)
     time.sleep(5)
     bot.send_message(message.chat.id, text)
     bot.send_message(message.chat.id, 'error, try again')


 elif message.text.lower() == "!15 3 5":
     text = "15 3 5 5 8 25 15..."
     bot.send_chat_action(message.chat.id, 'typing')
     time.sleep(3)
     bot.send_message(message.chat.id, text)
     time.sleep(5)
     bot.send_message(message.chat.id, text)
     time.sleep(5)
     bot.send_message(message.chat.id, text)
     time.sleep(5)
     bot.send_message(message.chat.id, text)
     bot.send_message(message.chat.id, '3 4 4 9 4, 5 4 6 11 15 11 8 25')

 elif message.text.lower() == "24 11 25":
     text = "9 13 9 15 3"
     bot.send_chat_action(message.chat.id, 'typing')
     time.sleep(3)
     bot.send_message(message.chat.id, text)

 elif message.text.lower() == "dw news":
     text = "k1ngdw Updated to 1.9.4\n\nvote ban, vote mute, ?kd vban, ?kd vmute with reply\n\nhttps://anddows.github.io/dwhelper.html"
     bot.send_chat_action(message.chat.id, 'typing')
     time.sleep(3)
     bot.send_message(message.chat.id, text)

 elif message.text.lower() == "dw versions":
     text = "k1ngdw 1.0\nk1ngdw 1.3\nk1ngdw 1.3 pro\nk1ngdw 1.4\nk1ngdw 1.5 beta\nk1ngdw 1.5.0 beta pro\nk1ngdw 1.6\nk1ngdw 1.7\nk1ngdw 1.8\nk1ngdw 1.9\nk1ngdw 1.9.1\nk1ngdw 1.9.2\nk1ngdw 1.10 beta\nk1ngdw 1.11 beta\nk1ngdw 1.9.3 beta test version\nk1ngdw 1.9.4"
     bot.send_chat_action(message.chat.id, 'typing')
     time.sleep(3)
     bot.send_message(message.chat.id, text)

 elif message.text.lower() == "!pydroid 3":
     text = "Play Marketdan Pydroid 3 ni yuklang"
     bot.send_chat_action(message.chat.id, 'typing')
     time.sleep(3)
     bot.send_message(message.chat.id, text)

 elif message.text.lower() == "!rec audio":
     bot.send_chat_action(message.chat.id, 'record_audio')
     time.sleep(3)
     with open('voice1.ogg', 'rb') as f:
        audio = f.read()
     bot.send_audio(audio = audio, chat_id=message.chat.id)

 elif message.text.lower() == "kd del":
        if message.reply_to_message:
            text = message.reply_to_message.id
            bot.send_message(message.chat.id, "Done message deleted" )
            bot.delete_message(message.chat.id, text)

 elif message.text.lower() == "!kd pin":
        if message.reply_to_message:
            text = message.reply_to_message.id
            time.sleep(2)
            bot.delete_message(message.chat.id, message.message_id)
            bot.pin_chat_message(message.chat.id, text)


 elif message.text.lower().startswith('!savol '):
   try:
     bot.pin_chat_message(message.chat.id, message.message_id)
     print("pinned")
   except:
         bot.send_message(message.chat.id, "Xatolik yuz berdi")

 elif message.text.lower() == "pin id":
     pin = bot.send_message(message.chat.id, "id:")
     bot.register_next_step_handler(pin, pinmsg)

 elif message.text.lower() == "unpin id":
     unpin = bot.send_message(message.chat.id, "id:")
     bot.register_next_step_handler(unpin, unpinpinmsg)


 elif message.text.lower() == "!kd unpin":
        if message.reply_to_message:
            text = message.reply_to_message.id
            time.sleep(2)
            bot.delete_message(message.chat.id, message.message_id)
            bot.unpin_chat_message(message.chat.id, text)

#  elif message.text.lower() == "kd set photo":
#       mesg = bot.send_message(message.chat.id,'Please send me your new title')
#       bot.register_next_step_handler(mesg,photo)


 elif message.text.lower() == "?del":
  try:
    #   bot.send_message(message.chat.id, "")
      bot.delete_message(message.chat.id, message.message_id)
      if message.reply_to_message:
            text = message.reply_to_message.id
            # bot.send_message(message.chat.id, "Done message deleted" )
            bot.delete_message(message.chat.id, text)
            # bot.delete_message(message.chat.id, message.message_id)
  except:
     bot.send_message(message.chat.id, "{bot = [i.r?]}")

 elif message.text.lower() == "13 3 19":
    #   bot.send_message(message.chat.id, "")
      bot.delete_message(message.chat.id, message.message_id)
      if message.reply_to_message:
            text = message.reply_to_message.id
            # bot.send_message(message.chat.id, "Done message deleted" )
            bot.delete_message(message.chat.id, text)
            # bot.delete_message(message.chat.id, message.message_id)

#  elif message.text.lower() == "?kd ban id":
#     kick = bot.send_message(message.chat.id, "id:")
#     bot.register_next_step_handler(kick, idforkick)

# @bot.message_handler(content_types = ['text'])
# def idforkick(message):
#   bot.kick_chat_member(message.chat.id, message.text)
#   bot.send_message(message.chat.id, "Done! User is kicked")

 elif message.text.lower() == "new name":
       mesg = bot.send_message(message.chat.id,'Please send me your new title')
       bot.register_next_step_handler(mesg,test)

 elif message.text.lower() == "new desc":
       mesg = bot.send_message(message.chat.id,'Please send me your new text for description')
       bot.register_next_step_handler(mesg,newdesc)

 elif message.text.lower() == "new admin name":
    #  if message.reply_to_message:
    #     text = message.reply_to_message.from_user.id
        admin = bot.send_message(message.chat.id, 'new admin title:')
        bot.register_next_step_handler(admin, newadmin)
        # bot.set_chat_administrator_custom_title(message.chat.id, text)
        # bot.send_message(message.chat.id,'Done!')

 elif message.text.lower() == "?kd ban id":
    if message.from_user.id in adminsid.admins_id:
       kick = bot.send_message(message.chat.id, "id:")
       bot.register_next_step_handler(kick, idforkick)

#  elif message.text.lower() == "send image":
#      if message.text.from_user.id == "696084613":
#         with open('img.jpg', 'rb') as f:
#             img = f.read()
#       bot.send_photo(photo = img, chat_id = message.chat.id)
#       bot.send_message(message.chat.id, "Done")

 elif message.text.lower() == "my name":
     bot.send_message(message.chat.id,
                                      'elif "*myname" in event.raw_text:\n        '
                                            'await event.edit(">_ ib_")\n        '
                                            'await event.edit(">_ ibr_")\n        '
                                            'await event.edit(">_ ibro_")\n        '
                                            'await event.edit(">_ ibroh_")\n        '
                                            'await event.edit(">_ ibrohi_")\n        '
                                            'await event.edit(">_ ibrohim_")\n        '
                                            'await event.edit("ibrohim")')

 elif message.text.lower() == "?kd mute id":
    if message.from_user.id in adminsid.admins_id:
      mute = bot.send_message(message.chat.id, 'id:')
      bot.register_next_step_handler(mute, idformute)

 elif message.text.lower() == "?kd unmute id":
    if message.from_user.id in adminsid.admins_id:
      mute = bot.send_message(message.chat.id, 'id:')
      bot.register_next_step_handler(mute, idforunmute)

#  if message.chat.type == 'private':
 elif message.text.lower() == "ban":
     bot.send_message(message.from_user.id, "Ban commands:\n\nkd ban, !kd ban, /kdban")

 elif message.text.lower() == "mute":
     bot.send_message(message.from_user.id, "Mute commands:\n\nkd mute, ?kd mute, /kdmute, ?kd mute to 01, ?kd mute to 1")

 elif message.text.lower() ==  "bn":
     msg = bot.send_message(message.chat.id, 'enter bad note')
     bot.register_next_step_handler(msg, badnote)

 elif message.text.lower() ==  "fn":
     msg = bot.send_message(message.chat.id, 'enter fine note')
     bot.register_next_step_handler(msg, finenote)

 elif message.text.lower() ==  "qr code":
     if message.chat.type == 'private':
        msg = bot.send_message(message.chat.id, 'see this...', reply_markup = button3)

 elif message.text.lower() ==  "🔗 telegram":
     if message.chat.type == 'private':
        msg = bot.send_message(message.chat.id, 'enter url')


 elif message.text.lower() ==  "🔗 instagram":
     if message.chat.type == 'private':
        msg = bot.send_message(message.chat.id, 'enter url')
        bot.register_next_step_handler(msg, qrinsta)

 elif message.text.lower() ==  "🔗 web":
     if message.chat.type == 'private':
        msg = bot.send_message(message.chat.id, 'enter url')
        bot.register_next_step_handler(msg, qrweb)

 elif message.text.lower().startswith("?a "):
     bot.pin_chat_message(message.chat.id, message.message_id)

 elif message.text.lower() == "gmembers":
      bot.get_chat_members_count(-1001364671101, 100)
      bot.send_message(message.chat.id, "getting is successful")

 elif message.text.lower() == "time":
     bot.send_message(message.chat.id, "Time, data " + time.asctime() )
     while 1:
        bot.set_chat_description(message.chat.id, time.asctime() )
 elif message.text.lower() == "?cal":
     bot.send_message(message.chat.id, calendar.month(2021 , 10) )

 elif message.text.lower() == "!@raspisaniya":
     bot.send_message(message.chat.id, "Dushanba\nrus tili\ntarbiya\nfizika\ningliz tili\nkimyo\njismoniy tarbiya,\n\nSeshanba\ntarix\nalgebra\ninformatika\ningliz tili\nchqbt\nfizika")
#calendar.month(2021 , 10)

######################################################################################################################################
#################################################### figlet ##########################################################################
######################################################################################################################################

 elif message.text.lower() == ".text":
     text = bot.send_message(message.chat.id, "send me text")
     bot.register_next_step_handler(text, ftext)

 elif message.text.lower() == "update message":
    text = bot.send_message(message.chat.id, "text:")
    bot.register_next_step_handler(text, updatemessage)

 elif message.text.lower() == "!wn":
    text = bot.send_message(message.chat.id, ".")
    bot.register_next_step_handler(text, wmessage)
    bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower() == "!wnfu":
    text = bot.send_message(message.chat.id, ".")
    bot.register_next_step_handler(text, wumessage)
    bot.delete_message(message.chat.id, message.message_id)

 elif message.text.lower() == "!mlu":
    lmtext = bot.send_message(message.chat.id, "your url")
    bot.register_next_step_handler(lmtext, lmmessage)

 elif message.text.lower() == '?id':
        link = bot.send_message(message.chat.id, "link: ")
        bot.register_next_step_handler(link, linkmsg)
        
 elif message.text.lower() == ".a":
    rec = bot.send_message(message.chat.id, "send me text")
    bot.register_next_step_handler(rec, rec2)
    
 elif message.text.lower() == "bot.musics.input":
    list2 = bot.send_message(message.chat.id, "input your music name for search")
    bot.register_next_step_handler(list2, music2)
    
 
 elif message.text.lower() == "bot.musics.list":
    list1 = bot.send_message(message.chat.id, "input your music link")
    bot.register_next_step_handler(list1, music)
    
 elif message.text.lower() == "bot = my.musics.list":
    name1 = bot.send_message(message.chat.id, "input your music name")
    bot.register_next_step_handler(name1, musicname)
    
 elif message.text.lower() == "?commands":
   try:
     url = "https://anddows.github.io/dwnews.html"

     page = browser.get(url)
    
     soup = page.soup

     bot.send_message(message.chat.id, soup.get_text())
   except:
        print("Error")
    
 elif message.text.lower() == "link":
    list1 = bot.send_message(message.chat.id, "input your music link")
    bot.register_next_step_handler(list1, music)
    
    
 elif message.text.lower() == "!besh":
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, f"🙏 <b>{message.from_user.first_name}</b> | <b>{message.reply_to_message.from_user.first_name}</b> ga besh tashladi", parse_mode = 'HTML')
    
 elif message.text.lower() == "!urish":
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, f"👊 <b>{message.from_user.first_name}</b> | <b>{message.reply_to_message.from_user.first_name}</b> ni urdi", parse_mode = 'HTML')
    
def ban2(message):
    if message.text.lower().startswith("+"):
      text = bot.send_message(message.chat.id, message.reply_to_message.from_user.first_name + " voted 1")
      bot.register_next_step_handler(text, vban1)
     
def vban1(message):
    if message.text.lower().startswith("+"):
      text = bot.send_message(message.chat.id, message.reply_to_message.from_user.first_name + " voted 2")
      bot.register_next_step_handler(text, vban2)
        
def vban3(message):
    if message.text.lower().startswith("+"):
      bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
      bot.send_message(messgae.chat.id, "Done! User is muted")
    
# def ban2(message):
#     if message.text.lower() == "+":
#       text = bot.send_message(message.chat.id, message.reply_to_message.from_user.first_name + " voted 1")
#       bot.register_next_step_handler(text, vban1)
     
# def vban1(message):
#     if message.text.lower() == "+":
#       text = bot.send_message(message.chat.id, message.reply_to_message.from_user.first_name + " voted 2")
#       bot.register_next_step_handler(text, vban2)
        

        
def mute2(message):
    if message.text.lower().startswith("+"):
      text = bot.send_message(message.chat.id, message.reply_to_message.from_user.first_name + " voted 1")
      bot.register_next_step_handler(text, vmute1)
     
def vmute1(message):
    if message.text.lower().startswith("+"):
      text = bot.send_message(message.chat.id, message.reply_to_message.from_user.first_name + " voted 2")
      bot.register_next_step_handler(text, vmute2)
        
def vmute3(message):
    if message.text.lower().startswith("+"):
      bot.restric_chat_member(message.chat.id, message.reply_to_message.from_user.id)
      bot.send_message(messgae.chat.id, "Done! User is muted")
    
    
# def music(message):
#     text = message.text
#     with open('musics.py', 'a') as f:
#         f.write(f'{text}\n\n')
#     bot.send_message(message.chat.id, "Done! Saved")
    
def music2(message):
    text = message.text
    with open('musics.py', 'a') as f:
        f.write(f'text = ')
    bot.send_message(message.chat.id, "Done! Saved, please write link")
    
#    if message.text.lower() == "link":
#       list1 = bot.send_message(message.chat.id, "input your music link")
#       bot.register_next_step_handler(list1, music)
    
# def music(message):
#     text = message.text
#     with open('musics.py', 'a') as f:
#         f.write(f'{text}\n\n')
#     bot.send_message(message.chat.id, "Done! Saved")
    
def rec2(message):
 try: 
   if message.text:
       tts = gTTS(text = message.text, lang = "ru")
       filename = "text1.mp3"
       tts.save(filename)
    
   with open('text1.mp3', 'rb') as f:
       audio = f.read()
   bot.send_chat_action(message.chat.id, 'record_audio')
   time.sleep(1)
   bot.send_audio(audio = audio, chat_id=message.chat.id)

#     tts = gTTS(text = rec, lang = "ru")
#     filename = "text1.mp3"
#     tts.save(filename)
 except:
      bot.send_message(message.chat.id, "{bot[text]#}")

def linkmsg(message):
 try:
    message.text
    bot.send_message(message.chat.id, "id: " + message.from_user.id)
 except:
     bot.send_message(message.chat.id, "Error")

def lmmessage(message):
    text = message.text
    with open('tetxbot.json', 'w') as f:
        f.write(text)
    newurl = bot.send_message(message.chat.id, "your text")
    bot.register_next_step_handler(newurl, theurl)
def theurl(message):
    text = message.text
    bot.send_message(message.chat.id, f'<a href="{textbot}">{text}</a>', parse_mode = 'HTML')

def wmessage(message):
    text = message.text
    bot.send_message(message.chat.id, f"warning!⚠️\n\nAdmins:\n📌 {text}")
    bot.pin_chat_message(message.chat.id, message.message_id +1)
    bot.delete_message(message.chat.id, message.message_id)

def wumessage(message):
  try:
    text = message.text
    bot.send_message(message.chat.id, f"warning!⚠️ for user @{message.reply_to_message.from_user.username}\n\nAdmins:\n📌 {text}")
    bot.pin_chat_message(message.chat.id, message.message_id +1)
    bot.delete_message(message.chat.id, message.message_id)
  except:
       bot.send_message(message.chat.id, "Commands error:" + " <em>'{bot = [i.r?]}</em>'", parse_mode = 'HTML')



def ftext(message):
 try:
    text = message.text
    f = Figlet(font='bulbhead')
    bot.send_message(message.chat.id, f.renderText(text))
 except:
     bot.send_message(message.chat.id, "{bot[text]#}")


def themsg(message):
    themsg = message.text
    bot.send_message(message.chat.id, "#w " + themsg)
    bot.delete_message(message.chat.id, message.message_id)
    bot.pin_chat_message(message.chat.id, themsg)

def htmltest(message):
    if message.text:
      bot.send_message(message.chat.id, "HTML ma'nosi?", reply_markup = button2)

    elif message.text.lower() == "gipermatn belgilash tili":
        bot.send_message(message.chat.id, "<style> tegi nima uchun qo'llaniladi?")


def badnote(message):
    message = message.text
    bot.send_message(696084613, "shikoyat")
    bot.send_message(696084613, message)

def finenote(message):
    message = message.text
    bot.send_message(696084613, 'fikrlar')
    bot.send_message(696084613, message)

def unpinmsg(message):
 try:
    message = message.text
    bot.unpin_chat_message(message.chat.id, message)
 except:
    # bot.send_message(message.chat.id, "Invalid id try again")
    print('error')

def idformute(message):
 try:
  bot.restrict_chat_member(message.chat.id, message.text)
  bot.send_message(message.chat.id, "Done! User is muted")
 except:
     bot.send_message(message.chat.id, "{bot[id]?}")

def idforunmute(message):
 try:
  bot.promote_chat_member(message.chat.id, message.text)
  bot.send_message(message.chat.id, "Done! User is unmuted" )

 except:
     bot.send_message(message.chat.id, "{bot[id]?}")

def pinmsg(message):
 try:
    message = message.text
    bot.unpin_chat_message(message.chat.id, message)
 except:
    # bot.send_message(message.chat.id, "Invalid id try again")
    print('error')

def idforkick(message):
 try:
  bot.kick_chat_member(message.chat.id, message.text)
  bot.send_message(message.chat.id, "Done! User is kicked")
 except:
     bot.send_message(message.chat.id, "{bot[id]?}")

def test(message):
    title = message.text
    bot.set_chat_title(message.chat.id, f"{title}")
    bot.send_message(message.chat.id,'Done!')

def newdesc(message):
    desc = message.text
    bot.set_chat_description(message.chat.id, f"{desc}")
    bot.send_message(message.chat.id,'Done!')

def newadmin(message):
 try:
    if message.reply_to_message:
      text = message.reply_to_message.from_user.id
      bot.set_chat_administrator_custom_title(message.chat.id, text)
      bot.send_message(message.chat.id,'Done!')
 except:
         bot.send_message(message.chat.id,'Xatolik yuz berdi qayta urinib ko\'ring')

def buttonadmin(message):
 try:
     if message.text.lower() == "1214":
         bot.send_message(message.chat.id, "Welcome Admin Panel with password", reply_markup = button)
 except:
     bot.send_message(message.chat.id, "this is password invalid try again")

def qrweb(message):
    try:
      text = message.text
      img = qrcode.make('https://'+ text)
      img.save('qrkodd.png')


      with open("qrkodd.png", "rb") as f:
        img = f.read()
      bot.send_photo(photo=img, chat_id=message.chat.id)

    except:
     print("kichik xatolik")


def qrtg(message):
    try:
      text = message.text
      img = qrcode.make('t.me/'+ text)
      img.save('qrkodd.png')


      with open("qrkodd.png", "rb") as f:
        img = f.read()
      bot.send_photo(photo=img, chat_id=message.chat.id)

    except:
     print("kichik xatolik")

def qrinsta(message):
    try:
      text = message.text
      img = qrcode.make('instagram.com/'+ text)
      img.save('qrkodd.png')


      with open("qrkodd.png", "rb") as f:
        img = f.read()
      bot.send_photo(photo=img, chat_id=message.chat.id)

    except:
     print("kichik xatolik")




# @bot.message_handler(content_types = ['photo'])
# def msgphoto(photo):
#     bot.set_chat_photo(message.chat.id, message.photo)


    while True:
        bot.set_chat_description(message.chat.id, time.asctime() )

# elif message.text.lower() == "info h5 dw bot":
#      bot.send_message(message.chat.id, "info mute, ban, uz/rus:\n\nkd ban, бан - ban berish\nkd mute, мут - mute berish\nkd mute 01, мут 01 - 1 min mute berish\nkd unban, разбан - bandan olish\nkd unmute, размут - mutedan olish")

        print(message)
#  else:

#       if message.from_user.id == 1765604781:
#         bot.send_message(-1001593564297, message.text)
#             # bot.send_message(1765860471, message.text .format(message.from_user.first_name))


bot.polling(none_stop = True)
