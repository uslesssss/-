from base64 import decode
import os
def getdata(st,t=0):#t=1不输出列表直接输出文本
    path=os.path.dirname(__file__)
    path=os.path.join(path,f'{st}.txt')
    with open(path,encoding='utf-8-sig') as f:
        temp=f.read()
    if t==1:return temp
    temp=temp.split(',')
    return temp


