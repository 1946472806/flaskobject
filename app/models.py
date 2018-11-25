from app.ext import db


class User(db.Model):
    id   = db.Column(db.Integer,primary_key=True,autoincrement=True)
    telephone = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(256))
    name = db.Column(db.String(50))
    token = db.Column(db.String(256))
    isdelete = db.Column(db.Boolean,default=False)
    email = db.Column(db.String(256))
    isactive = db.Column(db.Boolean,default=False)
    icon = db.Column(db.String(100),default='default.png')
    permissions = db.Column(db.Integer,default=1)

#轮播图
class Lunbo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bannerid = db.Column(db.Integer,unique=True)
    type = db.Column(db.Integer)
    object_id = db.Column(db.Integer)
    title = db.Column(db.String(55))
    url = db.Column(db.String(155))
    image = db.Column(db.String(256))
    description = db.Column(db.String(256))
    userid = db.Column(db.String(55))
    addtime = db.Column(db.String(55))
    uptime = db.Column(db.String(55))
    orderid = db.Column(db.Integer)
    cateid = db.Column(db.Integer)
    count_click = db.Column(db.Integer)
    status = db.Column(db.Integer)
    start_time = db.Column(db.String(55))
    end_time = db.Column(db.String(55))
    extra = db.Column(db.String(256))
    extra_data = db.Column(db.String(256))

# 电影模型类
class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    postid = db.Column(db.String(50))
    title= db.Column(db.String(256))
    wx_small_app_title = db.Column(db.String(256))
    pid = db.Column(db.Integer)
    app_fu_title = db.Column(db.String(56))
    is_xpc=db.Column(db.Integer)
    is_promote=db.Column(db.Integer)
    is_xpc_zp=db.Column(db.Integer)
    is_xpc_cp=db.Column(db.Integer)
    is_xpc_fx=db.Column(db.Integer)
    is_album=db.Column(db.Integer)
    tags=db.Column(db.String(56))
    recent_hot=db.Column(db.Integer)
    discussion=db.Column(db.Integer)
    image=db.Column(db.String(256))
    rating=db.Column(db.String(16))
    duration=db.Column(db.Integer)
    publish_time=db.Column(db.String(56))
    like_num=db.Column(db.Integer)
    share_num=db.Column(db.Integer)
    post_type=db.Column(db.Integer)
    cates=db.Column(db.String(556))

# 收藏模型
class Savegood(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(50))
    postid = db.Column(db.String(50))
    flag = db.Column(db.Boolean,default=False)