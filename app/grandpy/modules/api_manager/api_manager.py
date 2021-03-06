# !/usr/bin/python3.8
# -*- coding: Utf-8 -*

"""
API_MANAGER MODULE

Utility :   Do requests api's and return datas (Google Maps, WikiMedia)
Project :   GrandPy Bot, le papy robot
"""

from config import GM_API_KEY
import requests
import json

""" GOOGLE MAPS API REQUEST MAP_DATA (PLACE, ADDRESS, COORDINATES) """
def get_map_info(place):

    api_begin = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input='
    api_para = '&inputtype=textquery'
    query_data = '&fields=formatted_address,geometry,name&key='
    language = '&language=fr'
    api_key = GM_API_KEY

    # BUILD URL FOR REQUEST
    url = f"{api_begin}{place}{api_para}{query_data}{api_key}{language}"

    # REQUEST
    place_data = requests.get(url).json()

    # ATTRIBUTE DATAS
    status = place_data["status"]
    if status == "OK":
        address = place_data["candidates"][0]["formatted_address"]
        coordinates = place_data["candidates"][0]["geometry"]["location"]
        place = place_data["candidates"][0]["name"]

        # BUILD DICT MAP_DATA
        place_data = {"status": status, "place": place, "address": address, "coordinates": coordinates}

    return place_data if status == "OK" else None

""" WIKIMEDIA API REQUEST TITLE_DATA (by g_m coordinates) """
def get_wiki_data(coordinates):
    
    lat = coordinates["lat"]
    lng = coordinates["lng"]

    # ATTRIBUTE DATAS FOR URL
    api_begin = "https://fr.wikipedia.org/w/api.php?action=query"
    api_mid = "&list=geosearch&format=json&formatversion=2"
    api_coord = f"&gscoord={lat}|{lng}"
    api_param = "&gsradius=100&gslimit=1"

    # BUILD URL FOR REQUEST
    url = f"{api_begin}{api_mid}{api_coord}{api_param}"

    # REQUEST
    geo_data = requests.get(url).json()

    # ATTRIBUTE RESPONSE
    wiki_data = geo_data["query"]["geosearch"]

    # IF RESPONSE IS EMPTY RETURN NONE
    if len(wiki_data) == 0: return None
    # ELSE
    title = wiki_data[0]["title"]
    return title

""" WIKIMEDIA API REQUEST ANECDOTE_DATA (by WikiMedia title) """
def get_text_data(title):

    api_begin = "https://fr.wikipedia.org/w/api.php?action=query"
    api_mid = "&format=json&prop=extracts"
    api_title = f"&titles={title}"
    api_param = "&formatversion=2&exsentences=3&explaintext=1&exsectionformat=plain"

    url = f"{api_begin}{api_mid}{api_title}{api_param}"
    
    extract_data = requests.get(url).json()

    anecdote = extract_data["query"]["pages"][0]

    if len(anecdote) <= 3: 
        return None
    else:
        return anecdote["extract"]
