# !/usr/bin/python3.8
# -*- coding: Utf-8 -*

import pytest
import json

from app.grandpy.modules.api_manager import api_manager as api

def test_get_map_info_return_expected_datas(monkeypatch):

    class MockResponse:
        
        def json(*args, **kwargs):
            mock_url = "app/resources/mock_get_map_info.json"
            with open(mock_url, encoding='utf-8') as json_file:
                mock_resp = json.load(json_file)
            return mock_resp

    def mock_requests_url_answer(url):
        return MockResponse()

    monkeypatch.setattr('app.grandpy.modules.api_manager.api_manager.requests.get',
                         mock_requests_url_answer)
    map_data = api.get_map_info("mock")

    assert map_data["status"] == "OK"
    assert map_data["place"] == "Musée du Moteur"
    assert map_data["address"] == "18 Rue Alphonse Caillaud, 49400 Saumur, France"
    assert (map_data["coordinates"]["lat"] == 47.2505692 and
            map_data["coordinates"]["lng"] == -0.0876313)

def test_API_map_info_return_none():

    mock_place = "mauvais choix"
    map_data = api.get_map_info(mock_place)
    assert map_data == None

def test_API_get_wiki_data_return_title(monkeypatch):
    class MockReponse:
        def json(*args, **kwargs):
            mock_url = "app/resources/mock_get_wiki_data.json"
            with open(mock_url, encoding='utf-8') as json_file:
                mock_resp = json.load(json_file)
            return mock_resp

    def mock_requests_url_answer(url):
        return MockReponse()

    monkeypatch.setattr('app.grandpy.modules.api_manager.api_manager.requests.get',
                         mock_requests_url_answer)
    # The Eiffel Tower !!
    mock_coordinates = {'lat': 48.85837009999999, 'lng': 2.2944813} 
    title = api.get_wiki_data(mock_coordinates)

    assert title == "Tour Eiffel"

def test_API_get_wiki_data_return_none():

    mock_coordinates = {'lat': 48.85837009999999, 'lng': 1}
    results = api.get_wiki_data(mock_coordinates)
    assert results == None

def test_API_get_text_data_return_anecdote(monkeypatch):

    class MockReponse:
        def json(*args, **kwargs):
            mock_url = "app/resources/mock_get_text_data.json"
            with open(mock_url, encoding='utf-8') as json_file:
                mock_resp = json.load(json_file)
            return mock_resp
    def mock_requests_url_answer(url):
        return MockReponse()
    
    monkeypatch.setattr('app.grandpy.modules.api_manager.api_manager.requests.get',
                         mock_requests_url_answer)

    results = api.get_text_data("title")

    assert len(results) > 10

def test_API_get_text_data_return_none():

    mock_title = "Mauvais titre"
    results = api.get_text_data(mock_title)
    assert results == None