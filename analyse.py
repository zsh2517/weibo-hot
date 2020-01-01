# 数据分析
import os
import time
import datetime
import math
from datetime import datetime
import json
import pygal
bgn="2020-01-01-07-00-00".split("-")
end="2020-01-01-10-30-00".split("-")
keys=[]
xy_chart = pygal.XY(show_dots=False)
keyword="新年"
xy_chart.title = "微博关键词 “%s” 热度分析"%(keyword)
chart={}
def add(tm,rank,key):
    # print(rank)
    if key not in keys:
        print("识别到关键词 %s"%(key))
        chart[key]=[]
        keys.append(key)
    if rank!=55:
        chart[key].append((tm,-rank))
    else:
        chart[key].append((tm,-60))
    if key in keys:
        return 0
    else:
        return 1
for index in range(len(bgn)):
    bgn[index]=int(bgn[index])
    end[index]=int(end[index])
def tonext(tme,level):
    tme[level]+=1
    if(tme[5]==60):
        tme[5]=0
        tme[4]+=1
    if(tme[4]==60):
        tme[4]=0
        tme[3]+=1
    if(tme[3]==24):
        tme[3]=0
        tme[2]+=1
    if(tme[2]==32):
        tme[2]=0
        tme[1]+=1
    if(tme[1]==13):
        tme[1]=1
        tme[0]+=1
def proc(x):
    if x<=9:
        return "0"+str(x)
    else:
        return str(x)
def main():
    cnt=list(bgn)
    path=""
    while True:
        print(cnt)
        while path=="%s/%s/%s/%s-%s-%s-%s.txt"%(str(cnt[0]),proc(cnt[1]),proc(cnt[2]),str(cnt[0]),proc(cnt[1]),proc(cnt[2]),proc(cnt[3])):
            # print(cnt)
            tonext(cnt,5)
        # print(cnt,end)
        path="%s/%s/%s/%s-%s-%s-%s.txt"%(str(cnt[0]),proc(cnt[1]),proc(cnt[2]),str(cnt[0]),proc(cnt[1]),proc(cnt[2]),proc(cnt[3]))
        dir=open(path,"r")
        lines=dir.readlines()
        tot=len(lines)
        index=0
        while index<tot:
            # print(cnt[3],cnt[4],cnt[5])
            if end<cnt:
                return
            # print(index)
            while True:
                js=json.loads(lines[index])
                tm=js["time"].split("-")
                for i in range(0,6):
                    tm[i]=int(tm[i])
                # print(tm,cnt)
                if tm>=cnt:
                    break
                index+=1
            if cnt==tm:
                # print(cnt[3],cnt[4],cnt[5])
                for rank in range(0,51):
                    if keyword in js[str(rank)]["text"]:
                        # print(js[str(rank)]["text"])
                        # add(int(tm[4])*100+int(tm[5]),rank,js[str(rank)]["text"])
                        add(int(tm[3])*60+int(tm[4])+int(tm[5])/60,rank,js[str(rank)]["text"])
                index+=1
                # print(index)
            tonext(cnt,5)
main()
for (key,value) in chart.items():
    xy_chart.add(key,value)
xy_chart.render_to_file("chart.svg")
