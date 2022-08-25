import email
from secrets import choice
from getdata import getdata
import random
import sys
import getopt

def samples(lst,size):#可重复采样
    re=[]
    for _ in range(size):
        re.append(random.choice(lst))
    return re

class AllType:
    def __init__(self,st) -> None:
        self.st=st

    def cover(self,a=0,b=0) -> str:
        return self.st[:a]+'*'*(len(self.st)-a) if b==0 else self.st[:a]+'*'*(len(self.st)-a-b)+self.st[-1*b:]
    # def cut(self,a=0,b=0):
        

    # def intercept(self):

    def shuffle(self):
        temp=self.st[:]
        random.shuffle(temp)
        return temp

    def floa(self,num=0.1):#只能用于数字型
        temp=int(self.st)
        return str(random.choice([temp*(1-num),temp*(1+num)]))
    
    def rediff(self,a,b):#只能用于数字型
        temp=int(self.st)
        if temp<=a:
            return '低'
        elif temp<=b:
            return '中'
        else:return '高'



class Common(AllType):

    def cover(self, a=0, b=0)-> str:
        return super().cover(a, b)
    
class PersonName(AllType):

    def cover(self, a=0, b=0)-> str:
        return super().cover(1, b)
    
    def randmap(self):
        n=len(self.st)
        first=getdata('first')
        male=getdata('male')
        female=getdata('female')
        t1=[random.choice(first)+''.join(samples(male,1)),random.choice(first)+''.join(samples(female,1))]
        t2=[random.choice(first)+''.join(samples(male,2)),random.choice(first)+''.join(samples(female,2))]
        t3=[random.choice(first)+''.join(samples(male,3)),random.choice(first)+''.join(samples(female,3))]
        if n==3:return random.choice(t2)
        if n==2:return random.choice(t1)
        if n==4:return random.choice(t3)

class ID(AllType):
    def randmap(self):
        lst=[str(i) for i in range(10) ]
        lst1=[str(i) for i in range(1,9) ]
        lst1_=[str(i) for i in range(1,6) ]
        lst2=[str(i) for i in range(1960,2000)]
        lst3=[str(i) if i>=10 else f'0{i}'for i in range(1,13)]
        lst4=lst+['x']
        return ''.join(samples(lst1,1))+''.join(samples(lst1_,1))+''.join(samples(lst,4))+''.join(samples(lst2,1))+''.join(samples(lst3,1))+''.join(samples(lst3,1))+''.join(samples(lst,3))+''.join(samples(lst4,1))
    def cover(self, a=12, b=0) -> str:
        return super().cover(a, b)

class Phone(AllType):
    def randmap(self):
        lst=[str(i) for i in range(10) ]
        return self.st[:3]+''.join(samples(lst,8)) if len(self.st)==11 else self.st[:6]+''.join(samples(lst,8))
    def cover(self, a=3, b=0) -> str:
        return super().cover(a, b) 

class Post(AllType):
    def randmap(self):
        lst1=[str(i) if i>=10 else f'0{i}' for i in range(10,75) ]
        lst2=[str(i) if i<10 else f'0{i}' for i in range(25) ]
        lst3=[str(i) if i<10 else f'0{i}' for i in range(40) ]
        return random.choice(lst1)+random.choice(lst2)+random.choice(lst3)
    
    def cover(self, a=0, b=4) -> str:
        return super().cover(a, b)

class Email(AllType):
    def randmap(self):
        lst=getdata('email')
        temp_a,temp_b=self.st.split('@')
        re=samples([str(i) for i in range(0,10)],len(temp_a))
        if temp_b not in lst:lst.append(temp_b)
        return ''.join(re)+'@'+random.choice(lst)
    
    def cover(self,n=3) -> str:
        lst=getdata('email')
        temp_a,temp_b=self.st.split('@')
        re=samples([str(i) for i in range(0,10)],len(temp_a))
        return temp_a[:n]+'*'*(len(temp_a)-n)+'@'+random.choice(lst)

# class Date(AllType):#需要用户自行输入格式
#     def __init__(self, st) -> None:
#         super().__init__(st)
#     def randchange(self):
        
#     #范围内变动，格式，还需要讨论

class Ipv4(AllType):

    def cover(self, a=0, b=0) -> str:
        lst=self.st.split('.')
        lst[3]='*'*2
        lst[2]='*'*2
        return lst[0]+'.'+lst[1]+'.'+lst[2]+'.'+lst[3]

    def randmap(self):
        temp=[str(i) for i in range(254)]
        return samples(temp,1)[0]+'.'+samples(temp,1)[0]+'.'+samples(temp,1)[0]+'.'+samples(temp,1)[0]+'.'

class Ipv6(AllType):

    def cover(self, a=0, b=0) -> str:
        temp=[str(i) for i in range(0,10)]+['a','b','c','d','e','f']
        re=''
        for _ in range(4):
            re+=(''.join(samples(temp,4))+':')
        for _ in range(4):
            re+=(''.join(samples(temp,2))+'**:')

        return re[:-1]

    def randmap(self):
        temp=[str(i) for i in range(0,10)]+['a','b','c','d','e','f']
        re=''
        for _ in range(8):
            re+=(''.join(samples(temp,4))+':')
        return re[:-1]





class_name=['AllType','PersonName','ID','Phone','Post','Ipv4','Ipv6','Email']
fun_name=['randmap','cover']
if __name__=='__main__':
    # opts,args = getopt.getopt(sys.argv[1:],'1:2:3:4:5:6:7:8:9:10:',[])
    if sys.argv[-1]=='--help':
        print(getdata('help',1))
    else:
        classname,funname,st=sys.argv[1:]
        classname,funname=class_name[int(classname[-1:])],fun_name[int(funname[-1:])]
        exec(f'''print({classname}('{st}').{funname}())''')
    


    
    



