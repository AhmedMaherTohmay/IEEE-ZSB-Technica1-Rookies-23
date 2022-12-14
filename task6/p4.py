l = input()
l = l.split()
n = int(l[0])
m = int(l[1])

p = [input() for i  in range(n)]  # receving the input
s = []
max = 0

for i in range(len(p)):  # making a loop on topics to add them to each other by using or operator then counting one's to know the people who read the topic
    j = i
    while j < n:
        first = p[i]
        second = p[j]

        b = bin(int(first, 2) | int(second, 2)).count('1')  # after counting I get max 
        if (b > max):
            max = b
        s.append(str(b))

        j += 1

print(max)
print(s.count(str(max)))


