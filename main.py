import requests as req
from bs4 import BeautifulSoup

# url = input('Enter URL address: ')
url = 'https://books.toscrape.com/'

response = req.get(url)

if response.status_code == 200:
    html_content = response.text
    # print(html_content)
else:
    print(f'Error with downloading page. Status code: {response.status_code}')

soup = BeautifulSoup(html_content, 'html.parser')

for heading in soup.find_all('a'):
    print(heading.text.strip())
