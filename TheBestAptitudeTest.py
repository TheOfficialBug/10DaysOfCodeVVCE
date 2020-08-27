import numpy as np
q = input()
for _ in range(int(q)):
    input()
    gpa = list(map(float, input().split()))
    max_coef = 0
    for i in range(5):
        xs = list(map(float, input().split()))
        coef = np.corrcoef(gpa, xs)[0, 1]
        if coef > max_coef:
            max_coef = coef
            max_i = i
    print(max_i + 1)