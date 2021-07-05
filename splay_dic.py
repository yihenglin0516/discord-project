from linked_list import node 

class record():
    def __init__(self):
        self.array = []
    def insert(self,course):
        self.array.append(node(course))

    def search (self, CourseteacherName):
        for i in range(len(self.array)) :
            if self.array[i].Name +' ' + self.array[i].Teacher == CourseteacherName:
                temp = self.array[i]
                self.array.remove(self.array[i])
                self.array.insert(0,temp)

                return self.array[0] #class
            elif i+1 == len(self.array):
                return False
    
    def delete_all(self):
        self.array = []

    def list_all(self):
        self.array_ = str()
        for i in range(len(self.array)) :
            self.array_ += self.array[i].Name + ' ' + self.array[i].Teacher+' '+self.array[i].Time+'\n'
        
        return self.array_ #str





class dictionary():
    def __init__(self):
        self.dic = {}

    def insert(self , course):
        self.dic[course[0]+' '+course[1]] = node(course)

    def search(self,CourseteacherName):
        return self.dic.get(CourseteacherName) #class

    def delete_all(self):
        self.dic = {}
    
    def list_all(self):
        self.array_ =str()
        for i in self.dic.keys():
            self.array_ += self.dic.get(i).Name + ' '+self.dic.get(i).Teacher+' '+self.dic.get(i).Time            
        
        return self.array_ #str
        



        
