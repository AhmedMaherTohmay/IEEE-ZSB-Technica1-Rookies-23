n = int(input())
string = "hackerrank"
u = []

for x in range(n):
    p = input()
    c, i, j = 0, 0, 0
    while i < len(string) and j < len(p): # finding every alphabet in hackerrenk in the given string then appending it into list
        if string[i] == p[j]:
            i += 1
        j += 1
    u.append(i)

for i in range(len(u)):  # comparing the result list with hackerrank to  see if it matches
    if int(u[i]) == len(string):
        print("YES")
    else:
        print("NO")

