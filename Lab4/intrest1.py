def calc_interest(principal,time,is_Senior):
    rate=12 if is_Senior else 10
    interest=(principal*rate*time)/100
    return interest
principal=float(input("enter the principal amount:"))
time=float(input("enter the time (in years):"))
is_Senior=input("is the customer a senior citizen?(Y/N):").strip().lower()=="Y"
interest=calc_interest(principal,time,is_Senior)
print(f"the calculated interest is:{interest}")

