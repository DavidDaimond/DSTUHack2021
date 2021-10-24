# -*- coding: UTF-8 -*-
# COMMANDS FOR BOT
import config
import string


not_command = lambda message: message.text[0] != '/'


def msg_to_list(message):
    return message.text.lower().translate(str.maketrans('','',string.punctuation)).split(' ')

