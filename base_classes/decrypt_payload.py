import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import os
from dotenv import load_dotenv


class DecryptData:
    def decrypt_data(self, encrypted_value, iv, key):
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        padded_plaintext = cipher.decrypt(encrypted_value)
        plaintext = unpad(padded_plaintext, AES.block_size)
        return plaintext.decode('utf-8')

    def print_dict_values(self, data):
        if isinstance(data, str):
            data = json.loads(data)
        for key, value in data.items():
            if isinstance(value, dict):
                print(f"{key}:")
                DecryptData.print_dict_values(self, value)
            else:
                print(f"{key}: {value}")

    def main(self, payload):
        load_dotenv()
        key = base64.b64decode(os.getenv("KEY"))
        data = json.loads(payload)
        payload_value = data["payload"]
        encrypted_bytes = base64.b64decode(payload_value)

        data = json.loads(encrypted_bytes)

        iv_decoded = base64.b64decode(data['iv'])
        value_decoded = base64.b64decode(data['value'])

        decrypted_message = DecryptData.decrypt_data(self, value_decoded, iv_decoded, key)
        return decrypted_message
