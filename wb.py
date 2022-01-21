from bs4 import BeautifulSoup
import requests

page=requests.get("https://www.flipkart.com/search?q=apple+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=apple+mobiles%7CMobiles&requestId=2f285fa6-691f-4247-8c77-4085c16a15f4&as-backfill=on")
page.content

soup=BeautifulSoup(page.content,"html.parser")
mo=soup.find_all('div',class_="_13oc-S")
print(len(mo))

names=[]
ram=[]
price=[]
camera_spec=[]

for m in mo:
    name=m.find('div',class_='_4rR01T').text
    names.append(name)
    pric=m.find('div',class_='_30jeq3 _1_WHN1').text
    price.append(pric)
    ul=soup.find('ul',class_='_1xgFaf')
    cam=ul.find_all("li")[2].text
    camera_spec.append(cam)

import pandas as pd
dic= {"names":names, "price":price, "camera_specs":camera_spec}
df=pd.DataFrame(dic)

df.head()
