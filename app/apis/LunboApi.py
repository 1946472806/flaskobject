from flask_restful import Resource, fields, marshal_with

from app.models import Lunbo


user_fields = {
        'bannerid':fields.Integer,
        'image':fields.String
}

result_fields = {
    'msg':fields.String,
    'status':fields.Integer,
    'data':fields.List(fields.Nested(user_fields))
}
class LunboResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        # 轮播数据
        wheels = Lunbo.query.all()
        responsedata = {
            'msg':'获取数据成功',
            'status':200,
            'data':wheels
        }
        return responsedata
