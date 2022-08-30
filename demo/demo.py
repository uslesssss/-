from getdata import getdata
import random
import sys
import re
import hashlib


def samples(lst, size):  # 可重复采样
    ret = []
    for _ in range(size):
        ret.append(random.choice(lst))
    return ret


class AllType:
    def __init__(self, st) -> None:
        self.st = st

    def cover(self, a=0, b=0) -> str:
        return self.st[:a] + '*' * (len(self.st) - a) if b == 0 else self.st[:a] + '*' * (
                len(self.st) - a - b) + self.st[-1 * b:]

    def md(self):
        return hashlib.md5(self.st.encode('utf-8')).hexdigest()

    # def cut(self,a=0,b=0):

    # def intercept(self):

    def shuffle(self):
        temp = list(st)
        random.shuffle(temp)
        return ''.join(temp)

    def floa(self, num=0.1):  # 只能用于数字型
        temp = int(self.st)
        return str(random.choice([temp * (1 - num), temp * (1 + num)]))

    def rediff(self, a, b):  # 只能用于数字型
        temp = int(self.st)
        if temp <= a:
            return '低'
        elif temp <= b:
            return '中'
        else:
            return '高'


class Common(AllType):

    def cover(self, a=0, b=0) -> str:
        return super().cover(a, b)


class PersonName(AllType):

    def cover(self, a=0, b=0) -> str:
        return super().cover(1, b)

    def randmapping(self):
        n = len(self.st)
        first = getdata('first')
        male = getdata('male')
        female = getdata('female')
        t1 = [random.choice(first) + ''.join(samples(male, 1)), random.choice(first) + ''.join(samples(female, 1))]
        t2 = [random.choice(first) + ''.join(samples(male, 2)), random.choice(first) + ''.join(samples(female, 2))]
        t3 = [random.choice(first) + ''.join(samples(male, 3)), random.choice(first) + ''.join(samples(female, 3))]
        if n == 3: return random.choice(t2)
        if n == 2: return random.choice(t1)
        if n == 4: return random.choice(t3)


class Id(AllType):
    def randmapping(self):
        lst = [str(i) for i in range(10)]
        lst1 = [str(i) for i in range(1, 8)]
        lst1_ = [str(i) for i in range(1, 6)]
        lst2 = [str(i) for i in range(1960, 2000)]
        lst3 = [str(i) if i >= 10 else f'0{i}' for i in range(1, 13)]
        lst4 = lst + ['x']
        return ''.join(samples(lst1, 1)) + ''.join(samples(lst1_, 1)) + ''.join(samples(lst, 4)) + ''.join(
            samples(lst2, 1)) + ''.join(samples(lst3, 1)) + ''.join(samples(lst3, 1)) + ''.join(
            samples(lst, 3)) + ''.join(samples(lst4, 1))

    def cover(self, a=6, b=4) -> str:
        return super().cover(a, b)


class Phone(AllType):
    def randmapping(self):
        lst = [str(i) for i in range(10)]
        return self.st[:3] + ''.join(samples(lst, 8)) if len(self.st) == 11 else self.st[:6] + ''.join(samples(lst, 8))

    def cover(self, a=3, b=0) -> str:
        return super().cover(a, b)


class Post(AllType):
    def randmapping(self):
        lst1 = [str(i) for i in range(10, 75)]
        lst2 = [str(i) if i >= 10 else f'0{i}' for i in range(25)]
        lst3 = [str(i) if i >= 10 else f'0{i}' for i in range(40)]
        return random.choice(lst1) + random.choice(lst2) + random.choice(lst3)

    def cover(self, a=0, b=4) -> str:
        return super().cover(a, b)


class Email(AllType):
    def randmapping(self):
        lst = getdata('email')
        temp_a, temp_b = self.st.split('@')
        ret = samples([str(i) for i in range(0, 10)], len(temp_a))
        if temp_b not in lst: lst.append(temp_b)
        return ''.join(ret) + '@' + random.choice(lst)

    def cover(self, n=3) -> str:
        lst = getdata('email')
        temp_a, temp_b = self.st.split('@')
        ret = samples([str(i) for i in range(0, 10)], len(temp_a))
        return temp_a[:n] + '*' * (len(temp_a) - n) + '@' + random.choice(lst)


# class Date(AllType):#需要用户自行输入格式
#     def __init__(self, st) -> None:
#         super().__init__(st)
#     def randchange(self):

#     #范围内变动，格式，还需要讨论

class Ipv4(AllType):

    def cover(self, a=0, b=0) -> str:
        lst = self.st.split('.')
        lst[3] = '*' * 2
        lst[2] = '*' * 2
        return lst[0] + '.' + lst[1] + '.' + lst[2] + '.' + lst[3]

    def randmapping(self):
        temp = [str(i) for i in range(254)]
        return samples(temp, 1)[0] + '.' + samples(temp, 1)[0] + '.' + samples(temp, 1)[0] + '.' + samples(temp, 1)[
            0] + '.'


class Ipv6(AllType):

    def cover(self, a=0, b=0) -> str:
        temp = [str(i) for i in range(0, 10)] + ['a', 'b', 'c', 'd', 'e', 'f']
        ret = ''
        for _ in range(4):
            ret += (''.join(samples(temp, 4)) + ':')
        for _ in range(4):
            ret += (''.join(samples(temp, 2)) + '**:')

        return ret[:-1]

    def randmapping(self):
        temp = [str(i) for i in range(0, 10)] + ['a', 'b', 'c', 'd', 'e', 'f']
        ret = ''
        for _ in range(8):
            ret += (''.join(samples(temp, 4)) + ':')
        return ret[:-1]


class Passport(AllType):

    def cover(self, a=0, b=0) -> str:
        return super().cover(self, 3, 3)

    def randmapping(self):
        return ''.join(samples(list('EeKkGgDdSsPpHh'), 1) + samples(list(range(1, 9)), 8))


class Officer(AllType):

    def cover(self, a=0, b=0) -> str:
        return super().cover(self, 4, 3)

    def randmapping(self):
        return ''.join(samples(list('军兵士文职广'), 1) + '字弟' + samples(list(range(1, 9)), random.randint(4, 5)) + '号')


class Hukou(AllType):

    def cover(self, a=0, b=0) -> str:
        return super().cover(self, 3, 3)

    def randmapping(self):
        return ''.join(samples(list(range(10)), samples([15, 17, 18])))


def recog(st):
    name = '^[\u4e00-\u9fa5]{2,5}$'
    id = r'(^\d{6}[12]\d{3}([01]\d){2}\d{4}$)|(^\d{6}[12]\d{3}([01]\d){2}\d{3}X$)'  # 身份证
    phone = r'1[3,4,5,7,8]\d{9}'  # 电话
    post = '^[0-9]{6}$'  # 邮编
    email = r'^\w*@[a-zA-Z0-9]*\.[a-z]*$'  # 邮箱
    ipv4 = r'^[1-9][0-9]{0,3}\.[1-9][0-9]{0,3}\.[1-9][0-9]{0,3}\.[1-9][0-9]{0,3}$'  # ip
    passport = r'(^[EeKkGgDdSsPpHh]\\d{8}$)|(^(([Ee][a-fA-F])|([DdSsPp][Ee])|([Kk][Jj])|([Mm][Aa])|(1[45]))\\d{7}$)'  # 大陆护照
    officer = r'^[\u4E00-\u9FA5](字第)([0-9a-zA-Z]{4,8})(号?)$'  # 军官证
    # hukou = r'^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$'  # 户口本
    rules = [name, id, phone, post, email, ipv4, passport, officer]
    lst = ['PersonName', 'Id', 'Phone', 'Post', 'Email', 'Ipv4', 'Passport', 'Officer']
    for rule, cla in zip(rules, lst):
        if re.match(rule, st):
            return cla
    return 'AllType'


fun_name = ['randmapping', 'cover', 'md', 'shuffle']
if __name__ == '__main__':
    if sys.argv[-1] == '--help':
        print(getdata('help', 1))
    else:
        st, funname = sys.argv[1:]
        cla = recog(st)
        if cla == 'AllType':
            print(AllType(st).cover(2, 2))
        else:
            funname = fun_name[int(funname)]
            exec(f'''print({cla}('{st}').{funname}())''')
