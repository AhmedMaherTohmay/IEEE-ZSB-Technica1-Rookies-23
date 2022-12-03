n = int(input("Enter number of list: "))
i = n
for i in range(n):
 li = list(input("Enter the list: ").split())
m = int("".join(li)) + 1
s = str(m)
for i in s:
    print(i , end = " ")
