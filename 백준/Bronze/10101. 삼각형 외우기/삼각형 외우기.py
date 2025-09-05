x = int(input())
y = int(input())
z = int(input())

s = x + y + z

if s != 180:
    print("Error")
elif x == y == z:
    print("Equilateral")
elif x == y or x == z or y == z:
    print("Isosceles")
else:
    print("Scalene")
