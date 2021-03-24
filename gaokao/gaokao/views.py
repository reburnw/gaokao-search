from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from bson import json_util
import json
import datetime

datas = json.loads(open("./gaokao/origin.json").read())

data_dict = {}
for i in datas:
    data_dict[str(i["id"])]=i

def hello(request):
    return JsonResponse({
        "msg":"hello world"
    },status=200)

def query(request):
    
    q_type = request.GET.get("q_type",None)
    q_id = request.GET.get("q_id",None)
    
    if q_type=="1":
        q_id = str(q_id)
        res = data_dict.get(q_id,{
            "id":-1,
            "context":"内容缺失",
            "option":[
            ]
        })
        return JsonResponse({
            "q_id":q_id,
            "data":res
        },status=200)
    else :
        return JsonResponse({
                "msg":"q_type error"
            },status=400)