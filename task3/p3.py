n = int(input("Enter the number of bottles: "))
while n < 1:
    n = int(input("Enter the number of bottles: "))
    
bottles = []
print("Enter the bottles: ")
i = 0
bottles = []
for i in range(n):
    bottles.append(input().split(" "))
        
for i in range(n - 1):
        for j in range(i + 1, n):
            if bottles[j][1] < bottles[i][1]:
                switch = bottles[i]
                bottles[i] = bottles[j]
                bottles[j] = switch

f = 0
c = 0
for i in range(n):
        f += int(bottles[i][0])
c += int(bottles[n - 1][1]) + int(bottles[n - 2][1])

if(c > f):
    print("yes")
else:
    print("no")