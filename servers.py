__author__ = 'Admin'
import requests, pickle
from bs4 import BeautifulSoup

html = requests.get('http://us.battle.net/wow/en/status').text
soup = BeautifulSoup(html)
rawRealms = soup.find_all('td',class_='name')
realms = [None]*len(rawRealms)
for i in range(0,len(realms)):
    realms[i] = rawRealms[i].text.encode('ascii','ignore').strip().lower().replace("'", "").replace(" ", "").replace("-", "")
print(realms)
output = open('realms', 'wb')
pickle.dump(realms,output)
output.close()