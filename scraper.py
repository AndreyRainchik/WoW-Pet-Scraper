__author__ = 'Admin'
import requests,pickle,time,sys
from bs4 import BeautifulSoup

realms = ['blackhand','dalaran','thrall','velen','ysera','proudmoore','eldrethalas']
pkl_file = open('ids','rb')
items = pickle.load(pkl_file)
pkl_file.close()
pkl_file2 = open('realms','rb')
realms2 = pickle.load(pkl_file2)
pkl_file2.close()
site = 'http://www.wowuction.com/us/'
for item in items:
    low = sys.maxint
    lowRealm = ""
    high = 0
    highRealm = ""
    for realm in realms:
        time.sleep(1) #no more accidental DDoS
        s = site+realm+'/horde/Items/Stats/'+item
        html = requests.get(s).text
        soup = BeautifulSoup(html)
        price = float(soup.find('span',class_="cur_g").text+'.'+soup.find('span',class_="cur_s").text)
        if(price<low):
            low=price
            lowRealm = realm
        if(price>high):
            high=price
            highRealm = realm
    print "Item #:",item
    print "Lowest:",low," on",lowRealm
    print "Highest:",high," on",highRealm
    print ""
