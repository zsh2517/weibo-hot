# 数据合并，打包到根目录（按照天）
import json
import os
import os.path
def proc(x):
    if x<=9:
        return "0"+str(x)
    else:
        return str(x)
date="2020-01-01-"
for h in range(0,24):
    count=0
    # f=open(date.replace("-","/")+proc(h)+".txt","w",encoding="utf-8")
    print(date.replace("-","/")+date+proc(h)+".txt",end=" ")
    f=open(date.replace("-","/")+date+proc(h)+".txt","w")
    # print(h)
    hh=proc(h)
    for m in range(0,61):
        mm=proc(m)
        for s in range(0,61):
            ss=proc(s)
            # print(hh+"/"+mm+"-"+ss+".txt")
            # print(date.replace("-","/")+hh+"/"+mm+"-"+ss+".txt")
            if os.path.exists(date.replace("-","/")+hh+"/"+mm+"-"+ss+".txt"):
                count+=1
                j=json.load(open(date.replace("-","/")+hh+"/"+mm+"-"+ss+".txt","r",encoding="utf-8"))
                j["time"]=date+hh+"-"+mm+"-"+ss
                f.write(json.dumps(j,ensure_ascii=False)+"\n")
    print("Number of file: %4d"% (count))

cnt=date.split("-")
for index in range(0,3):
    cnt[index]=int(cnt[index])
path="%s/%s/%s/"%(str(cnt[0]),proc(cnt[1]),proc(cnt[2]))
name="%s-%s-%s"%(str(cnt[0]),proc(cnt[1]),proc(cnt[2]))
print("mkdir "+ path + name)
os.system("mkdir "+ path + name)
print("cp %s*.txt %s%s"%(path,path,name))
os.system("cp %s*.txt %s%s/"%(path,path,name))
print("zip %s%s.zip %s%s/ -q -r" % (path,name,path,name))
os.system("zip %s%s.zip %s%s/ -q -r" % (path,name,path,name))
print("cp %s%s.zip %s.zip"%(path,name,name))
os.system("cp %s%s.zip %s.zip"%(path,name,name))
