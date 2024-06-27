# def fun1():
#     print("hello world.....")
# fun1() 
   
# -----------nested function-----------

# def outer():
#     print("outer")
#     def inner():
#         print("inner")
#     inner()
# outer()    


# ------closure function--------------
'''
def outer():
    print("outer")
    def inner():
        print("inner")
    return inner
ref=outer()
print(ref)   
ref() 
'''
# --------------decorated functions--------------

def outer(funtion):
    print("outer")
    def inner():
        print("inner")
    return inner
ref=outer()
ref()    

