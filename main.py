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

book_HTML_elements = soup.find_all('a', href=True, title=True)
book_price_elements = soup.find_all('p', class_='price_color')


book_names = [name['title'] for name in book_HTML_elements]
book_prices = [price.text for price in book_price_elements]

for name, price in zip(book_names, book_prices):
    print(f'Book: {name}, price: {price[1:]}')
