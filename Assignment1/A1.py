years = int(input("Enter the number of years: "))
total_days=0

for i in range(1, years+1):
    
    is_leap_year = (years % 4 == 0 and years% 100 != 0) or (years % 400 == 0)
    if is_leap_year:
        total_days += 366
    else:
        total_days += 365

hours = total_days * 24
minutes = hours * 60
seconds = minutes * 60

print("In" , years , "years:" )
print("total days:" , total_days ,)
print("hours:" ,hours)
print("minutes:", minutes)
print("seconds:" , seconds)

