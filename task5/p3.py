n = str(input())

b = 0
while(b != 1 and b != 4):
    b = 0
    for i in range(len(n)):
        b = b  + (int(n[i]) * int(n[i]))
    n = str(b)



if(b == 1):
    print("true")
if(b == 4):
    print("false")