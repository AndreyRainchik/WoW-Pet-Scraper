__author__ = 'Admin'
import requests,pickle
from bs4 import BeautifulSoup
html = requests.get('http://petsear.ch/Items').text
soup = BeautifulSoup(html)
rawIds = soup.find_all('th',style="width:40px;")
ids = [None]*(len(rawIds)/2)
for i in range(0,len(ids)):
    ids[i] = str(rawIds[2*i].text.encode('ascii','ignore'))

print(ids)
output = open('ids', 'wb')
pickle.dump(ids,output)
output.close()