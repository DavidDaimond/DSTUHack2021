# -*- coding: UTF-8 -*-

import telebot
import telebot.types as types
import csv
import config
import string


not_command = lambda message: message.text[0] != '/'


def msg_to_list(message):
    return message.text.lower().translate(str.maketrans('','',string.punctuation)).split(' ')

