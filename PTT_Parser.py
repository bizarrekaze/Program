import urllib.request
import subprocess, sys
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

req = Request('https://www.ptt.cc/bbs/Gamesale/index.html', headers={'User-Agent': 'Mozilla/5.0'})
flag = False
oldlist = []
while True:
    response = urlopen(req).read()
    soup =  BeautifulSoup(response,"html.parser")
    container = soup.select('.r-ent')
    for each_item in container:
        if (str(each_item.select('div.author')[0].text)+str(each_item.select('div.title'))) not in oldlist:
            print ("\n=========================NEW Message======================")
            if flag:
                subprocess.call(['notify-send' , str(each_item.select('div.title')[0].text)])
            print ("date："+each_item.select('div.date')[0].text, "作者："+each_item.select('div.author')[0].text)
            print (each_item.select('div.title')[0].text)
            print ("---------------------------------")
        oldlist.append(str(each_item.select('div.author')[0].text)+str(each_item.select('div.title')))
    flag = True
    time.sleep(10)
