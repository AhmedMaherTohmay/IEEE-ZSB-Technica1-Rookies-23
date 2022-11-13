#P5 sum of number

N = int(input("enter number "))
c = 0
for i in range(1 , N + 1):
    if i % 5 == 0 or i % 3 == 0:
        c = c + i
print(c)
