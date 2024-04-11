n = int(input())

og = n
days = 0
hours = 0
minutes = 0
seconds = 0

days,n = n//(24*3600),n%(24*3600)
hours,n = n//(3600),n%(3600)
minutes,n = n//(60),n%(60)
seconds = n
print(days, hours, minutes, seconds)
if og == 0:
    print(f"NOW")
elif og < 60:
    print(f"{seconds} seconds")
elif og < 3600:
    print(f"{minutes} minutes {seconds} seconds")
elif og < 86400:
    print(f"{hours} hours {minutes} minutes {seconds} seconds")
else:
    print(f"{days} days {hours} hours {minutes} minutes {seconds} seconds")