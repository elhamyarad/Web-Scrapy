import requests
from bs4 import BeautifulSoup
import pandas as pd

# UrlSite = "https://liliom.ir/brand/dior-%d8%af%db%8c%d9%88%d8%b1/?jsf=epro-archive-products&pagenum=1"
# site = requests.get(UrlSite)
# soup = BeautifulSoup(site.text, 'html.parser')
# pages = soup.find_all('div', {'class': 'jet-filters-pagination__item'})
# print(len(pages))

n = 10
m = 1
titles = []
PriceAfterDiscount = []

for page in range(m, n + 1):
    UrlSite = "https://liliom.ir/brand/dior-%d8%af%db%8c%d9%88%d8%b1/?jsf=epro-archive-products&pagenum=" + str(m)
    m += 1
    site = requests.get(UrlSite)
    soup = BeautifulSoup(site.text, 'html.parser')

    pages = soup.find_all('div', {'class': 'jet-filters-pagination__item'})

    div1 = soup.find('div', {'data-source': 'main_loop'})
    div2 = div1.find_all('div', {'class': 'product-grid-item'})

    for item in range(len(div2)):
        title = div2[item].find('h3').text
        titles.append(title.replace('\n', '').replace(',', ' '))

        if div2[item].find('ins'):
            priceAfter = div2[item].find('ins').text
            PriceAfterDiscount.append(int(priceAfter.replace('\n', '').replace(',', '').replace('تومان', '')))
        else:
            priceAfter = 'موجود نیست'
            PriceAfterDiscount.append(priceAfter)

liliomDictionary = {
    'Title': titles,
    'Price': PriceAfterDiscount
}

df = pd.DataFrame(liliomDictionary)
df.to_csv('liliomList.csv')

liliomDataList = pd.read_csv('liliomList.csv')
print(liliomDataList.to_string())








# UrlSite = "https://liliom.ir/brand/dior-%d8%af%db%8c%d9%88%d8%b1/?jsf=epro-archive-products&pagenum=6"
# site = requests.get(UrlSite)
# soup = BeautifulSoup(site.text, 'html.parser')
# div1 = soup.find('div', {'data-source': 'main_loop'})
# div2 = div1.find_all('div', {'class': 'product-grid-item'})
#
# titles = []
# # PriceBeforeDiscount = []
# PriceAfterDiscount = []
#
# for item in range(len(div2)):
#     title = div2[item].find('h3').text
#     titles.append(title.replace('\n', '').replace(',', ' '))
#
#     if div2[item].find('ins'):
#         priceAfter = div2[item].find('ins').text
#         PriceAfterDiscount.append(int(priceAfter.replace('\n', '').replace(',', '').replace('تومان', '')))
#     else:
#         priceAfter = 'موجود نیست'
#         PriceAfterDiscount.append(priceAfter)
#
# liliomDictionary = {
#     'Title': titles,
#     'Price': PriceAfterDiscount
# }
#
# df = pd.DataFrame(liliomDictionary)
# df.to_csv('liliomList.csv')
#
# liliomDataList = pd.read_csv('liliomList.csv')
# print(liliomDataList.to_string())
