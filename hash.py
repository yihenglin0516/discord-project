from bs4.element import Tag
import linked_list

class Hash:
    def __init__(self,size):
        self.size=size
        self.table=[linked_list.Linked_list() for i in range(size)]
        

    def insert(self,item):  #item是list
        index=0
        key=item[0]+' '+item[1]
        for i,character  in enumerate(key): #hashing 
            index+=(ord(character)//100)**i
        index=index%self.size
        print('key= '+key+'index= '+str(index))
        _item=linked_list.node(item)
        self.table[index].push(_item)

    def list_all(self): #只show出基本的info 
        result=[]
        for i in self.table:
            if i.root:
                result.append(i.show())
        
        result = result[::-1]
        result = ''.join(result)
        return result 

    def search(self,key):
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
            _key=pointer.Name+' '+pointer.Teacher
            if _key==key:
                return pointer
            else:
                pointer=pointer.next 
        return 'class not found '

    def add_comment(self,ctx,classname,comment):
        target=self.search(classname)  #find  the class we want to insert 
        if type(target)==str:
            ctx.send('no such class') 
        else:
            target.comment+=str(ctx.author)+': '+comment+'\n'
            
    
    def great_points(self,classname):
        target = self.search(classname)
        
        if type(target) == str:
            pass
        else :
            target.great_points += 1 
            while(target.next): 
                if target.next.great_points < target.great_points:
                    #change info
                    target.next.Name,target.Name = target.Name,target.next.Name  
                    target.next.Teacher,target.Teacher = target.Teacher,target.next.Teacher 
                    target.next.Time,target.Time = target.Time,target.next.Time
                    target.next.NTUcourse,target.NTUcourse = target.NTUcourse,target.next.NTUcourse
                    target.next.comment,target.comment = target.comment,target.next.comment
                    target.next.graet_points,target.graet_points = target.graet_points,target.next.graet_points
                    
                    target = target.next
                else:
                    break
    



            
        

            

        
        
        




