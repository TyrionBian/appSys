import os
import requests
import json
import datetime
import time
import happybase
from flask import Flask
from flask import request

control_server = os.environ['CONTROL_SERVER']

def preprocess(data):
    #data have: id, jobID
    #1. 获取基本信息
    url = "http://"+control_server+":5000/" + "/application/{uuid}".format(uuid=data["id"])
    r = requests.get(url=url)
    info = r.json() # get application info

    dt = datetime.datetime.strptime(info["applytime"], "%Y-%m-%d %H:%M:%S.%f")
    ts_h = int((time.mktime(dt.timetuple()) + (dt.microsecond / 1000000.0))*1000)

    #2. 请求数据源
    ## TODO get data with url
    res = open('dt_success.txt', 'r+')
    res = res.read()
    
    ## write to hbase
    connection = happybase.Connection(host='localhost',port=9090)
    table = connection.table('mytable')
    table.put(info['uuid'].encode('utf-8'), {b'cf1:jxlmiguan': res.encode('utf-8')},timestamp=ts_h)

    #3. 添加模型任务到队列
    r = requests.post("http://"+control_server+':5000/schedule/', json={
    "topic": "data",
    "key": info['uuid'],
    "value": data["jobID"]
    })

    return 'OK'