arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
m = len(arr2)
li = []

if(arr1[0] < arr1[1]):
    c = (int(arr1[1]) // int(arr1[0])) * int(arr1[0])
    b = arr1[1] - c
else:
    b = arr1[1]

for i in range(arr1[2]):
    arr3 = str(input())
    li.append(arr3)

z = m - b
p = []

for i in range(z , m):
    p.append(arr2[i])

for i in range(0 , z):
    p.append(arr2[i])


for i in range(len(li)):
    print(p[int(li[i])])

