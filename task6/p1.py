t = int(input())
while (t > 15 or t < 1):
    t = int(input())    # making sure that input dosen't exceed 15

p = []
c = 0
for i in range(t):  # receving numbers
    arr = str(input())
    n = int(arr)
    for i in range(len(arr)):
        if(int(arr[i]) == 0): #skipping zero's to avoid proplems
            continue
        else:
            if(n % int(arr[i]) == 0): # divisor
                c += 1
    p.append(c) #appending results
    c = 0

for i in range(len(p)): # printing result
    print(p[i])

