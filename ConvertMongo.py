from pymongo import MongoClient
import pandas as pd
from typing import TypedDict


class ConvertMongo:

    def __init__(self,data_base,collection,CONNECT_STRING):

        #'mongodb://localhost:27017/'

        self.dictionary_data = {}
     
        self.CONNECTION_STRING =CONNECT_STRING
        self.collection_str = collection
        self.data_base_str = data_base
        try:
            self.client = MongoClient(self.CONNECTION_STRING,serverSelectionTimeoutMS=5000)
            self.client.admin.command('ping')
            self.data_base = self.client[data_base]
            self.collection = self.data_base[collection]
            print('Succesful')
                    

        except:
            print('Failed')

    def selectDs(self,collection:str,db:str):
        self.collection_str = collection
        self.data_base_str = db
        try:
            data_base = self.client[db]
            collection = data_base[collection]
            print('Succesful')
        except:
            print('failed')
    def ConvertCvdstr(self,csv:str):
        df = pd.read_csv(csv)
        df = df.loc[:,df.columns!='#']

        df_dict = df.to_dict('records')

        for i in range(len(df_dict)):
            result = self.collection.insert_one(df_dict[i])

            
    def ConvertCsv(self,df:object):
        df = df.loc[:,df.columns!='#']
        df_dict = df.to_dict('records')

        
        for i in range(len(df_dict)):
            result = self.collection.insert_one(df_dict[i])
