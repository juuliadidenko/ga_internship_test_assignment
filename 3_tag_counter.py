import requests
from bs4 import BeautifulSoup
from typing import List

url = 'https://greenatom.ru/'
resp = requests.get(url).content
soup = BeautifulSoup(resp, 'html.parser')


def get_html_tag_count(soup) -> int:
    return len(soup.find_all())


def get_tags_with_attrs_count(soup) -> int:
    tags_with_attrs: List[str] = [
        tag for tag in soup.find_all() if len(tag.attrs)]
    return len(tags_with_attrs)
