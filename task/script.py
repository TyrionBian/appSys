
import requests
import json
import uuid
import datetime
import os
from flask import request
from cache import get_redis, write_redis
from app.datasource import preprocess
from app.driver import drive

from flask import Flask
app = Flask(__name__)

control_server = os.environ['CONTROL_SERVER']

@app.route('/')
def some_job():
    #write_redis(key="msg:product1_channel1", value="chainid_20181221")
    #write_redis(key="wf:chainid_20181221", value="PS001_PS002_AF002_CP001_CP003")

    r = requests.post('http://'+control_server+':5000/application/', json={
    "productNum": "product1",
    "channelNum": "channel1",
    "name": "biantl",
    "idcard": "13092612313423234324",
    "phone": "18514027772"
    })

    print(r.status_code)

    print(json.loads(r.content).get('uuid'))

    uuid = json.loads(r.content).get('uuid')
    r = requests.get('http://'+control_server+':5000/application/'+uuid)
    apply_info = json.loads(r.content)

    # -------------------------------------------------------------------------

    chainid = get_redis(key="msg:"+ apply_info['productNum'] + "_" + apply_info['channelNum'])
    values = chainid.split("_")

    now = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')
    r = requests.post('http://'+control_server+':5000/status/', json={
    "uuid": apply_info['uuid'],
    "chainid": values[0],
    "chainversion": values[1],
    "status": "start",
    "createtime": now,
    "updatetime": now,
    "applytime": apply_info['applytime']
    })

    print(r.status_code)

    # -------------------------------------------------------------------------
    # get task flow
    print(chainid)
    task_flow = get_redis(key="wf:" + chainid)
    print(task_flow)


    # -------------------------------------------------------------------------
    # start tasks, 任务提交
    jobList = task_flow.split("_")
    drive(id=uuid, jobList=jobList, position=0)
    # r = requests.post('http://'+control_server+':5000/schedule/', json={
    # "topic": "test",
    # "key": uuid,
    # "value": task_flow
    # })
    # print(r.status_code)
    # print(r.content)


    return 'OK'

@app.route('/redis/<string:func>', methods=['POST'])
def redis_f(func):
    # redis function API, for write to redis, and get message from redis by key
    # Params
    # func:string, methods for write or get
    data = request.json
    if func=="write":
        write_redis(key=data["key"], value=data["value"])
    elif func=="get":
        get_redis(key=data["key"])

@app.route('/job', methods=['POST'])
def job():
    # drive job API
    data = request.json
    job_flow = data['job_flow']
    _len = len(job_flow.jobList)
    if((data['status_code'] == 202 and job_flow.position < _len and job_flow.position >= 0)):
        drive(id=data['id'], jobList=data['jobList'], position=data['position'])

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5001)
