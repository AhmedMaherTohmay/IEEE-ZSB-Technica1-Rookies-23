t = int(input())
while (t > 15 or t < 1):
    t = int(input())

p = []
c = 0
for i in range(t):
    arr = str(input())
    n = int(arr)
    for i in range(len(arr)):
        if(int(arr[i]) == 0):
            continue
        else:
            if(n % int(arr[i]) == 0):
                c += 1
    p.append(c)
    c = 0

for i in range(len(p)):
    print(p[i])

