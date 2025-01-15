
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))


def is_magic_number(num):
    while num >= 10:
        num = sum_of_digits(num) 
    return num == 1  


num = int(input("Enter a number: "))


if is_magic_number(num):
    print(f"{num} is a magic number.")
else:
    print(f"{num} is not a magic number.")
