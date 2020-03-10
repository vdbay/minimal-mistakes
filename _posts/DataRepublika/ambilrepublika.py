import requests
import json
import os
import datetime
from bs4 import BeautifulSoup
my_dict = {}
page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text, 'html.parser');
all = []
for headline in obj.find_all('div',class_='teaser_conten1'):
    w = json.dumps(headline.find('h2').a.get('href'))
    x = json.dumps(headline.find('h1').text)
    y = json.dumps(headline.find('h2').text)
    z = json.dumps(headline.find('div', class_='date').text)
    currentDT=datetime.datetime.now()
    my_dict['Kategori']=x
    my_dict['Judul']=y
    my_dict['Waktu Publish']=z    
    my_dict['Link Berita']=w
    a=str(currentDT.hour)+":"+str(currentDT.minute)+":"+str(currentDT.second)+" "+str(currentDT.day)+"/"+str(currentDT.month)+"/"+str(currentDT.year)
    my_dict['Waktu Diambil']=a
    all.append( dict(my_dict))    
    print(my_dict)

dict_web = {"Berita":all}
with open('headlinebyazhar.json', 'w') as file:
    json.dump(dict_web, file, indent=4)
