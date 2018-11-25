import time

from flask_restful import Resource, reqparse, fields, marshal_with

from app.ext import cache, db
# 激活
from app.models import User
from app.tools import get_token

class IconForm(fields.Raw):
    def format(self, value):
        return '/static/img/' + value

user_fields = {
        'telephone':fields.String,
        'password':fields.String,
        'name':fields.String,
        'token':fields.String,
        'email':fields.String,
        'icon':IconForm(attribute='icon'),
        'permissions':fields.Integer
}

result_fields = {
    'msg':fields.String,
    'status':fields.Integer,
    'time':fields.String,
    'err':fields.String,
    'data':fields.Nested(user_fields)
}

# 请求参数 定制
parser = reqparse.RequestParser()
parser.add_argument('telephone',type=str,help='请输入telephone')
class GetFileName(Resource):
    @marshal_with(result_fields)
    def get(self):
        parse = parser.parse_args()
        telephone = parse.get('telephone')
        users = User.query.filter(User.telephone == telephone)
        if users.count():
            user = users.first()
            responsedata = {
                'msg': '获取图片成功!',
                'status': 200,
                'time': str(int(time.time())),
                'data': user
            }
            return responsedata
        else:
            responsedata = {
                'msg': '获取图片失败!',
                'status': 406,
                'time': str(int(time.time()))
            }
            return responsedata
