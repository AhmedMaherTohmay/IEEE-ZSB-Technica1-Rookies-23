lower = int(input().strip())  
higher = int(input().strip())
result = []
sum1 = 0
for i in range(lower, higher + 1):
    split = []
    sq = i * i           
    arr = str(sq)
    length = len(arr) // 2
    if length == 0:
        split = arr
    else:
        split.append(arr[0 : length]) # appending the d digits in list
        split.append(arr[length : ])  # and the other d digits in the list
    split = map(int, split) 
    sum1 = sum(split)              # summing digits after appending them
    if sum1 == i:                 # checking the kaprekar condition
        result.append(i)
if result:
    print(' '.join(map(str, result)))
else:
    print("INVALID RANGE")

