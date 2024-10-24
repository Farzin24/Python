n=int(input("enter the number to find its factors :"))
i=1
print(f"factors of {n} are:")
while i<=n:
    if n % i==0:
        print(i)
    i +=1
