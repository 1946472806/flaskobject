import hashlib
import time

import uuid

#获取token
def get_token():
    hash = hashlib.sha512()
    hashstr = str(uuid.uuid4()) + str(int(time.time()))
    hash.update(hashstr.encode('utf-8'))
    return hash.hexdigest()

# 返回数据格式化
def format_response(msg='', status=400, err='', data=None):
    responseData = {}
    responseData['msg'] = msg
    responseData['status'] = status
    responseData['time'] = str(int(time.time()))
    responseData['err'] = err
    responseData['data'] = data

    return responseData