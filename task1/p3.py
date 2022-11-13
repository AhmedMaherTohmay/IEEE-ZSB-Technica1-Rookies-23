#p3 sum of list

list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    c = int(input())
    list.append(c)
    
c = 0
for y in list:
    c = c + y
print(c) 

b = 0
i = 0
while i < len(list):
    
    b = b + list[i]
    i = i + 1
print(b)
  
def sum(list):
    if len(list) == 0:
       return 0
    else:
       return list[0] + sum(list[1:])

print(sum(list))
