from PythonProjects.api_test.reference import VKAuth as VKAuth1
from PythonProjects.api_test.vkey import VKey as vkey

email = vkey.email
pswd = vkey.pswd


vk = VKAuth1(['friends'], '7342834', '5.52', email=email, pswd=pswd)
vk.auth()

access_token = vk.get_token()
user_id = vk.get_user_id()



print(access_token)
# your code goes here