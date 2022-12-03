n = int(input("Enter the number of the string: "))
k = int(input("frequent numbers wanted: "))
arr = input("Enter array: ").split()

for i in range(n):
    arr[i] = int(arr[i])

narr = [0]*(max(arr) + 1)
for i in arr:
    narr[i]+=1

index = 0
for i in range(k):
    print(narr.index(max(narr)) , end = " ")
    narr[narr.index(max(narr))] = 0