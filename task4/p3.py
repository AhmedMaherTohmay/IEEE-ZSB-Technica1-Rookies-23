arr = list(map(int, input().split()))
li = []
c = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if(arr[i] == arr[j]):
            c = (j - i)
            li.append(c)


print(min(li))
print(li)
