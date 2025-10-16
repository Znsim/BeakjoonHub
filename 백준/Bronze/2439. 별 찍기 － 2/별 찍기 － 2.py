N = int(input())

for i in range(1, N+1):
    print(" " * (N - i) + "*" * i)  # 공백 (N-i)개 + 별 i개
