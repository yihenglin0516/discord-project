class node:
    def __init__(self,item) : ##item type 是list
        self.value=item
        self.next=None
    def _output(self):
        result=''
        for i in self.value:
            result+=i+' '
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
            l=pointer.value
            result+=l[0]+' '+l[1]+' '+l[2]+'\n'
            pointer=pointer.next
        return result

            
            
