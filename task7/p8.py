arr1 = str(input())
arr2 = []
i = 0
while i < len(arr1):
    if(arr1[i] == '.'):
        arr2.append('0')
    elif(arr1[i] == '-'and arr1[i+1] == '.'):
        arr2.append('1')
        i += 1
    else:
        arr2.append('2')
        i += 1
    i +=1
print(''.join(arr2))