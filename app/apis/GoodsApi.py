
from flask_restful import Resource, fields, marshal_with

# 登录
from app.models import Goods
from app.tools import format_response


user_fields = {
        'id':fields.Integer,
        'postid':fields.String,
        'title':fields.String,
        'wx_small_app_title':fields.String,
        'image':fields.String,
        'like_num':fields.Integer,
        'duration':fields.String
}

result_fields = {
    'msg':fields.String,
    'status':fields.Integer,
    'time':fields.String,
    'err':fields.String,
    'data':fields.List(fields.Nested(user_fields))
}

class GoodsResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        goods = Goods.query.all()
        # if not goods.count():
        #     return format_response(msg='获取界面数据失败!',status=406,err='没有界面数据!')
        #

        return format_response(msg='获取界面数据成功!',status=200,data=goods)