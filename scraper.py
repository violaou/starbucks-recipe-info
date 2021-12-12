# from bs4 import BeautifulSoup
import requests


r = requests.get('https://www.starbucks.ca/menu/drinks/hot-coffees')
print(r)