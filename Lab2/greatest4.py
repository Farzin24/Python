numbers=input("Enter integers seperated by spaces:").split()
modified_list=[]
for x in numbers:
    if int(x)>100:
        modified_list.append('Over')
    else:
        modified_list.append(x)
print("Modified List:",modified_list)

