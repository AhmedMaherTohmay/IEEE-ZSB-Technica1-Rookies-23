arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
m = len(arr2)
li = []

if(arr1[0] < arr1[1]):
    c = (int(arr1[1]) // int(arr1[0])) * int(arr1[0])   # if the rotation count is bigger than the elements in integar array 
    b = arr1[1] - c                                     # we do this equation to get the wanted rotation 
else:                                                   # we do the samething  when we get the angle after rotating many times
    b = arr1[1]

for i in range(arr1[2]):
    arr3 = str(input())
    li.append(arr3)

z = m - b
p = []

for i in range(z , m):          # (1 , 2 , 3)  append ( 2, 3)
    p.append(arr2[i])

for i in range(0 , z):           # append (1) 
    p.append(arr2[i])


for i in range(len(li)):        # print the final list
    print(p[int(li[i])])

