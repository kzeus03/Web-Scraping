import pandas as pd
import requests
from bs4 import BeautifulSoup
url ="https://www.formula1.com/en/results.html/2023/drivers.html"
r=requests.get(url)
print(r)
soap = BeautifulSoup(r.text,"lxml")
table = soap.find("table",{"class":"resultsarchive-table"})
header=table.find_all("th")
titles=[]
for i in header :
    h=i.text
    titles.append(h)
df=pd.DataFrame(columns=titles)
print(df)
rows=table.find_all("tr")
for i in rows[1:] :
    data=i.find_all("td")
    row=[tr.text for tr in data]
    print(row)
    l=len(df)
    df.loc[l]=row
print(df)
df.to_csv("f1.csv")