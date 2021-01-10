import requests

input = input("Geçerli bir URL adresi girin: ")

if input == "exit":
    exit()
else:
    url = "https://api.promptapi.com/short_url/hash"

    payload = input.encode("utf-8")
    headers= {
        "apikey": "NyAMk6cQRvS2MIuTLiavyJGPcFJfimaq"
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    result = response.text
    print(result)