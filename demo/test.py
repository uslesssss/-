import demo
import json
import sys
import base64









if __name__ == '__main__':
    # with open('./json.txt',encoding='utf-8-sig') as f:
    #     s=f.read()

    s = sys.argv[-1]
    s=base64.b64decode(s)
    s=str(s, 'utf-8')
    print(s)
    # s=sys.stdin.readline()
    # print(final_deal(s))
    # print(type(s))
    # lsts = json.loads(s)
    # print(type(lsts))
    # print(s)