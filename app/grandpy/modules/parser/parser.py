# !/usr/bin/python3.8
# -*- coding: Utf-8 -*

"""
PARSER MODULE

Utility :   To parse, clean, end return data to build response
Project :   GrandPy Bot, le papy robot
"""
import json


class Parser:

    """ SEQUENCE TO CLEAN SENTENCE """
    def clean_sentence(self, sentence):

        msg = sentence["msg"]
        # Set lower to analyse
        msg = msg.lower()
        # To detect and remove greetings
        greetings = self.detect_greeting(msg)
        # To remove special char
        filter_msg = self.remove_special_char(greetings["msg"])
        # To remove stopWord
        msg = self.remove_stopWords(filter_msg)
        # Build response
        response = {"msg": msg, "greetings": greetings["greeting"]}

        return response

    """ TO DETECT IF USER SAY A GREETING """
    def detect_greeting(self, message):

        greetings_list = ["salut", "bonjour", "bonjours",
                          "coucou", "hey", "ahoy"]
        # 0 : No greetings / 1 : Greeting detected
        greeting = 0

        for greet in greetings_list:
            if greet in message:
                message = message.replace(greet, "")
                greeting = 1

        return {"msg": message, "greeting": greeting}

    """ TO REMOVE SPECIAL CHAR """
    def remove_special_char(self, msg):

        for i in msg:
            if i in "['\"/\\:?!-}><(){,]":
                # To keep separate {it's -> it s etc..}
                if i in ",-'\"":
                    msg = msg.replace(i, " ")
                else:
                    msg = msg.replace(i, "")
        return msg

    """ TO GET A LIST OF STOP WORD (for removing)"""
    def get_stopWords(self):

        filepath = 'app/resources/stop_words.json'

        with open(filepath) as stop_words_file:
            stop_words_list = json.load(stop_words_file)

        return stop_words_list

    """ TO REMOVE STOP WORDS """
    def remove_stopWords(self, msg):

        sw_list = self.get_stopWords()
        msg_list = msg.split()
        for stopword in sw_list:
            for word in msg_list:
                if word == stopword:
                    msg_list.remove(stopword)

        return msg_list
