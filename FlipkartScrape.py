import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

PRODUCT=[]
PRICE=[]
SELLER=[]

def get_data(Furl):
  page = requests.get(Furl)
  soup = BeautifulSoup(page.content, 'html.parser')
  title = soup.find("div", class_="_2NKhZn").text
  PRODUCT.append(title)
  price = soup.find("div", class_="_30jeq3").text
  PRICE.append(price)
  seller = soup.find("div", class_="_1RLviY").text
  SELLER.append(seller)
  
file=open('C:\\webscrp\\Furl.txt','r')
links=file.readlines()
for link in links:
    get_data(link)
	
df=pd.DataFrame({'Product Name':PRODUCT, 'Price':PRICE, 'Seller':SELLER})
df.head(10)
df.to_excel('C:\\webscrp\\Flaptops.xlsx')

