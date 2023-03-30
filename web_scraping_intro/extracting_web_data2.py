import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/?ref_=nv_mp_mv250'

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 15236.80.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.125 Safari/537.36'
}

response = requests.get(url, headers=user_agent)

print(response.status_code)
print(response.ok)

soup = BeautifulSoup(response.content, 'html.parser')

print('---------------------------')

elements = soup.select('.titleColumn')

for x in elements:
    print( " ".join( x.text.strip().split() ))

print('---------------------------')

element1 = soup.select('#main .header')[0]

print(element1.text)


print('----------------------------------')

result = soup.select('#nav-link-categories-mov+ .navlinkcat__targetWrapper .ipc-list-item__text')

for x in result:
    print(x.text)



