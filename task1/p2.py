#P2 Factorial of number

N = int(input("enter number "))
def fact(n):
    if n <= 1: 
        return n
    else:        
        c = fact(n - 1)
    return n * c

print(fact(N))
