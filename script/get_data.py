
import requests
import json
from bs4 import BeautifulSoup
def process(site_url):
    #print()
    #print("processing {}".format(site_url))
    res = requests.get(site_url)
    res.encoding = 'utf8' 
    soup = BeautifulSoup(res.text, "html.parser")
    trs = soup.find_all('tr')

    info_type = trs[1].text.strip().split()[0].split(":")[-1]

    title_lst = trs[2].text.strip().split()
    # ['院校代号', '院校名称', '录取数', '科类', '录取志愿', '录取最高分', '录取最低分']
    # ['院校代号', '院校名称', '计划数', '录取数', '科类', '录取志愿', '录取最高分', '录取最低分']
    
    
    datas = []
    for tr in trs[3:]:
        data = tr.text.replace("国家贫困专项 男","国家贫困专项男",999).strip().split()
        
        if len(title_lst) == 8:
            if len(data)==8:
                datas.append( data[0:2]+data[3:8])
            else :
                datas.append( data)
        else :
            if(len(data)<7):
                continue
            datas.append( data )
    # ['院校代号', '院校名称', '录取数', '科类', '录取志愿', '录取最高分', '录取最低分']
    print("url:{},type:{},count:{}".format(site_url,info_type,len(datas)))
    return datas,site_url,info_type

def main():
    sites_list = open("../origin_data/sites.txt","r").read().strip().split()

    parse_data = []
    for site_url in sites_list[:]:
        raw_datas,origin_url,info_type = process(site_url)
        for data in raw_datas:
            print(data,len(data))
            if(len(data)!=7):
                if data[0] in ["4124","1130"]:
                    data.pop(2)
                elif data[0] in ["4484"]:
                    data.pop(7)
                else :
                    exit(0)
            try:
                parse_data.append({
                    "school_id":data[0],
                    "school_name":data[1],
                    "count":data[2],
                    "type1":data[3],
                    "type2":data[4],
                    "high_score":int(data[5].split('(')[0].split('.')[0]),
                    "low_score":int(data[6].split('(')[0].split('.')[0]),
                    "origin":origin_url,
                    "info_type":info_type
                })
            except :
                print("error",data)
                if data[0] in ["6536","3166","9561"]:
                    continue
                else :
                    exit(0)
        print()
    f=open("./data/res.json","w")
    f.write(json.dumps(parse_data, indent=4))
    f.close()
        
    return
if __name__ == "__main__":
    main()