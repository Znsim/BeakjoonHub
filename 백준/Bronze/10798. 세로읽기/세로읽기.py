n = []

for i in range(5):
    n.append(list(input())) 


for i in range(15):  
    for j in range(5):  
        if i < len(n[j]):  
            print(n[j][i], end='')
