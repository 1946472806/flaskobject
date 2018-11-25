from flask_restful import Api

from app.apis.ActiveApi import Active
from app.apis.ChangeinfoApi import Changinfo
from app.apis.ChecksvaeApi import Checksave
from app.apis.GetfinenameApi import GetFileName
from app.apis.GoodsApi import GoodsResource
from app.apis.LoginApi import Login
from app.apis.LunboApi import LunboResource
from app.apis.NameApi import NameResource
from app.apis.RegisterApi import Register
from app.apis.Savegood import Savegoods
from app.apis.VerifyuserApi import VerifyuserResource

api = Api()
def init_api(app):
    api.init_app(app=app)

# 轮播
api.add_resource(LunboResource,'/api/v1/getlunbo/')
# 检测用户是否存在
api.add_resource(VerifyuserResource,'/api/v1/verifyuser/')
#注册
api.add_resource(Register,'/api/v1/register/')
#激活
api.add_resource(Active,'/api/v1/useractive/')
#登录
api.add_resource(Login,'/api/v1/login/')
#获取图片
api.add_resource(GetFileName,'/api/v1/filename/')
#修改用户信息
api.add_resource(Changinfo,'/api/v1/changinfo/')
#展示的商品信息
api.add_resource(GoodsResource,'/api/v1/goods/')
#添加收藏或修改收藏状态
api.add_resource(Savegoods,'/api/v1/savegoods/<string:telephone>/<int:postid>/')
#判断是否已经收藏
api.add_resource(Checksave,'/api/v1/checksave/<string:telephone>/<int:postid>/')