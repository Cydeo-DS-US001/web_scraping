import requests
from bs4 import BeautifulSoup

url = 'https://www.shopify.com/'

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 15236.80.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.125 Safari/537.36'
}

response = requests.get(url, headers=user_agent)

print(response.status_code)
print(response.ok)

soup = BeautifulSoup(response.content, 'html.parser')

# print(soup)

element1= soup.find('h1', string='The global commerce platform')

print(element1.text)

"""
<h1 class="font-bold text-5xl sm:text-6xl md:text-7xl lg:text-8xl richtext">The global commerce platform</h1>
"""

element2 = soup.find('a', attrs={'data-component-name': 'login' } )
#element2 = soup.find('a', href = '/login')

print(element2.text)


"""
<a class="whitespace-nowrap hover:underline text-black" href="/login" data-component-name="login">Log in</a>
"""

print('-------------------------------------')

links = soup.find_all('a')

for x in links:
    print(x.text)


print('-------------------------------------')


buttons = soup.find_all('button')
result = []
for x in buttons:
    if len(x.text) > 0:
        print(x.text)
        result.append(x)








