n = int(input())
string = "hackerrank"
u = []

for x in range(n):
    p = input()
    c, i, j = 0, 0, 0
    while i < len(string) and j < len(p):
        if string[i] == p[j]:
            i += 1
        j += 1
    u.append(i)

for i in range(len(u)):
    if int(u[i]) == len(string):
        print("YES")
    else:
        print("NO")

