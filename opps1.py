class StringClass:
    def __init__(self):
        self.n= input('enter your string \n')
        print(len(self.n))

    def Con(self,String):
        list1=[]
        list1[1:0]=String
        return list1

obj=StringClass()
str1=obj.n
print(obj.Con(str1))