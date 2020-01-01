# 没用了，就是之前没写允许非ascii字符，json里面汉字是\uxxxx，这个转换
import json
import os
import os.path
def proc(x):
    if x<=9:
        return "0"+str(x)
    else:
        return str(x)
for h in range(0,24):
    print(proc(h))
    f=open("2019-12-31-"+proc(h)+".txt","r",encoding="utf-8")
    ff=open("2019-12-31-"+proc(h)+".txtx","w",encoding="utf-8")
    lines=f.readlines()
    print(len(lines))
    for line in lines:
        j=json.loads(line)
        ff.write(json.dumps(j,ensure_ascii=False)+"\n")