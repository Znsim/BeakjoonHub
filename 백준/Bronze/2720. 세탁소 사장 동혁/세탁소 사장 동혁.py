#c = {'Q':25,'D':10,'N':5,'P':1} 
c = [25,10,5,1]
n = int(input())

for i in range(n):
    t = int(input())

    re = []

    for coin in c :
        re.append(t//coin)
        t %= coin

    print(*re)