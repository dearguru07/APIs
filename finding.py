# str="if you think you can or you can't , you aare right"

'''
print(str.count("you"))

str1="you"
print(str1 in  str) ====> True

print(str.find("you")) ===>3

print(str.index("you")) ====>3

print(str.rfind("you")) ====>36

print(str.rindex("you"))  ========>36

print(str.find("virat")) ====>-1


print(str.index("virat")) ====>error

'''


'''-----removing spaces at beginning & ending of the string --- '''

'''
star="      gurucharan     "

srt1=star.rstrip()
print(srt1)

srt2= star.lstrip()
print(srt2)

str3=star.strip()
print(str3)
'''



''' Removeing sapces at middle of the strings '''


# star=input(print("enter the string"))
# newstring=''
# str=star.strip()
# print(str)



star=input(print("enter the string"))
i=0
# print(len(star))
newstr=""
while(i<=len(star)-1):
    data=star[i]
    if(data==" "):
       i=i+1
    else:
        newstr=newstr+data
    i=i+1
print(newstr)          
   
   
   
# ----------string formating--------------
   
# name=input(print("enter the string"))

# print("hi{}".format(name))

# print("name={}".format(name))


