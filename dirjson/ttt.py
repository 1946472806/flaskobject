
import pymysql
from flask import json

db = pymysql.connect(host='127.0.0.1', user='root', password="200417",database='flaskobjectdb', port=3306,charset='utf8')
cursor = db.cursor()

with open('lunbo.json','r') as fp:
    collection = json.load(fp)
    returnValue = collection.get('data')
    db.begin()
    for Value in returnValue:
        cursor.execute("insert into lunbo(bannerid,type,object_id,title,url,image,description,userid,addtime,uptime,orderid,cateid,count_click,status,start_time,end_time) values ({},{},{},'{}','{}','{}','{}','{}','{}','{}',{},{},{},{},'{}','{}')".format(Value['bannerid'],Value['type'],Value['object_id'],Value['title'],Value['url'],Value['image'],Value['description'],Value['userid'],Value['addtime'],Value['uptime'],Value['orderid'],Value['cateid'],Value['count_click'],Value['status'],Value['start_time'],Value['end_time']))
        db.commit()


