import requests
from bs4 import BeautifulSoup

# replace example url with your own.
url = ('https://www.example.com')
page = requests.get(url)

page
response = [200]

page.status_code
200

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())
