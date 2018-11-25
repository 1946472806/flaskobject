import os

#根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_RID = os.path.join(os.path.dirname(os.path.abspath("__file__")), 'static/img/')

#基础类（公共配置）
class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '$%^&*()dfghjk123123j4567wfTYUI123123sdfadjhgpo., /.' #使用session要配置秘钥
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'redis' #session存储方式
    SESSION_COOKIE_NAME = 'userSession' # 存储在客户端的 key名称
    # PERMANENT_SESSION_LIFETIME = 10 #设置session的过期时间


def get_db_uri(database):
    db = database.get('db') or 'mysql'
    driver = database.get('driver') or 'pymysql'
    username = database.get('username') or 'root'
    password = database.get('password') or '200417'
    host = database.get('host') or '127.0.0.1'
    port = database.get('port') or '3306'
    dbname = database.get('dbname') or 'flaskobjectdb'

    return '{}+{}://{}:{}@{}:{}/{}'.format(db,driver,username,password,host,port,dbname)


class DevelopConfig(BaseConfig):
    DEBUG = True
    #数据库配置
    DATABASE = {
        'db':'mysql',
        'driver':'pymysql',
        'username':'root',
        'password':'200417',
        'host':'127.0.0.1',
        'port':'3306',
        'dbname':'flaskobjectdb'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)
    MAIL_SERVER = "smtp.163.com"
    MAIL_USERNAME = "15919913340@163.com"
    MAIL_PASSWORD = "a19910720"
    MAIL_DEFAULT_SENDER = '15919913340@163.com'

class TestingConfig(BaseConfig):
    TESTING = True


class StagingConfig(BaseConfig):
    pass


class ProductConfig(BaseConfig):
    pass


config = {
    'develop':DevelopConfig, #开发环境
    'testing':TestingConfig, #测试环境
    'staging':StagingConfig, #演示环境
    'product':ProductConfig,#线上环境
    'default':DevelopConfig,#默认环境
}

def init_setting(app,env_name):
    app.config.from_object(config.get(env_name))