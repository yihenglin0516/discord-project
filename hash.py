from bs4.element import Tag
import linked_list
class Hash:
    def __init__(self,size):
        self.size=size
        self.table=[linked_list.Linked_list() for i in range(size)]
    def _insert(self,item):  #item是list
        index=0
        key=item[0]+' '+item[1]
        for i,character  in enumerate(key): #hashing 
            index+=(ord(character)//100)**i
        index=index%self.size
        print('key= '+key+'index= '+str(index))
        _item=linked_list.node(item)
        self.table[index].push(_item)
    def output(self): #只show出基本的info 
        result=''
        for i in self.table:
            if i.root:
                result+=i.show()
        return result 
    def find(self,key):
        index=0
        key=str.strip(key)
        print(key)
        for i,character  in enumerate(key): #hashing 
            index+=(ord(character)//100)**i
        index=index%self.size
        print(index)
        target=self.table[index]
        pointer=target.root
        while pointer:
            _key=pointer.value[0]+' '+pointer.value[1]
            if _key==key:
                return pointer._output()
            else:
                pointer=pointer.next 
        return 'class not found '
            

        
        
        




