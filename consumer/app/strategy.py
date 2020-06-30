import requests
from app.datasource import preprocess

class Job:
    def __init__(self, id, jobID):
        self.id = id
        self.jobID = jobID

    def run(self):
        data = {}
        data['id'] = self.id
        data['jobID'] = self.jobID
        preprocess(data)
        # r = requests.post('http://127.0.0.1:5000/model/CP001', json={
        #     "id": self.id,
        #     "jobID": self.jobID
        # })
        # return r.status_code, r.content
        from random import choice
        return choice([201,202,203,204,202,202,202,202,202,202,202,202,202,202,202,202,202,202,202]), 0

    def __call__(self):
        return(self.run())
    
    def __repr__(self):
        fmt = '<Job, jobID: {}, jobList: {}>'
        return fmt.format(self.jobID) 

class JobFlow:
    def __init__(self, id, position, jobList):
        self.id = id
        self.position = position
        self.jobList = jobList
        self._len = len(self.jobList)
        self.job = Job(self.id, jobList[self.position])

    def next(self, step=1):
        if float(step).is_integer() and step<=self._len:
            if((self.position + step) < self._len):
                self.position = self.position+step
                self.job = Job(self.id, self.jobList[self.position])
            else:
                self.position = -1
        else:
            raise ValueError('Param step need Integer and not larger then len(job) please.')
    
    def __repr__(self):
        fmt = '<JobFlow, position: {}, jobList: {}>'
        return fmt.format(self.position, self.jobList)  
