arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
p = []
d, m, y = 0, 0, 0
for i in reversed(range(3)): # substracting to get the remaining days, months and years
    c = arr1[i] - arr2[i]
    p.append(c)

if(p[0] > 0):                   # Instead of using for loops I just made it manually (:
    print(int(p[0]) * 10000)
else:
    y += 1

if(p[1] > 0 and p[0] == 0):
    print(int(p[1]) * 500)
else:
    m += 1

if(p[2] > 0 and p[1] == 0 and p[0] == 0):
    print(int(p[2]) * 15)
else:
    d += 1

if(m == 1 and y == 1 and d == 1):
    print("0")
