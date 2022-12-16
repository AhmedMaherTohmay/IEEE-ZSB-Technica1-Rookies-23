old = int(input())  # this code is in case the old number is 1000 <= old <= 9000
while True:
    old += 1
    a = int(old / 1000)
    b = int(old / 100 % 10)
    c = int(old / 10 % 10)
    d = int(old % 10)
    if ((a != b) and (a != c) and (a != d) and (b != c) and (b != d) and (c != d)):
        break
print(old)

"""old = int(input())    # this code works for evry condition but takes a longer time):
while True:
    old += 1
    arr = str(old)
    for i in range(len(arr)): 
        for j in range(len(arr)):
            if(int(arr[i]) == int(arr[j])):
                continue
            else:
                break

print(old)"""

