# ------------ control flow of nested function ------------

'''

def ourt():
    print("outer fun")
    def inner():
        print("inner")
        print("process")
        print("leave inner")
    print("leave outer") 
    inner()
ourt()      

'''
#--------------- control flow of closure function-----------
'''
def ourt():
    print("outer")
    def inner():
        print("inner")
        print("process")
        print("leave inner")
    return inner
ref=ourt()
print("calling inner")
ref()
print("end")

   ''' 
#    --------------control flow of decorated function----------    
 
'''

def print_msg():
    print("hello world")
def outer(print1):
    print("outer")
    def inner():
        print("inner")
        ref=print1
        ref()
        print("leave inner")
    return inner 
ptr1=print_msg
ptr2=outer(ptr1)
print("calling inner")
ptr2()
print("prgm end")

'''
#    --------------using decorated function change to upper case-----------     

'''
def print_msg():
    msg="hello world"
    return msg
def outer(data):
    print("outer")
    def inner():
        print("inner")
        ref=data
        msg1=ref()
        msg2=msg1.upper()
        print(msg2)
    return inner 
ptr1=print_msg
ptr2=outer(ptr1)
print("calling inner")
ptr2()
print("prgm end")

'''

def fun1():
    msg="hii my frnd"
    return msg
def outer(data):
    print("hello every one")
    def fun2():
        print("inner")
        print("process")
        ref =data
        msg1=ref()
        msg2=msg1.upper()
        print(msg2)
    return fun2
ptr1=fun1
ptr2=outer(ptr1)
print('calling inner')
ptr2()
print("program will end")    