n = int(input())
x = []
y = []

for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

here_x = max(x) - min(x)
here_y = max(y) - min(y)

print(here_x * here_y)