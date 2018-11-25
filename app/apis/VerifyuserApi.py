from flask import jsonify
from flask_restful import Resource, reqparse

from app.models import User

parser = reqparse.RequestParser()
parser.add_argument('telephone',type=str,help='请输入电话号码',required=True)

class VerifyuserResource(Resource):
    def get(self):
        parse = parser.parse_args()
        telephone = parse.get('telephone')
        users = User.query.filter(User.telephone == telephone)
        if users.count():
            return jsonify({'msg': '用户已经存在!', 'status': '0'})
        else:
            return jsonify({'msg': '用户有效!', 'status': '1'})