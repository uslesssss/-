import demo
import json
import sys
import base64


def final_deal(s):  # s为json字符串
    lsts = json.loads(s)
    dic = {}
    for i, j in zip(lsts[0].values(), lsts[0].keys()):
        if not i:
            continue
        dic[j] = demo.recog(str(i))

    lsts_ = []

    for lst in lsts:
        dic_temp = {}
        lsts_.append(dic_temp)
        for i in lst.keys():
            cla = dic.get(i)

            if not cla:
                continue
            else:
                if cla[1] == 'AllType':
                    dic_temp[f'{i}_cover'] = cla[0](str(lst[i])).cover()
                else:
                    dic_temp[f'{i}_cover'] = cla[0](str(lst[i])).cover()
                    dic_temp[f'{i}_shuffle'] = cla[0](str(lst[i])).shuffle()
                    dic_temp[f'{i}_md'] = cla[0](str(lst[i])).md()
                    dic_temp[f'{i}_randmapping'] = cla[0](str(lst[i])).randmapping()

    for i, j in zip(lsts, lsts_):
        i.update(j)
    return lsts


if __name__ == '__main__':
    with open('./json.txt', encoding='utf-8-sig') as f:
        s = f.read()

    # s = sys.argv[-1]
    # s=base64.b64decode(s)
    # s=str(s, 'utf-8')
    re = final_deal(s)
    print(json.dumps(re, ensure_ascii=False))
    # print(type(s))
    # lsts = json.loads(s)
    # print(type(lsts))
    # print(s)
