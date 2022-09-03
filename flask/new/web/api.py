from ast import arg
from inspect import ArgSpec
from flask_restful import Resource,reqparse
from flask import request
import json
from demo import test

def validjson(s):
    if isinstance(s,json.array):
        return s
    else:
        return isinstance(s,json.array)


class GetDeal(Resource):
    def __init__(self) -> None:
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('data',required=True,action='append')

    def post(self):
        args=self.parser.parse_args()
        data=args.data[:-1]
        data_=[]
        for i in data:
            data_.append(json.loads(i.replace("'",'"')))
        data_=test.final_deal(data_) 
        return data_
