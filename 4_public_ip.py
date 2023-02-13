# Вариант 1. Необходима установка cURL
import os


def get_public_ip() -> str:
    ip_addr: str = os.popen('curl -s ifconfig.me').readline()
    return ip_addr


# Вариант 2 с использованием внешних сервисов
import requests

url = 'https://checkip.amazonaws.com'


def get_public_ip2(str: url) -> str:
    ip_addr: str = requests.get(url).text.strip()
    return ip_addr
