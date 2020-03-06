import requests
import vk_api
import selenium
import getpass
from PythonProjects.api_test.vkey import VKey as vkey
from bs4 import BeautifulSoup

email = vkey.email
pswd = vkey.pswd


api_auth_url = 'https://oauth.vk.com/authorize'
app_id = 7342834    # ID приложения созданного в контакте
permissions = ('friends',)
redirect_uri = 'https://oauth.vk.com/blank.html'
display = 'wap'
api_version = "5.52"

# сборка запроса
auth_url_template = '{0}?client_id={1}&scope={2}&redirect_uri={3}&display={4}&v={5}&response_type=token'
auth_url = auth_url_template.format(api_auth_url, app_id, ','.join(permissions), redirect_uri, display, api_version)

# используя менеджер контента, можно убедиться, что ресурсы, применимые
# во время сессии будут свободны после использования
session = requests.Session()
response = session.get(auth_url)
print(auth_url)

payload = {'_origin': 'https://oauth.vk.com', 'ip_h': '13531cf4e9c85b7e88', 'lg_h': "lg_h", 'to': 'aHR0cHM6Ly9vYXV0aC52ay5jb20vYXV0aG9yaXplP2NsaWVudF9pZD03MzQyODM0JnJlZGlyZWN0X3VyaT1odHRwcyUzQSUyRiUyRm9hdXRoLnZrLmNvbSUyRmJsYW5rLmh0bWwmcmVzcG9uc2VfdHlwZT10b2tlbiZzY29wZT0yJnY9NS41MiZzdGF0ZT0mZGlzcGxheT13YXA-', 'email': '+79119563347', 'pass': 'Lansberg9210', 'submit_allow_access': True}
auth_url_parser = "https://login.vk.com/?act=login&soft=1&utf8=1"

response_post = session.post(auth_url_parser, data=payload)





file = open('response.html', 'w')
file.write(str(response_post.text))
print()
file.close()


# look for <form> element in response html and parse it

