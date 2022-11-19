points = int(input()), int(input()), int(input())
points = sorted(points)

if points[2] < points[0] + points[1]:
    print('YES')
else:
    print('NO')
