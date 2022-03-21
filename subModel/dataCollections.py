from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from subModel.utils import *
import csv,json


transFile = "transctionDetails.json"
skuDetails = "skuDetails.json"


def transctionDetails(queryParams):
    response = {"result" : []}
    transactionJsonData = readJson(transFile)
    skuJsonData = readJson(skuDetails)
    transID = queryParams.get("transId",None)
    try:
        output_dict = [item for item in transactionJsonData["result"] if ((item['transaction_id'] == str(transID)))]
        for item in output_dict:
            finaldata = {}
            skuID = item["sku_id"]
            transactionId = item["transaction_id"]
            skuPrice = item["sku_price"]
            transactionDateTime = item["transaction_datetime"]
            for item in skuJsonData["result"]:
                test = item["sku_id"]
                if skuID == test:
                    skuName = item["sku_name"]
            finaldata["sku_name"] = skuName
            finaldata["sku_id"] = skuID
            finaldata["transaction_id"] = transactionId
            finaldata["sku_price"] = skuPrice
            finaldata["transaction_datetime"] = transactionDateTime
            response["result"].append(finaldata)
        return response
    except Exception as ex:
        print(str(ex))


def filterDataByDate(queryParams):
    response = {"summary" : []}
    constQueryParam = int(queryParams.get("daysago",None))
    startDate = str(dateFormat(constQueryParam))
    transactionJsonData = readJson(transFile)
    skuJsonData = readJson(skuDetails)
    try:
        output_dict = [item for item in transactionJsonData["result"] if ((item['transaction_datetime'] >= startDate))]
        output_json = json.dumps(output_dict)
        for i in output_dict:
            tempData = {}
            subId = i["sku_id"]
            transPrice = i["sku_price"]
            for item in skuJsonData["result"]:
                test = item["sku_id"]
                if subId == test:
                    skuName = item["sku_name"]
            tempData["skuName"] = skuName
            tempData["transactionPrice"] = transPrice
            response["summary"].append(tempData)
        return response
    except Exception as ex:
        print(str(ex))



def filterDataByCategory(queryParams):
    response = {"summary" : []}
    constDateParam = int(queryParams.get("daysago",None))
    startDate = str(dateFormat(constDateParam))
    transactionJsonData = readJson(transFile)
    skuJsonData = readJson(skuDetails)
    try:
        output_dict = [item for item in transactionJsonData["result"] if ((item['transaction_datetime'] >= startDate))]
        output_json = json.dumps(output_dict)
        for i in output_dict:
            tempData = {}
            subId = i["sku_id"]
            transPrice = i["sku_price"]
            for item in skuJsonData["result"]:
                test = item["sku_id"]
                if subId == test:
                    skuCat = item["sku_category"]
                tempData["skuCategory"] = skuCat
                tempData["transactionPrice"] = transPrice
            response["summary"].append(tempData)
            
        return response
    except Exception as ex:
        print(str(ex))

