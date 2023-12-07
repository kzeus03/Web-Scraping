import requests
from bs4 import BeautifulSoup

url ="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)
soap=BeautifulSoup(r.text,"lxml")
container=soap.find_all("div",class_="col-md-4 col-xl-4 col-lg-4")
for i in range(len(container)) :
    box=soap.find_all("div",class_="col-md-4 col-xl-4 col-lg-4")[i]
    name = box.find("a").text
    print(i+1,")",name)