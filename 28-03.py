'''
str=input(print("enter a name"))
if(str.isalpha()):
    print("str have only chara")
if(str.isdigit()):
    print("only digits")
if(str.isalnum()):
    print("both are in str")       
    
    '''
    
'''    
str="dinesh"
# print(str)    
str1=str.replace("h","z")
print(str1)


srting="rangaswqami"
str=srting.replace("i","w")
print(str)

'''

# class Farmer():
#     def __init__(self,p,t,r):
#         self.p=p
#         self.t=t
#         self.r=r
#     def disp(self):
#         s1=(self.p*self.t*self.r)/100
#         print(s1)
# f1=Farmer(100000,2,2.5)    
# f1.disp()
    
        
'''  
class Farmer:
    r=2.5
    def __init__(self,p,t):
        self.p=p
        self.t=t
        # self.r=r
    def disp(self):
        s1=(self.p*self.t*self.r)/100
        print(s1)
f1=Farmer(100000,2)    
f1.disp()          

'''


# class Farmer:
#     def __init__(self,p,t,r):
#         self.p==p
#         self.t==t
#         self.r==r
# s1=Farmer((10000,2,2)*100)
# print(s1)       



# ------------------Actual & Formal parameters----------

class Demo():
    def disp(self,x,y):
        temp=x
        x=y
        y=temp
        
d=Demo()
a=10
b=20
print("before swapping")
print(a)
print(b)
d.disp(a,b)
print("after swapping")
print(a)
print(b)           


# -------------------swapping the two nubers-------------

x=int(input("enter a number"))
y=int(input("enter a number"))
x,y=y,x
print("x=",x)
print("y=",y)
