import requests
from pprint import pprint

username = "YestayZ"
url = f"https://api.github.com/users/YestayZ"


user_data = requests.get(url).json()
pprint(user_data)


print('-------------------      ')

import base64
from github import Github
from pprint import pprint
# Github username
#username = "YestayZ"
# pygithub object
g = Github()
# get that user by username
user = g.get_user(username)
for repo in user.get_repos():
    print(repo)