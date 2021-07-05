from hash import Hash
import json 
import requests
##在檔案裡面沒東西的時候會有問題
class Data (): #裡面放不同的hash
    def __init__(self):
        self.database={} 
    ##存檔存不進去
    def save(self,ctx): #ctx為context物件
        
        response=requests.get("https://api.jsonstorage.net/v1/json/3f4e6ccf-02d2-492e-850f-f2b011e59f21")   
        raw=response.json()
        #寫入
        node_list=self.database[ctx].get_all_node()
        raw[ctx]=[] #清空再重新寫入
        for node in node_list:
            raw[ctx].append([node.Name,node.Teacher,node.Time,node.credit,node.great_points,node.disliked_points,node.NTUcourse,node.comment])
        print(raw)
        update=requests.put("https://api.jsonstorage.net/v1/json/3f4e6ccf-02d2-492e-850f-f2b011e59f21" 
        ,json=raw
        )
        print(update)
    
    def load(self,ctx):
        self.database[ctx]=Hash(150)
        try:
            response=requests.get("https://api.jsonstorage.net/v1/json/3f4e6ccf-02d2-492e-850f-f2b011e59f21")   
            raw=response.json()
            data=raw[ctx]  #回傳裝有課程資料的list
        except KeyError: #新的channel
            raw={ctx:[]}
            data=raw[ctx]  #回傳裝有課程資料的list
        print(raw)
        
        for c in data :
            self.database[ctx].insert(c)
       