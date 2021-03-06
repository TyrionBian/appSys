import requests
from .strategy import JobFlow
import os

control_server = os.environ['CONTROL_SERVER']

def drive(id, jobList):
    id = id.decode('utf-8')
    jobList = jobList.decode('utf-8').split("_")
    # status_code: 201 accept, 202 pending, 203 reject, 204 error
    _len = len(jobList)
    job_flow = JobFlow(id=id, position=0, jobList=jobList)
    job = job_flow.job
    job.run()

    # while (status_code == 202 and job_flow.position < _len and job_flow.position >= 0):
    #     job = job_flow.job
    #     status_code, content = job.run()
    #     print(status_code)
    #     job_flow.next()

    # if status_code == 201:
    #     print("accept")
    # else:
    #     print("reject, status_code:{}.".format(status_code))
    
    
    # r = requests.post('http://'+control_server+':5000/status/uuid/', json={
    #     "uuid": job.id,
    #     "status": "finish"
    # })
    # print(job.id, job.jobID, job_flow.jobList)
