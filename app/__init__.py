from flask import Flask

from app.apis import init_api
from app.ext import init_ext
from app.models import db
from app.settings import init_setting
from app.views import init_views


def create_app(env_name='default'):
    app = Flask(__name__,template_folder='../templates',static_folder='../static') #加上template_folder属性才能访问模板文件,static_folder属性访问静态文件

    #配置相关
    init_setting(app,env_name)
    #插件相关
    init_ext(app)
    #蓝图
    init_views(app)
    #api
    init_api(app)


    return app