# 热榜爬虫的主文件
import requests
from bs4 import BeautifulSoup
import requests
import json
import time
import os
import datetime
count=0
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
while True:
    cnt=int(round(time.time()*1000))
    fname=int(round(cnt/1000))
    if((fname-1)%60==0):
        print(datetime.datetime.now().strftime('\r%Y-%m-%d %H:%M:%S'))
    if((fname-1)%3!=0):
        time.sleep(0.3)
        continue
    # print(fname)
    print(datetime.datetime.now().strftime('\r%Y-%m-%d %H:%M:%S'),end="")

    path=datetime.datetime.now().strftime('%Y/%m/%d/%H/')
    fname=datetime.datetime.now().strftime('%M-%S')
    # print(fname)
    url="https://s.weibo.com/top/summary"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                             "(KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"}
    data = requests.get(url, headers=headers)
    soup=BeautifulSoup(data.text,"lxml")
    soup=soup.select("#pl_top_realtimehot > table > tbody")[0]
    # print(soup)
    res={}
    for i in range(1,52,1):
        rb={}
        soup2=soup.select("tr:nth-child("+str(i)+")")[0]
        rb["rank"]=str(i-1)
        rb["url"] = "https://s.weibo.com" + soup2.select("td.td-02 > a")[0]["href"]
        rb["text"] = soup2.select("td.td-02 > a")[0].text
        if i!=1:
            number= soup2.select("td.td-02 > span")[0].text
            rb["number"]=str(number)
        else:
            rb["number"]="None"
        # print(i)
        attr = soup.select("#pl_top_realtimehot > table > tbody > tr:nth-child("+str(i)+") > td.td-03 > i")
        if len(attr):
            rb["attr"] = attr[0].text
        else:
            rb["attr"]="None"
        res[str(i-1)]=dict(rb)
    # print(res)
    # print(cnt)
    os.makedirs(path,exist_ok=True)
    json.dump(res,open(path+fname+".txt","w",encoding="utf-8"),ensure_ascii=False)
exit(0)

