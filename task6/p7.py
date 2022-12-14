import os

def beautifulTriplets(d, arr):
    cnt=0
    for i in arr:                     # if d = 2 and the substract of two elemts is eual to d (3 - 1 = 2) propaply their are triplets    
        for j in arr:                 # to make sure we add d to the seconed element ( 3 + 2 = 5 ) and search for it (5)
            if(j - i == d):
                if((j + d) in arr):
                    cnt += 1           
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
