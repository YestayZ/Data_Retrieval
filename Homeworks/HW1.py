import requests
from pprint import pprint

username = "YestayZ"
url = f"https://api.github.com/users/YestayZ"


user_data = requests.get(url).json()
pprint(user_data)


print('-------------------      ')


from github import Github
g = Github()
user = g.get_user(username)
for repo in user.get_repos():
    print(repo)