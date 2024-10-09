s=input("enter a string:")
if len(s)>1:
    first,*middle,last=s
    s=last+''.join(middle)+first   
print("modified string",s)
