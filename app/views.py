import hashlib
import random
import time
import uuid

from flask import Blueprint, render_template, url_for, redirect, make_response, abort, request, session, jsonify, g

from app.models import User, Goods
from app.ext import db, cache

blue = Blueprint('bluename',__name__)

def init_views(app):
    app.register_blueprint(blueprint=blue)

@blue.before_request
def before():
    token = session.get('token')
    if token:
        user = User.query.filter(User.token == token).first()
    else:
        user = None
    g.user = user

#注册
@blue.route('/register/',methods=['POST'])
def register():
    user = User()
    user.telephone = request.form.get('telephone')
    user.password = generate_password(request.form.get('password'))
    user.name = request.form.get('name')
    user.token = generate_password(str(uuid.uuid5(uuid.uuid4(),'register')) + str(time.time()))
    db.session.add(user)
    db.session.commit()
    session['token'] = user.token
    return redirect(url_for('bluename.index'))

#登录
@blue.route('/login/',methods=['POST'])
def login():
    telephone = request.form.get('ltelephone')
    password = generate_password(request.form.get('lpassword'))
    users = User.query.filter(User.telephone == telephone).filter(User.password == password)
    if users.count():
        user = users.first()
        user.token = generate_password(str(uuid.uuid5(uuid.uuid4(), 'register')) + str(time.time()))
        session['token'] = user.token
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('bluename.index'))
    return '登录失败!...'


#退出登录
@blue.route('/loginout/')
def loginout():
    session.pop('token')
    return redirect(url_for('bluename.index'))

#首页
@blue.route('/')
def index():
    #轮播数据
    lunbos = [
        {'name': 'Iphone I',  'img': '/static/img/lunbo1.jpg'},
        {'name': 'Iphone II', 'img': '/static/img/lunbo2.jpeg'},
        {'name': 'Iphone III', 'img': '/static/img/lunbo3.jpg'},
        {'name': 'Iphone VI', 'img': '/static/img/lunbo4.jpg'},
    ]
    #分页
    page = int(request.args.get('page') or 1)
    per = 6
    paginate = Goods.query.paginate(page,per)
    title = '苹果手机'
    return render_template('bootstrap.html',user=g.user,paginate=paginate,title=title,lunbos=lunbos)

# 主页
@blue.route('/home/')
def home():
    return render_template('home.html',user=g.user)

# 购物车
@blue.route('/cart/')
def cart():
    return render_template('cart.html',user=g.user)

# 关于我们
@blue.route('/about/')
def about():
    return render_template('about.html',user=g.user)

#密码加密
def generate_password(str):
    sha = hashlib.sha512()
    sha.update(str.encode('utf-8'))
    return sha.hexdigest()


#可以不带参数，指定默认值即可
@blue.route('/getusername/')
@blue.route('/getusername/<name>/<age>/<sex>/')
def getusername(name='许仙',age=18,sex='女'):
    return '名字:' + name + '年龄:' + str(age) + '性别:' + sex

#指定参数的数值类型
@blue.route('/getnum/<int:a>/<int:b>/')
def getnum(a,b):
    return str(a + b)

#路径类型
@blue.route('/getpath/<path:pathurl>/')
def getpath(pathurl):
    return pathurl

#uuid类型
@blue.route('/getuuid/<uuid:uuidstr>/')
def getuuid(uuidstr):
    return uuidstr

#any类型
@blue.route('/getany/<any(A,B,C):op>/')
def getany(op):
    return op

#反向解析
@blue.route('/urlget/')
def urlget():
    path = url_for('bluename.getmethods') #蓝图名称.函数名
    return redirect(path)

#响应
#1.return 2.render_template 3.make_response 4.response()
@blue.route('/getresponse/')
def getresponse():
    response = make_response('hahhhaha',300) #300为返回给客户端的状态码
    return response
#-------------------------------------------------
#抛出异常
@blue.route('/geterror/')
def geterror():
    abort(401)

#异常处理
@blue.errorhandler(401)
def err401(ex):
    return '<h1>401，不存在的网页</h1>'
#-------------------------------------------------

#保存数据
@blue.route('/savedb/')
def savedb():
    user = User()
    user.name = '金庸-' + str(random.randint(1000,9999))
    user.age = random.randint(0,200)
    db.session.add(user)
    db.session.commit()
    return '插入数据成功!'
#查询数据
@blue.route('/querydb/')
@cache.cached(timeout=30)
def querydb():
    users = User.query.all()
    return render_template('showdb.html',users=users)

