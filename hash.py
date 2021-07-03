from bs4.element import Tag
import linked_list


class Hash:
    def __init__(self,size):
        self.size=size
        self.table=[linked_list.Linked_list() for i in range(size)]
        

    def insert(self,item):  #item是list
        index=0
        key=item[0].strip()+" "+item[1].strip()
        for i,character  in enumerate(key): #hashing 
            if ord(character)>10000:
                index+=(ord(character)//100)**i
            else:
                index+=ord(character)**i
        index=index%self.size
        print('key= '+key+'index= '+str(index))
        _item=linked_list.node(item)
        self.table[index].push(_item)

    def list_all(self): #只show出基本的info 
        '''
        result=[]
        for i in self.table:
            if i.root:
                print(1)
                result.append(i.show())
        print(result)
        result = ''.join(result)
        return result 
        '''
        all_node = self.get_all_node()
        result = [[],[],[],[],[],[],[],[],[],[],[]]
        for i in all_node:
            sum_ = i.disliked_points - i.great_points
            result[sum_+5].append(i)
    
        result_str = ''
        for i in result:
            for j in i:
                
                result_str += j.Name+' '+j.Teacher+' '+j.Time+'讚'+str(j.great_points)+' '+'倒讚'+str(j.disliked_points)+'\n'
        return result_str

    def search(self,key):
        index=0
        key=str.strip(key)
        print(key)
        for i,character  in enumerate(key): #hashing 
            if ord(character)>10000:
                index+=(ord(character)//100)**i
            else:
                index+=ord(character)**i
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
    
    def clear_comment(self,ctx,classname):
        target=self.search(classname)  #find  the class we want to insert 
        if type(target)==str:
            ctx.send('no such class') 
        else :
            comment_ = target.comment.split("\n")
            comment_ = comment_[:-1]
            print(comment_)
            for i in range(len(comment_)):
                comment_[i] = comment_[i].split(': ') #原先comment_[i] 是 "username: comment"
                print(comment_[i])
                if comment_[i][0] == str(ctx.author):
                    comment_[i] = ' '
                else :
                    comment_[i] = ': '.join(comment_[i])
                    print(comment_[i])
            print(comment_)
            
            for i in comment_ :
                if i == ' ':
                    comment_.remove(i)
            
            
            comment_ = '\n'.join(comment_)
            comment_ = comment_.strip()
            if comment_ :
                target.comment = comment_ + '\n'
            else :
                target.comment = ''
            
    
    def great_points(self,classname):
        great_limit = 5
        target = self.search(classname)
        
        if type(target) == str:
            pass
        else :
            if target.great_points == great_limit:
                pass
            else :
                target.great_points += 1 
    
    def disliked_points(self,classname):
        disliked_limit = 5
        target = self.search(classname)
        
        if target.disliked_points == disliked_limit:
                pass
        else :
            target.disliked_points += 1
    
    def get_all_node(self):
        result=[]
        for i in self.table:
            pointer=i.root
            while pointer:
                result.append(pointer)
                pointer=pointer.next
        return result  
    def save_data(self):
        node_list=self.get_all_node()
        data=open('data.txt','w',encoding='utf-8')
        for node in node_list:
            data.write(node.Name+'!'+node.Teacher+'!'+node.Time+'!'+node.credit+'!'+str(node.great_points)+'!'+str(node.disliked_points)+'!'+node.NTUcourse+'\n')
        data.close()

        
            


    



            
        

            

        
        
        




