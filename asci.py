# print("enter a charc")
# str=input()
# Asciiv=ord(str)
# print(Asciiv)



# print(int(input("enter the chara")))
# str=input()
# Asciiv=chr(str)
# print(Asciiv)


# print("enter the chart")
# string=input("R")
# Ascii=ord(string )
# print(Ascii+32)

# print("enter the chara")
# str=input(a)
# AsciiV=ord(str )
# print(AsciiV)

# print("enter the chacr")
# strin=input("M")
# AsciiVa=ord(strin )
# print(AsciiVa+32)

# print("enter the charx")
# stringu=input("u")
# Asciival=ord(stringu )
# print(Asciival)


#  --------------UpperCase to LoweCase---------------

'''
print("enter a string")
str=input()

i=0
newStr=""

while (i<=len(str)-1) :
    data=str[i]
    Asciiv=ord(data)
    if (Asciiv>=65  and Asciiv<=90):
        newAscii=Asciiv+32
        convr=chr(newAscii)
        newStr=newStr+convr
    else:
        newStr=newStr+data
    i=i+1
print(newStr)    
        '''
        
        
# --------------LoweCase to UpperCase-------------    
        
        
# print("enter the name")
str=input(print("enter the name"))
i=0
newStr=""
while (i<len(str)):
    data=str[i]
    Asciiv=ord(data)
    if(Asciiv>=97 and Asciiv<=122):
        newAscii=Asciiv-32
        convstr=chr(newAscii)
        newStr=newStr+convstr
    else:
        newStr=newStr+data
    i=i+1
print(newStr)               

