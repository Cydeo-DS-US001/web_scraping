import requests as r
from bs4 import BeautifulSoup as soup

url = 'https://cydeo.com/'

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 15236.80.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.125 Safari/537.36'
}

response = r.get(url, headers=user_agent)

print(response.ok)

s = soup(response.content, 'html.parser')

print(s.title)
# print(s)

print('--------------------------------------------------')

# element1 = s.find('a', class_='mega-menu-link')
element1 = s.find('a', href='https://cydeo.com/programs/')

print(element1.text)

"""
<a class="mega-menu-link" href="https://cydeo.com/programs/" tabindex="0">Programs</a>
"""

# element2 = s.find('h1', class_='elementor-heading-title elementor-size-default')

element2 = s.find('h1', string='Discover your potential')

print(element2)
print(element2.text)

"""
<h1 class="elementor-heading-title elementor-size-default">Discover your potential</h1>
"""

print('---------------------------------------------------')

elements = s.find_all('a', class_='mega-menu-link')

for x in elements:
    print(x.text)




