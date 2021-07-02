class node:
    def __init__(self,data) : ##item type 是list
        self.Name = data[0]
        self.Teacher = data[1]
        self.Time = data[2]
        self.NTUcourse = data[6]
        self.credit=data[3]
        self.comment=''
        self.great_points = int(data[4])
        self.disliked_points = int(data[5])
        self.next=None
        
    def output(self):
        result="課程名稱:"+self.Name+" "+"\n"+"教師姓名:"+self.Teacher+"\n"+"上課時間:"+self.Time+"\n"+"學分:"+' '+self.credit+'讚'+str(self.great_points)+' '+'倒讚'+str(self.disliked_points)+"\n"+"ntu course: "+self.NTUcourse
        if self.comment!='' :
            result+=self.comment+'\n'

        return result

class Linked_list:
    def __init__(self):
        self.root=None
        self.current=None   
    def push(self,item) : #item傳入node
        if not self.root:
            self.root=item
            self.current=item 
        else:
            self.current.next=item 
            self.current=item
    def show(self):
        pointer=self.root
        result=''
        while  pointer:
            result+=pointer.Name+' '+pointer.Teacher+' '+pointer.Time+'讚'+str(pointer.great_points)+' '+'倒讚'+str(pointer.disliked_points)+'\n'
            pointer=pointer.next
        return result


            
            
