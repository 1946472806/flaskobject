
import pymysql
from flask import json

db = pymysql.connect(host='127.0.0.1', user='root', password="200417",database='flaskobjectdb', port=3306,charset='utf8')
cursor = db.cursor()

with open('movie.json','r') as fp:
    collection = json.load(fp)
    returnValue = collection.get('data')
    db.begin()
    for Value in returnValue:
        cursor.execute("insert into goods(postid,title,wx_small_app_title,pid,app_fu_title,is_xpc,is_promote,is_xpc_zp,is_xpc_cp,is_xpc_fx,is_album,tags,recent_hot,discussion,image,rating,duration,publish_time,like_num,share_num,post_type) "
                       "values ('{}','{}','{}',{},'{}',{},{},{},{},{},{},'{}',{},{},'{}','{}',{},'{}',{},{},{})".format(Value['postid'],Value['title'],Value['wx_small_app_title'],Value['pid'],Value['app_fu_title'],Value['is_xpc'],Value['is_promote'],Value['is_xpc_zp'],
                                                                  Value['is_xpc_cp'],Value['is_xpc_fx'],Value['is_album'],Value['tags'],Value['recent_hot'],Value['discussion'],
                                                                  Value['image'],Value['rating'],Value['duration'],Value['publish_time'],Value['like_num'],Value['share_num'],Value['post_type']))
        db.commit()

