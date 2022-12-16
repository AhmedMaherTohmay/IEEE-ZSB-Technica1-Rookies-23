import os

def chocolateFeast(n, c, m):
    p = int(n / c)       # getting number of choclats he can buy
    wrapp = choco = p
    while wrapp >= m:     # getting how many time he can wrap
        wrapp -= (m-1)    # by substacting (wrap - 1) from chocolats  
        choco += 1
    return choco 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
