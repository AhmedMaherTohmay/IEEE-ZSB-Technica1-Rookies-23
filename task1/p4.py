#P4 sum of number

N = int(input("enter number "))
def sum(n):
    if n <= 1: 
        return n
    else:        
        c = sum(n - 1)
    return n + c

print(sum(N))