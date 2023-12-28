import requests
from bs4 import BeautifulSoup
import pandas as pd

UrlSite = "https://divar.ir/s/tehran/mobile-phones?q=iphone%2013"

site = requests.get(UrlSite)
soup = BeautifulSoup(site.text, 'html.parser')
div1 = soup.find('div', {'class' : 'browse-post-list-f3858'})
div2 = div1.find_all('div', {'class' : 'kt-post-card__body'})
# print(div2[0].find('h2').text)
titles = []
descriptions = []
prices = []

for item in range(len(div2)):
    title = div2[item].find('h2').text
    titles.append(title.replace('\n', ''.replace(',', ' ')))

    description = div2[item].find_all('div', {'kt-post-card__description'})[0].text
    descriptions.append(description.replace('\n', ''.replace(',', ' ')))

    price = div2[item].find_all('div', {'kt-post-card__description'})[1].text
    prices.append(int(price.replace('\n', '').replace(',', '').replace('تومان', '')))

# print(titles)
# print(descriptions)
# print(prices)

divarDictionary = {
    'Title': titles,
    'Description': descriptions,
    'Price': prices
}
df = pd.DataFrame(divarDictionary)
df.to_csv('divarMobileList.csv')

divarDataList = pd.read_csv('divarMobileList.csv')
print(divarDataList.to_string())
