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
parser.add_argument('token',type=str,help='请输入token',required=True)
class Active(Resource):
    @marshal_with(result_fields)
    def get(self):
        parse = parser.parse_args()
        token = parse.get('token')
        userid = cache.get(token)
        if not userid:
            responsedata={
                'msg':'激活失败!',
                'status':401,
                'time':str(int(time.time())),
                'err':'链接已失效!'
            }
            return responsedata
        user = User.query.get(userid)
        user.isactive = True
        user.token = get_token()
        db.session.add(user)
        db.session.commit()
        responsedata = {
            'msg': '激活成功!',
            'status': 200,
            'time': str(int(time.time())),
            'data': user
        }
        return responsedata