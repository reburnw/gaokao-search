from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from bson import json_util
import json
import datetime

datas = json.loads(open("./gaokao/res.json").read())

def hello(request):
    return JsonResponse({
        "msg":"hello world"
    },status=200)

def query(request):
    
    q_type = request.GET.get("q_type",None)
    q_type1 = request.GET.get("q_type1",None)
    q = request.GET.get("q",None)
    
    if q_type=="1":
        q_score = 0
        try :
            q_score = int(q)
        except :
            return JsonResponse({
                "msg":"q error"
            },status=404)

        res_data = []
        for data in datas:
            if data["type1"] != q_type1:
                continue
            if((data["low_score"] <= q_score) & (data["high_score"] >= q_score)):
                res_data.append(data)
        return JsonResponse({
            "data":res_data,
            "size":len(res_data)
        },status=200)
    else :
        return JsonResponse({
                "msg":"q_type error"
            },status=200)