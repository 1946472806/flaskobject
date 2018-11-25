from flask_restful import Resource


class NameResource(Resource):
    def get(self,str):
        return {'msg':'请求参数:' + str}