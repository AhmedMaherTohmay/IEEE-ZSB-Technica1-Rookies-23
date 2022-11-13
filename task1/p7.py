#p7 palindrome
n = str(input("enter number "))
c = int(len(n)/2) + 1
b = int(len(n))
reverse = n[:: -1]
print(reverse)

def check(n):
    for i in range(0, b):
        if reverse[i] == n[i]:
            continue
        else:
            return 0
        
if check(n) == 0:
    print("no")
else:
    print("yes")

