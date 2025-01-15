def is_palindrome(num):
    return str(num) == str(num)[::-1]

numbers=[]

while True:
    n=input("enter a number: ")
    if n.lower()=='q':
        break
    elif n.isdigit():
        numbers.append(int(n))
    else:
        print("enter valid input")
for num in numbers:
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
