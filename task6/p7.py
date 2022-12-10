import os

def beautifulTriplets(d, arr):
    cnt=0
    for i in arr:
        for j in arr:
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
