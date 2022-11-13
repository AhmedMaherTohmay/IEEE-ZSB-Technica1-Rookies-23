#P6  The greatest common divisor (GCD) of two or more integers

A = int(input("enter number "))
B = int(input("enter number "))
if A > B:
    C = A % B
    if B % C == 0:
        print(C)
    else:
        print(B % C)
else:
    C = B % A
    if A % C == 0:
        print(C)
    else:
        print(A % C)
