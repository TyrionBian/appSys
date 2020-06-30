import requests
from app.datasource import preprocess


class JobFlow:
    def __init__(self, id, position, jobList):
        self.id = id
        self.position = position
        self.jobList = jobList
        self._len = len(self.jobList)

    def next(self, step=1):
        if float(step).is_integer() and step<=self._len:
            if((self.position + step) < self._len):
                self.position = self.position+step
            else:
                self.position = -1
        else:
            raise ValueError('Param step need Integer and not larger then len(job) please.')
    
    def run(self):
        data = {'id':self.id, 'jobID':self.jobList[self.position], 'jobList':self.jobList}
        preprocess(data)

    def __call__(self):
        return(self.run())
    
    def __repr__(self):
        fmt = '<JobFlow, position: {}, jobList: {}>'
        return fmt.format(self.position, self.jobList)  
