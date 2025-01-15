n = int(input("Enter the number of rows: "))

def print_row(i, n):
    spaces = " " * (n - i)
    numbers = "".join(str(j) for j in range(1, i + 1)) + "".join(str(j) for j in range(i - 1, 0, -1))
    print(spaces + numbers)


for i in range(1, n + 1):
    print_row(i, n)


for i in range(n - 1, 0, -1):
    print_row(i, n)
