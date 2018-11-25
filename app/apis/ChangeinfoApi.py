import os
import time

from flask_restful import Resource, reqparse, fields, marshal_with
from werkzeug.datastructures import FileStorage

from werkzeug.utils import secure_filename

from app.ext import db
from app.models import User
from app.settings import UPLOAD_RID
from app.tools import get_token

# 注册
parser = reqparse.RequestParser()
#定制请求参数格式
parser.add_argument('telephone',type=str,help='请输入手机号',required=True)
parser.add_argument('email',type=str,help='请输入邮箱',required=True)
parser.add_argument('filename', type=FileStorage, location='files', required=True, help='请选择头像img')


#定制返回参数格式
'''
{
    'msg':'注册成功',
    'stauts':200,
    'time':123456,
    'err':xxx,
    'data':{
        'telephone':xxxx,
        'password':xxx,
        'name':xxxx,
        'token':xxx,
        'email':xxxx,
        'icon':xxxx,
        'permissions':xxxx
    }
}
'''
# 定义格式的需求，可以继承 fields.Raw 类并且实现格式化函数
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

class Changinfo(Resource):
    @marshal_with(result_fields)
    def post(self):
        responsedata = {
            'time':str(int(time.time()))
        }
        print('##############')
        parse = parser.parse_args()
        print('$$$$$$$$$$$$$$$$')
        user = User()
        user.telephone = parse.get('telephone')
        user.name = parse.get('name')
        user.email = parse.get('email')
        # 图片数据
        imgfile = parse.get('filename')
        # 图片名称
        filename = '%s-%s' % (user.telephone, secure_filename(imgfile.filename))
        # 文件路径
        filepath = os.path.join(UPLOAD_RID, filename)
        user.token = get_token()
        users = User.query.filter(User.telephone == user.telephone)
        if users.count() > 0:
            user = users.first()
            # 保存文件
            imgfile.save(filepath)
            # 更新用户信息
            user.icon = filename
            db.session.add(user)
            db.session.commit()

            responsedata['msg'] = '修改成功!'
            responsedata['status'] = 200
            responsedata['data'] = user
            return responsedata

        else:
            responsedata['msg'] = '修改失败!'
            responsedata['status'] = 406
            return responsedata

