# !/usr/bin/python3.8
# -*- coding: Utf-8 -*

import pytest
import json

from app.grandpy.papybot import GrandPy

gp = GrandPy()

def test_fct_get_datas_return_expected_datas():


    mock_sentence = 'Musée du moteur'
    mock_response = gp.get_datas(mock_sentence)

    assert type(mock_response[0]) == dict
    assert type(mock_response[1]) == str
    assert mock_response[0]["place"] == "Musée du Moteur"
    assert mock_response[0]["address"] == "18 Rue Alphonse Caillaud, 49400 Saumur, France"
    assert mock_response[0]["coordinates"]["lat"] == 47.2505692
    assert mock_response[0]["coordinates"]["lng"] == -0.0876313
    assert "Le Musée du moteur est un musée français" in mock_response[1]

def test_fct_get_datas_return_error_msg():

    mock_sentence = 'fhxjfjcyjsjsftjfykfk'
    mock_response = gp.get_datas(mock_sentence)

    assert mock_response[0] == None
    assert mock_response[1] == "Désolé 🤷‍♂️ Mais je n'ai pas compris votre question ! 😇"

def test_fct_get_response_return_json_str():

    mock_sentence = {"msg": "Musée du moteur"}
    mock_response = gp.get_response(mock_sentence)
    
    #JSON DUMP
    assert type(mock_response) == str