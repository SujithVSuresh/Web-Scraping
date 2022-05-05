


import requests
from bs4 import BeautifulSoup

url = 'https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/'
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')
#result = soup.find(class_='row')
product_element = soup.find_all("div", class_="thumbnail")

for element in product_element:
    price = element.find("h4", class_="price")
    title = element.find("a", class_="title")
    link = title['href']

    print(title.text)
    print(price.text)
    print(f'https://codedamn-classrooms.github.io{link}')

#Output
#Asus AsusPro Adv...
#$1139.54
#https://codedamn-classrooms.github.ioNone

#Asus ROG Strix G...
#$1101.83
#https://codedamn-classrooms.github.ioNone

#Acer Aspire 3 A3...
#$494.71
#https://codedamn-classrooms.github.ioNone
