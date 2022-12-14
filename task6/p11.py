l = input()
l = l.split()
n = int(l[0])
m = int(l[1])

p = list(map(int, input().split()))

sec = 86400
day = 0
c = 0
for i in range(n):              # consider she want 2 sec to read the book and we have 1 sec in the first day
    c += sec - int(p[i])        # and 1 sec in the other day to know the wanted days we add the second's of each day 
    day += 1                    # then compare it with wanted seconeds 
    if(c >= m):
        print(day)
        break

