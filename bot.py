# -*- coding: UTF-8 -*-
import config
import telebot
import telebot.types as types
import commands

import time
import random
import cherrypy

bot = telebot.TeleBot(config.TOKEN)

cherrypy.config.update({
    'server.socket_host': config.WEBHOOK_LISTEN,
    'server.socket_port': config.WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': config.WEBHOOK_SSL_CERT,
    'server.ssl_private_key': config.WEBHOOK_SSL_PRIV
})


# @bot.message_handler(func=commands.is_admin, commands=['addadmins'])
# def addadmins(message):
#     last_message = 'addadmins'
#     bot.send_message(message.chat.id, f'')


@bot.message_handler(func=commands.not_command)
def send_admin(message):
    bot.send_message(message.from_user.id, """Друг мой, я не общаюсь. Лучше надень маску и скинь мне фоточку)
Спасибо, ты солнышко ❤️""")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # print('something')
    bot.reply_to(message, config.INFO_TEXT)
    chat_id = message.from_user.id

    with open('commons/mask_right.jpg', 'rb') as right:
        bot.send_photo(chat_id, right)
        bot.send_message(chat_id, 'Вот так маску надевать правильно')
        time.sleep(0.5)

    with open('commons/mask_wrong.jpg', 'rb') as wrong:
        bot.send_photo(chat_id, wrong)
        bot.send_message(chat_id, 'Вот так неправильно')
        time.sleep(0.5)

    with open('commons/without_mask.jpg', 'rb') as without_mask:
        bot.send_photo(chat_id, without_mask)
        bot.send_message(chat_id, 'Но ещё хуже ходить без маски')
        time.sleep(1)

    bot.send_message(message.from_user.id, 'А теперь пришли мне своё фото.')


@bot.message_handler(content_types=['photo'])
def check_face_mask(message):
    None
    # Здесь будет код для проверки фотографий на наличие маски
    has_mask = True
    chat_id = message.from_user.id
    bot.send_message(chat_id,
                     """Я пока ещё не умею ничего распознавать, так что будем считать, что ты в маске, ок?""")

    with open('commons/love.webp', 'rb') as sti:
        bot.send_sticker(chat_id, sti)
        sti.close()


"""
def botwork():
    try:
        print('BOT STARTED HIS WORK!')
        print(bot.get_webhook_info())
        bot.remove_webhook()
        bot.polling(none_stop=True)
    except Exception as ex:
        bot.send_message(649697634, f'Bot disabled his work with {ex}. Reboot....')
        print(f'Bot disabled his work with {ex}. Reboot....')
        time.sleep(10)
        bot.stop_bot()
        bot.stop_polling()
        botwork()
"""


def botwork():
    try:
        bot.infinity_polling(interval=0, timeout=20)
        # bot.remove_webhook()
        # bot.set_webhook(url=config.WEBHOOK_URL_BASE + config.WEBHOOK_URL_PATH, certificate=open(config.WEBHOOK_SSL_CERT, 'r'))
        # cherrypy.quickstart(config.WebhookServer(), config.WEBHOOK_URL_PATH, {'/': {}})
        # print('BOT STARTED HIS WORK!')
        # print(bot.get_webhook_info())
    except Exception as ex:
        # bot.send_message(649697634, f'Bot disabled his work with {ex}. Reboot....')
        # time.sleep(10)
        botwork()


if __name__ == '__main__':
    botwork()

