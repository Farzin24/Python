dict1={}
n1=int(input("how many items in dictionary 1?"))
for i in range(n1):
    key=input("enter key:")
    value=input("enter value:")
    dict1[key]=value
dict2={}
n2=int(input("how many items in dictionary 2?"))
for i in range(n2):
    key=input("enter key:")
    value=input("enter value:")
    dict2[key]=value
merged_dict={**dict1,**dict2}
print("merged dictionary:",merged_dict)

