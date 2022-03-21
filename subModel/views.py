from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import csv,json
import os
from subModel.utils import *
from subModel.dataCollections import *


def transaction_detail(request):
    try:
        response = transctionDetails(request.GET)
        return JsonResponse(response,safe = False)
    except Exception as ex:
        return Response({"result": []})


def transactionSummaryBySKU(request):
    try:
        result = filterDataByDate(request.GET)
        return JsonResponse(result,safe = False)
    except Exception as ex:
        return Response({"result": []})

def transactionSummaryByCategory(request):
    try:
        result = filterDataByCategory(request.GET)
        return JsonResponse(result,safe = False)
    except Exception as ex:
        return Response({"result": []})
