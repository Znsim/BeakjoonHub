paper = []

for i in range(100):             # 세로로 100줄 만들기
    row = []                     # 각 줄(행)을 만들 리스트
    for j in range(100):         # 가로로 100칸 만들기
        row.append(0)            # 0으로 초기화
    paper.append(row)            # 완성된 줄을 도화지에 추가

n = int(input())

for i in range(n):
    x, y = map(int,input().split())
    for j in range(10):
        #print("y값:", y+j)
        for k in range(10):
            #print("y값 x값:", y+j, x+k)
            paper[y+j][x+k] = 1 #(x,x+10)
        #print("-----------")
        #(y+=1)

cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1

print(cnt)

