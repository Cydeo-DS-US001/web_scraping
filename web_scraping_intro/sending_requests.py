import requests
from bs4 import BeautifulSoup

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 15236.80.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.125 Safari/537.36'
}

response = requests.get('https://www.amazon.com/', headers= user_agent)

print(response)
print(response.status_code)
print(response.ok)

print('-----------------------------------------')

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.title)
print(soup)

