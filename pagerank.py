import urllib.request
import sys
import re
import xmltodict
import json
import time
import concurrent.futures
from datetime import date


def getrank(url):
    api = 'http://data.alexa.com/data?cli=10&dat=s&url='+url
    xml = urllib.request.urlopen(api).read()
    result = xmltodict.parse(xml)
    data = json.dumps(result).replace("@", "")
    data_tojson = json.loads(data)

    try:
        rank = data_tojson["ALEXA"]["SD"][1]["POPULARITY"]["TEXT"]
    except:
        rank = '0'
    try:
        country = data_tojson["ALEXA"]["SD"][1]["COUNTRY"]["NAME"]
        countryrank = data_tojson["ALEXA"]["SD"][1]["COUNTRY"]["RANK"]
    except:
        country = 'Country'
        countryrank = '0'

    data_world = {"World": rank}
    data_country = {country: countryrank}

    print(url, data_world, data_country)


if __name__ == "__main__":
    start_time = time.time()

    try:
        urls = ['google.com', 'youtube.com', 'facebook.com']
        for url in urls:
            getrank(url)

    except Exception as e:
        pass
    print("--- %s seconds ---" % round(time.time() - start_time, 2))
