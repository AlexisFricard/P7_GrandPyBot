# !/usr/bin/python3.8
# -*- coding: Utf-8 -*
import json
from app.grandpy.modules.parser.parser import Parser

parse = Parser()


def test_if_parser_detect_greetings():

    mock_sentance = 'bonjour'
    tester = parse.detect_greeting(mock_sentance)

    assert tester["msg"] == ""
    assert tester["greeting"] == 1


def test_if_special_char_are_removed():

    mock_message = 'je voudrais l\'adre[]sse de la tour eiffel:)'
    msg = parse.remove_special_char(mock_message)

    assert msg == "je voudrais l adresse de la tour eiffel"


def test_if_loading_stopword_resource_are_list_and_valide_lenth(monkeypatch):

    sw_list = parse.get_stopWords()
    assert len(sw_list) >= 600 and type(sw_list) == list


def test_if_stopWords_was_removed_then_cleaning_sentence(monkeypatch):

    def mock_get_stopWords(self):
        filepath = 'app/resources/stop_words.json'
        with open(filepath) as stop_words_file:
            stop_words_list = json.load(stop_words_file)
        return stop_words_list

    def mock_remove_special_char(self, mock_sentence):

        msg = mock_sentence["msg"]
        msg = msg.lower()
        for i in msg:
            if i in "['\"/\\:}<>(){,]":
                if i in ",'\"":
                    msg = msg.replace(i, " ")
                else:
                    msg = msg.replace(i, "")
        return msg

    monkeypatch.setattr(
        'app.grandpy.modules.parser.parser.Parser.get_stopWords',
        mock_get_stopWords
    )
    monkeypatch.setattr(
        'app.grandpy.modules.parser.parser.Parser.remove_special_char',
        mock_remove_special_char
    )

    mock_sentence = {"msg": "Je voudrais l'adre[]sse de la tour eiffel:)"}
    mock_msg = parse.remove_special_char(mock_sentence)
    message = parse.remove_stopWords(mock_msg)

    assert message == ['tour', 'eiffel']
