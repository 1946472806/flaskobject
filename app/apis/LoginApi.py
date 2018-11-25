import time

from flask import render_template
from flask_mail import Message
from flask_restful import Resource, reqparse, fields, marshal_with
from werkzeug.security import generate_password_hash, check_password_hash

from app.ext import mail, cache, db
from app.models import User


# 登录
from app.tools import get_token, format_response

parser = reqparse.RequestParser()
#定制请求参数格式
parser.add_argument('telephone',type=str,help='请输入手机号',required=True)
parser.add_argument('password',type=str,help='请输入密码',required=True)


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

class Login(Resource):
    @marshal_with(result_fields)
    def post(self):
        responsedata = {
            'time': str(int(time.time()))
        }
        parse = parser.parse_args()
        telephone = parse.get('telephone')
        password = parse.get('password') # 加密处理
        users = User.query.filter(User.telephone == telephone)
        if not users.count():
            return format_response(msg='登录失败!',status=406,err='用户不存在!')
        user = users.first()
        if user.isdelete:
            return format_response(msg='登录失败!',status=406,err='用户已经注销!')
        if not check_password_hash(user.password,password): #校验密码
            return format_response(msg='登录失败!',status=406,err='密码错误!')
        else:
            if not user.isactive: #激活
                # 邮件信息
                msg = Message(subject='Tpp激活邮件',
                              recipients=[user.email],  # 收件人邮箱
                              sender="15919913340@163.com")  # 发件人
                body_html = render_template('mail_send.html', name=user.name,
                                            active_url='http://127.0.0.1:5000/api/v1/useractive?token=' + user.token)
                msg.html = body_html
                # 发送邮件
                mail.send(msg)

                # 状态保持,即控制注册链接的有效时间
                cache.set(user.token, user.id, timeout=60)
                return format_response(msg='登录失败!',status=406,err='用户还没有激活,激活链接已经重新发送!!')
            user.token = get_token()
            db.session.add(user)
            db.session.commit()

            return format_response(msg='登录成功!',status=200,data=user)