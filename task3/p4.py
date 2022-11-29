n = int(input("Enter the number of pages in book: "))
f = int(input("the wanted page: "))
c = 0
if(f % 2 != 0):
    c = ((f - 1) / 2)
else:
    c = (f / 2)
o = n - f + 1
m = 0
if(o % 2 != 0):
    m = ((o - 1) / 2)
else:
    m = (o / 2)
    
if (c > m):
    print(m)
else:
    print(c)