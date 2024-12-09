str1=input("enter the frist string:")
str2=input("enter the second string:")
newstr1=str1[0]+str2[1]+str1[2:]
newstr2=str2[0]+str1[1]+str2[2:]
str3=newstr1+" "+newstr2
print(str3)
