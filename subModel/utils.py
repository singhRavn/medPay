from datetime import date
from datetime import datetime, timedelta
import csv,json
import os

csvFilePath = r'transactionDetails.csv'
jsonFilePath = r'transctionDetails.json'
csvFilePath1 = r'skuDetails.csv'
jsonFilePath1 = r'skuDetails.json'

def currentDate():
    todayDate = date.today()
    return todayDate

def dateFormat(N):
    date_N_days_ago = datetime.now() - timedelta(days=N)
    dateCurrent = date_N_days_ago.date()
    return dateCurrent


def readJson(fileName):
    module_dir = os.path.dirname(__file__)
    folderpath = os.path.join(module_dir,"JsonData")
    file_path = os.path.join(folderpath,fileName)
    if (os.path.exists(file_path)):
        with open(file_path,'r') as f:
            result = json.load(f)
            return result
    return {}   


def make_json(csvFilePath, jsonFilePath,id):
    try:
        data = {"result":[]}
        with open(csvFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            for rows in csvReader:
                result = rows[id]
                data["result"].append(rows) 
        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))
    except Exception as ex:
        print(str(ex))


