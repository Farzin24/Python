def factorial(num):
    if num==0 or num ==1:
        return 1
    else:
        result =1
    for i in range(2,num+1):
        result *=i
    return result

def sum_series(n):
    total=0
    for i in range (1,n+1):
        total +=(i**i)/factorial(i)
    return total
n=int(input("enter the  nnumber of terms:"))
result =  sum_series(n)
print("sum of the series:",result)
