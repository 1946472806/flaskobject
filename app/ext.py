from flask_bootstrap import Bootstrap
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #实例化数据库对象
migrate = Migrate() #实例化数据迁移对象
sess = Session() #实例化session对象
bootstrap = Bootstrap()
toolbar = DebugToolbarExtension()
cache = Cache(config={'CACHE_TYPE': 'redis'})
mail = Mail()


def init_ext(app):
    db.init_app(app=app)
    migrate.init_app(app=app,db=db)
    sess.init_app(app=app)
    bootstrap.init_app(app=app)
    # toolbar.init_app(app=app)
    cache.init_app(app=app)
    mail.init_app(app=app)