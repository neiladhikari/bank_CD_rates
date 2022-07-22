#A web scraper to pull current top CD rates for various terms/ periods and the respective banks, as published on bankrate.com.
from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import io

page = requests.get("https://www.bankrate.com/banking/cds/current-cd-interest-rates/")
soup = BeautifulSoup(page.content, 'html.parser')
article_content = soup.find('div', class_='article__content')

for header in article_content.find_all(['h3']):
    print(header.get_text())
    for elem in header.next_siblings:
        if elem.name and elem.name.startswith('h3'):
            break
        if elem.name == 'ul':
            print(elem.get_text())
