import pymysql
from flask import json

db = pymysql.connect(host='127.0.0.1', user='root', password="200417",database='flaskdb', port=3306,charset='utf8')
cursor = db.cursor()

with open('city.json','r') as fp:
    city_collection = json.load(fp)
    returnValue = city_collection.get('returnValue')
    letter_keys = returnValue.keys()
    # db.begin()
    for letter in letter_keys:
    #     cursor.execute("insert into letter(name) values ('{}')".format(letter))
    # db.commit()
        listValue = returnValue[letter]
        db.begin()
        cursor.execute("select id from letter where name='{}'".format(letter))
        letterid = cursor.fetchone()[0]
        for item in listValue:
            cursor.execute("insert into city values({},'{}','{}','{}',{})".format(item['id'],item['regionName'],item['cityCode'],item['pinYin'],letterid))

        db.commit()