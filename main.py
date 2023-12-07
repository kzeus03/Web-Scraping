import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)
soap=BeautifulSoup(r.text,"lxml")
h_tag=(soap.find("h1",{"class":"page-header"}))
print("Heading : ",h_tag.string)
d_tag=(soap.find_all("a",class_="title"))
p_tag=(soap.find_all("h4",class_="float-end price card-title pull-right"))
device_list=[]
price_list=[]

for i in d_tag :
    name = i.text
    device_list.append(name)
for i in p_tag :
    price = i.text
    price_list.append(price)
"""
print("Devices---Cost")
for i in range(len(device_list)) :
    print(i+1 ," " ,device_list[i],"---",price_list[i])
"""
df = pd.DataFrame({"Product Name" : device_list , "Price" : price_list})
print(df)
df.to_csv("products list.csv")