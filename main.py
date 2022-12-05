from webserver import keep_alive
import json
import random
import re
import os
import telebot
from telebot import types
#from telegram.ext import Updater
# Токен и другое
bot = telebot.TeleBot(os.environ['TOKEN'], parse_mode="HTML")

# Список команд
cmds = ["https://telegra.ph/Komandy-i-Ispolzovaniya-06-21-2"]

vating = [
    "<b>Подать репорт на администратора</b>",
    "Перед нажатием принять прочитайте инструкцию и информацию что будет если.. ",
]

# Команда start


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, f'Твой ID: <code>{message.from_user.id}</code>')


'''
@bot.message_handler(commands=['buy_script'])
def buy_script(message):
    bot.reply_to(message, '(используя эту команду Автор не нисёт ответственность) Чтобы заказать скрипт надо перейти к боту @zroblox_bot и написать /buy_script' 
                )
'''

isd = [621479866, 1103023320]
UserID = 'none'
UserMessage = 'none'


@bot.message_handler(commands=['reportadm'])
def reportadm(message):
    if ' ' in message.text:
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("информация", url='https://telegra.ph/Komandy-I-ispolzovaniya-06-21'), types.InlineKeyboardButton('Принимаю', callback_data="accept"))
        global UserMessage
        UserMessage = message.id
        global UserID
        UserID = message.from_user.id
        bot.send_message(message.chat.id, '\n'.join([str(v) for v in vating]),  reply_markup=markup)
    else:
        bot.send_message(message.chat.id, '\n'.join([str(v) for v in vating]))


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "accept" and call.from_user.id == UserID:
        bot.edit_message_text(f'Репорт был успешно отправлен.', call.message.chat.id, call.message.message_id)
        for id in isd:
            bot.send_message(id, f'<b>REPORT</b>\nПоступил репорт от @{call.from_user.username} (<code>{call.from_user.id}</code>)')
            bot.forward_message(id, call.message.chat.id, UserMessage)


'''
'''

'''
@bot.message_handler(commands=['reportadm'])
def reportadm(message):
    if ' ' in message.text:
        bot.reply_to(message, f'Репорт был успешно отправлен.')
        bot.send_message(message.chat.id,  f'/warn @{message.from_user.username}')
        for id in isd:
            bot.send_message(id, f'<b>REPORT</b>\nПоступил репорт от @{message.from_user.username} (<code>{message.from_user.id}</code>)'
            )
            bot.forward_message(id, message.chat.id, message.id)
    else:
        bot.send_message(message.chat.id, vating[3])

'''
'''
# Команда report

ids = [
    1103023320, 621479866, 1412417616, 1111802131, 1746061464, 5153692125,
    1737841445
]
'''


@bot.message_handler(commands=['report'])
def report(message):
    if ' ' in message.text:
        bot.reply_to(
            message,
            f'Репорт был успешно отправлен <b>{len(ids)}</b> модераторам.')
        for id in ids:
            bot.send_message(
                id,
                f'<b>REPORT</b>\nПоступил репорт от @{message.from_user.username} (<code>{message.from_user.id}</code>)'
            )
            bot.forward_message(id, message.chat.id, message.id)
    else:
        bot.send_message(message.chat.id, cmds[3])


# Команда help
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, '\n'.join([str(cmd) for cmd in cmds]))


# Команда nick
nicks = [
    'de', 'fa', 'o', 'si', 'g', 'sha', 'mo', 'me', 'zo', 'er', 'ga', 'ni',
    'fri', 'fro', 'ty', 'ka', 'zee', 'ru', 'up', 'sa', 'pu', 'nu', 'za'
]


@bot.message_handler(commands=['nick'])
def nick(message):
    bot.reply_to(message,
                 ''.join(random.choices(nicks, k=random.randrange(2, 5))))


# Команда crt
moderators = [
    "<b>СОЗДАТЕЛИ БОТА:</b>", "@Link_ny - Создатель",
    "@TOOM_TYM - Редактор #1", "@Zgoly_yt - Редактор #2",
    "@SONG1000_7 - на чиле)", ""
]


@bot.message_handler(commands=['crt'])
def crt(message):
    bot.reply_to(message,
                 '\n'.join([str(moderator) for moderator in moderators]))


# Команда dick
@bot.message_handler(commands=['dick'])
def dick(message):
    random_number = random.randint(1, 10)
    bot.reply_to(
        message,
'print(message.reply_to_message.from_user.id)',print(message.reply_to_message.from_user.id)
    )
    


# Отправка сообщений от имени бота
ChatId = '@ArceusX_chat'
'''
@bot.message_handler(commands=['send'])
def send(message):
    if message.from_user.id in ids:
        text = re.sub(r"^\S+ *", r"", message.text)
        bot.send_message(ChatId, f'{text}')
'''

def get_args(message):
    args = re.split("\s+", message)[1:]
    if not args:
        return False
    else:
        return args


# Check for admin
def is_admin(id):
    with open('admins.json', "r") as jsonFile:
        data = json.load(jsonFile)
        if id in data:
            return True
        return False
    return False


@bot.message_handler(commands=['add_adm'])
def add_adm(message):
    # Check if user is admin
    if is_admin(int(message.from_user.id)):
        args = get_args(message.text)
        # Check for args
        if args and args[0].isdigit():
            id = int(args[0])
            with open('admins.json', "r") as jsonFile:
                data = json.load(jsonFile)
            if id not in data:
                data.append(id)
                with open("admins.json", "w") as jsonFile:
                    json.dump(data, jsonFile)

                bot.reply_to(message, f"`{id}` назначен админом.")
            else:
                bot.reply_to(message,
                             'Этот пользователь уже назначен админом.')
        else:
            bot.reply_to(message, 'Пользователь не найден.')
    else:
        bot.reply_to(message, 'Вы не можете использовать данную команду.')


# Запуск бота
print(f"{bot.user.username} запущен!")
keep_alive()
bot.polling(none_stop=True, interval=0)
