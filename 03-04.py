
# the proces of selecting in the elements in list,covert ele into a new elelmts is called mapping

# def fun1(num):
#     return num+10
'''
L=[]
i=0
while(i<=4):
    print("enter a value")
    data=int(input())
    L.insert(i,data)
    i=i+1
K=list(map(fun1,L)) 
print(K) 
'''
'''
K=list(map(lambda num:num+10,L))  
print(K)
# no need of delclere function
'''
'''
def Fun1():
    a=10
    print(a)
    def fun2():
        b=20
        print(a)
        print(b)
    fun2()
    print(a)
    print(b)   
Fun1()     
'''

# def Fun1():
#     a=10
#     print(a)
#     def fun2():
#         a=20
#         b=30
#         print(a)
#         print(b)
#     fun2()
#     print(a)
# Fun1()        


# def Fun1():
#     a=10
#     print(a)
#     def fun2():
#         nonlocal a
#         a=20
#         b=30
#         print(a)
#         print(b)
#     fun2()
#     print(a)
# Fun1()   

# ----------------L E G B Rule-----------

x=10
def outer():
    x=15
    def inner():
        x=20
        print(x)
    inner()    
outer()    