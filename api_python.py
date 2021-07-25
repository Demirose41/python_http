# import requests
# url = "https://icanhazdadjoke.com/"

# response = requests.get(url, headers={"Accept": "application/json"})
# data = response.json()
# print(response.text)
# print(data['joke'])

import requests
from random import choice
user_input = input("enter search term\n")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term": user_input, 'limit': 1}
    ).json()


results = res['results']
total_jokes = res['total_jokes']

if total_jokes > 1:
    print(f"I found {total_jokes} jokes about {user_input}. Here is one:")
    print(choice(results)["joke"])
elif total_jokes == 1 :
    print(f"there is A jokes about {user_input}\n")
    print(choice(results)["joke"])
else:
    print(f"Sorry, couldn't find a joke with the term {user_input}")



