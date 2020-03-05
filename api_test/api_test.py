import requests
import vk_api
import selenium
import getpass
from PythonProjects.api_test.vkey import VKey as vkey

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

print(auth_url)
# используя менеджер контента, можно убедиться, что ресурсы, применимые
# во время сессии будут свободны после использования
session = requests.Session()
response = session.get(auth_url)


find_url = "https://login.vk.com/?act=login&soft=1&utf8=1"
response_post = requests.post(find_url, data={'email': email, 'pass': pswd})
print(response_post)




file = open('response.html', 'w')
file.write(str(response_post.text))
file.close()


# look for <form> element in response html and parse it

