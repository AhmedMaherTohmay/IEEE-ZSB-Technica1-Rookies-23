string = "hello"
p = input("Enter a string")
i = 0
j = 0
while i < len(string) and j < len(p):
    if string[i] == p[j]:
        i += 1
    j += 1
if i == len(string):
    print("YES")
else:
    print("NO")