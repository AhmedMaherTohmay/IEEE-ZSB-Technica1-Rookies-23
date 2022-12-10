l = input()
l = l.split()
n = int(l[0])
m = int(l[1])

p = list(map(int, input().split()))

sec = 86400
day = 0
c = 0
for i in range(n):
    c += sec - int(p[i])
    day += 1
    if(c >= m):
        print(day)
        break

