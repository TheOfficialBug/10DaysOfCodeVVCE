n = int(input())

ar = []
for i in range(n):
    if i < n//2:
        numX, striX = input().strip().split()
        ar.append((int(numX),'-'))
    else:
        numX,striX = input().strip().split()
        ar.append((int(numX),striX))

ar.sort(key=lambda tup: tup[0])
print(*[x[1] for x in ar])