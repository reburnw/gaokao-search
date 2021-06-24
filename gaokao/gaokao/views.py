from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
import json
import datetime

datas = json.loads(open("./gaokao/res.json").read())

wen = json.loads(open("./gaokao/wen.json").read())

li = json.loads(open("./gaokao/li.json").read())


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

        q_res = None
        if q_type1 == "文史类":
            if q_score > 665:
                q_score=665
            if q_score < 180:
                q_score=180
            for i in wen:
                if i["score"] == q_score:
                    q_res = i
                    break
        if q_type1 == "理工类":
            if q_score > 695:
                q_score=695
            if q_score < 180:
                q_score=180
            for i in li:
                if i["score"] == q_score:
                    q_res = i
                    break
        # print(q_res)
        res_data = []
        for data in datas:
            if data["type1"] != q_type1:
                continue
            if(
                (data["low_score"] <= q_res["related_score"][-1]) & 
                (data["high_score"] >= q_res["related_score"][-1])
                ):
                res_data.append(data)
            elif (
                (data["low_score"] <= q_res["related_score"][0]) & 
                (data["high_score"] >= q_res["related_score"][0])
                ):
                res_data.append(data)

        return JsonResponse({
            "data":res_data,
            "size":len(res_data),
            "meta":q_res
        },status=200)
    else :
        return JsonResponse({
                "msg":"q_type error"
            },status=200)