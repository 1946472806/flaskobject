import time
from flask_restful import Resource

from app.ext import mail, cache, db
from app.models import Savegood, Goods


# 收藏
class Savegoods(Resource):
    def get(self,telephone,postid):
        responsedata = {
            'time': str(int(time.time()))
        }

        savegoods = Savegood.query.filter(Savegood.telephone == telephone).filter(Savegood.postid == postid)
        if savegoods.count():
            savegood = savegoods.first()
            db.session.delete(savegood)
            db.session.commit()

            good = Goods.query.filter(Goods.postid == postid).first()
            good.like_num = good.like_num - 1
            db.session.add(good)
            db.session.commit()

            db.session.commit()
            responsedata['msg'] = '收藏修改成功!'
            responsedata['status'] = 200
            responsedata['flag'] = 0
            responsedata['num'] = good.like_num
            return responsedata
        else:
            savegood = Savegood()
            savegood.telephone = telephone
            savegood.postid = postid
            savegood.flag = True
            db.session.add(savegood)
            db.session.commit()

            good = Goods.query.filter(Goods.postid == postid).first()
            good.like_num = good.like_num + 1
            db.session.add(good)
            db.session.commit()

            responsedata['msg'] = '添加收藏成功!'
            responsedata['status'] = 200
            responsedata['flag'] = 1
            responsedata['num'] = good.like_num
            return responsedata