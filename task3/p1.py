n = int(input("Enter the number of matrix: "))
mat = []
print("Enter the matrix: ")

for i in range(n):
	a = list(map(int, input().split()))
	mat.append(a)

c = 0
b = 0
for i in range(n):
    for j in range(n):
        if(i == j):
            c  += mat[i][j]
        if ((i + j) == (n - 1)):
            b += mat[i][j]

m = c - b
if(m > 0):
    print(m)
else:
    print(-m)