import json 

def process(lst):
    score_info = []

    for idx in range(len(lst)):
        
        if idx>0:
            score_info.append({
                "score":int(lst[idx].split()[0]),
                "high":int(lst[idx-1].split()[2]),
                "low":int(lst[idx].split()[2]),
            })
        else :
            score_info.append({
                "score":int(lst[idx].split()[0]),
                "high":0,
                "low":int(lst[idx].split()[2]),
            })
        
        
    return score_info

def check(x,y):
    # print(x,y)
    if (x["high"]<y["low"]) & (x["low"]>y["high"]):
        return True
    else :
        return False

def main():
    wen_21 = process(open("./gaokao/gaokao/2021_wen").read().strip().split('\n'))
    li_21 = process(open("./gaokao/gaokao/2021_li").read().strip().split('\n'))
    
    wen_20 = process(open("./gaokao/gaokao/2020_wen").read().strip().split('\n'))
    li_20 = process(open("./gaokao/gaokao/2020_li").read().strip().split('\n'))

    # wen_19 = process(open("./gaokao/gaokao/2019_wen").read().strip().split('\n'))
    # li_19 = process(open("./gaokao/gaokao/2019_li").read().strip().split('\n'))
    
    for i in wen_21:
        i["related_score"] = []
        for j in wen_20:
            if(check(i,j)):
                i["related_score"].append(j["score"])

    for i in li_21:
        i["related_score"] = []
        for j in li_20:
            if(check(i,j)):
                i["related_score"].append(j["score"])

    f = open("./gaokao/gaokao/wen.json","w")
    f.write(json.dumps(wen_21,indent=4))
    f.close()

    f = open("./gaokao/gaokao/li.json","w")
    f.write(json.dumps(li_21,indent=4))
    f.close()
    
    
        
    

if __name__ == "__main__":
    main()