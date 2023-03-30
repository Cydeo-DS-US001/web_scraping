import requests
from bs4 import BeautifulSoup

url = 'http://practice.cybertekschool.com/tables'

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 15236.80.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.125 Safari/537.36'
}

response = requests.get(url, headers=user_agent)

print(response.status_code)
print(response.ok)

soup = BeautifulSoup(response.content, 'html.parser')

print('-------------------------------------------------')

emails = soup.select('td:nth-child(3)')

for x in emails:
    print(x.text)

print('-------------------------------------------------')

websites = soup.select('td:nth-child(5)')

for x in websites:
    print(x.text)

print('------------------------------------------------------')

element1 = soup.select('h3+ p')[0]

print(element1.text.strip())





