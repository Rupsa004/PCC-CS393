p=float(input("enter the principal amount: "))
r=float(input("enter the interest rate: "))
t=int(input("enter the time period(years): "))
s=(p * t * r) / 100
t1=p+s
a=p * (1 + r / 100)**t
c=a-p
t2=p+c
print("Simple Interest:", s)
print("Total Amount (Simple Interest):", t1)
print("Compound Interest:", c)
print("Total Amount (Compound Interest):", t2)