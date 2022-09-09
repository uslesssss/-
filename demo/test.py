from demo import *
import json
import sys
import base64


def deal_string(s, choice):  # 查询每一个数据的类型并处理
    if not s:
        return ""
    else:
        if not isinstance(s, str): s = str(s)
        cls, cls_name = recog(s)
        # print(s,cls_name)
        if cls_name == 'AllType':
            return cls(s).cover()
        else:
            funname = funname_dic[cls_name]

            for i in choice:
                if i in funname: break

            if i == 0:
                return cls(s).fixmapping()
            elif i == 1:
                return cls(s).randmapping()
            elif i == 2:
                return cls(s).cover()
            elif i == 3:
                return cls(s).md()


def final_deal(lst, choice, not_deal_lst=[]):  # 递归遍历每一个数据
    for ele in lst.keys() if isinstance(lst, dict) else range(len(lst)):
        if ele in not_deal_lst:
            continue
        if isinstance(lst[ele], list) or isinstance(lst[ele], dict):
            final_deal(lst[ele], choice, not_deal_lst)
        else:
            lst[ele] = deal_string(lst[ele], choice)


if __name__ == '__main__':
    with open(r'D:\AIIT\脱敏组件\test.json', encoding='utf-8-sig') as f:
        lst = f.read()
    #
    # lst=base64.b64encode(lst.encode('utf-8'))
    lst = sys.argv[-1]
    lst = base64.b64decode(lst)
    lst = str(lst, 'utf-8')
    lst = json.loads(lst)
    print(lst)
    final_deal(lst, [1, 2, 3])
    print(lst)
    # print(json.dumps(lst, ensure_ascii=False))
