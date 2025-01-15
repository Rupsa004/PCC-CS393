num = int(input("Enter a number: "))
r = int(str(num)[::-1])
print("Reversed number:", r)
if r%2==0:
    print("num is even")
else:
    print("num is odd")

