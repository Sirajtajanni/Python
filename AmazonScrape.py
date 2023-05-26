
import openpyxl
from bs4 import BeautifulSoup
import requests
import pandas as pd
import lxml

HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

PRODUCT=[]
PRICE=[]

def get_data(Aurl):
    r = requests.get(link, headers = HEADERS)
    soup = BeautifulSoup (r.content, "lxml")
    name = soup.find("span", id="productTitle", class_="a-size-large product-title-word-break").text
    PRODUCT.append(name)
    price = soup.find("span", class_="a-offscreen").text
    PRICE.append(price)
  
file=open('C:\\webscrp\\Aurl.txt','r')
links=file.readlines()
for link in links:
  #print (link)
  get_data(link)
    
	
df=pd.DataFrame({'Product name': PRODUCT, 'Price': PRICE})
df.head(10)
df.to_excel('C:\\webscrp\\Alaptops123.xlsx')
