N = int(input())
meio = N//2

for i in range(N):
    if i%5 == 0:
        if i <= meio:
            print(N//meio)
        else:
            print(i)