l = input()
l = l.split()
n = int(l[0])
m = int(l[1])

p = [input() for i  in range(n)]
s = []
max = 0

for i in range(len(p)):
    j = i
    while j < n:
        first = p[i]
        second = p[j]

        b = bin(int(first, 2) | int(second, 2)).count('1')
        if (b > max):
            max = b
        s.append(str(b))

        j += 1

print(max)
print(s.count(str(max)))


