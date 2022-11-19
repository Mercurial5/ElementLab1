n = int(input())

breaks = n - 1
breaks1 = 5 * ((breaks // 2) + (breaks % 2))
breaks2 = 15 * (breaks // 2)

minutes = 45 * n + breaks1 + breaks2

hours = (minutes // 60)
print(9 + hours, (minutes - hours * 60))
