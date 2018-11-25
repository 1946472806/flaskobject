import time
from flask_restful import Resource

from app.ext import mail, cache, db
from app.models import Savegood, Goods


# 收藏
class Checksave(Resource):
    def get(self,telephone,postid):
        responsedata = {
            'time': str(int(time.time()))
        }

        savegoods = Savegood.query.filter(Savegood.telephone == telephone).filter(Savegood.postid == postid)
        if savegoods.count():
            responsedata['status'] = 200
            return responsedata
        else:
            responsedata['status'] = 406
            return responsedata