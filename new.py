import json

class MapReduce:
    def __init__(self):
        self.intermediate=[]
        self.result=[]

    def mapper(self,key,value):
        
