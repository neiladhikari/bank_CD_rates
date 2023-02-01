import pandas as pd
import html5lib
import requests
import random
import openpyxl

url="https://www.depositaccounts.com/blog/cd-rates-survey/"

user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]

page = requests.get(url, headers={'User-Agent': random.choice(user_agents_list)})
pdtable = pd.read_html(page.text)
cdrates = pdtable[6]
cdrates.to_excel('cdrates.xlsx', index=False, header=False)