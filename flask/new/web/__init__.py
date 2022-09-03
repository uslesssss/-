from flask_restful import Api
from flask import request,Flask
from web.api import *
app=Flask(__name__)
#这里还需要一些配置


API=Api(app)
API.add_resource(GetDeal,'/getdeal',endpoint='getdeal')