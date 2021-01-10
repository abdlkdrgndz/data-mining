# Author: Abdulkadir Gündüz
# Creation Date: 2020-12-16

import requests
import json
from datetime import datetime
import time

def controlDomain():
    enterDomain = input("Alan adı girin: ")
    if enterDomain != "exit":
        url = "https://api.promptapi.com/whois/query?domain=" + enterDomain

        payload = {}
        headers= {
        "apikey": "NyAMk6cQRvS2MIuTLiavyJGPcFJfimaq"
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        response = response.text
        json_object = json.loads(response)
        print(
            "Kayıt Tarihi: " + json_object['result'].get('creation_date'), 
            "Expire : " + json_object['result'].get('expiration_date'), 
            " Registrar: " + json_object['result'].get('registrar'),
            sep=" -> ")
        return controlDomain()
    else:
        exit()

controlDomain()