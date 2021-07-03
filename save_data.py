from hash import Hash
import json 
##在檔案裡面沒東西的時候會有問題
class Data (): #裡面放不同的hash
    def __init__(self):
        self.database={} 
    ##存檔存不進去
    def save(self,ctx): #ctx為context物件
        try:   
            f=open('data.json','r',encoding='utf-8')
            raw=json.load(f) #return a dictionary with key=server name and value=list of class
        except :
            raw={}
        #寫入
        node_list=self.database[ctx].get_all_node()
        raw[ctx]=[] #清空再重新寫入
        for node in node_list:
            raw[ctx].append([node.Name,node.Teacher,node.Time,node.credit,node.great_points,node.disliked_points,node.comment])
        print(raw)
        f.close()
        f=open('data.json','w',encoding='utf-8')
        json.dump(raw,f)
        f.close()
    
    def load(self,ctx):
        self.database[ctx]=Hash(150)
        try:
            f=open('data.json','r',encoding='utf-8')
            raw=json.load(f)
            data=raw[ctx]  #回傳裝有課程資料的list
        except KeyError: #新的channel
            raw={ctx:[]}
            data=raw[ctx]  #回傳裝有課程資料的list
        print(raw)
        
        for c in data :
            self.database[ctx].insert(c)
        f.close()    