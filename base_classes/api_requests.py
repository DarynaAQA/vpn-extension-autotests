from base_classes.decrypt_payload import DecryptData
import requests
import json
from typing import Dict, Tuple


class ApiRequests:

    def __init__(self, url=None):
        self.url = url
        self.response = None

    def send_request(self):
        self.response = requests.get(self.url)
        return self.response

    def decrypt_response(self) -> Dict[str, str]:
        decrypt_method = DecryptData()
        try:
            data = self.response.text
            decrypted_message = decrypt_method.main(data)
            json_decrypted_message = json.loads(decrypted_message)
            return json_decrypted_message
        except json.JSONDecodeError:
            print("Error while decoding JSON")

    def parse_free_servers(self) -> Dict[str, Tuple[str, str, str]]:
        self.response = self.send_request()
        data = self.decrypt_response()
        us_servers_data = {}
        for i in range(0, len(data["data"])):
            us_servers_data[f"{i + 1}"] = data["data"][i]['id'], data["data"][i]['title'], data["data"][i]['load']
        return us_servers_data

    def get_current_city(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        get_ip = requests.get(f"https://gapi.vqols.cc/ip", headers=headers)
        get_ip_response = get_ip.json()
        current_city = get_ip_response["city"]
        return current_city
