class node:
    def __init__(self,data) : ##item type 是list
        self.Name = data[0]
        self.Teacher = data[1]
        self.Time = data[2]
        self.NTUcourse = data[3]
        self.comment=''
        self.graet_points = 0
        self.next=None
        
    def output(self):
        result=self.Name+' '+self.Teacher+' '+self.Time+'\n'+self.NTUcourse+'\n'
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
            result+=pointer.Name+' '+pointer.Teacher+' '+pointer.Time+pointer.great_points+'\n'
            pointer=pointer.next
        return result

            
            
