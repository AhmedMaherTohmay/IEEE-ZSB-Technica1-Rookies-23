def rotate(A):
	N = len(mat)
	for i in range(N // 2):
		for j in range(i, N - i - 1):
			temp = mat[i][j]
			mat[i][j] = mat[N - 1 - j][i]
			mat[N - 1 - j][i] = mat[N - 1 - i][N - 1 - j]
			mat[N - 1 - i][N - 1 - j] = mat[j][N - 1 - i]
			mat[j][N - 1 - i] = temp

def printmat(mat):
	N = len(mat)
	print(N)
	for i in range(N):
		print(mat[i])

n = int(input("Enter the number of matrix: "))
mat = []
print("Enter the matrix: ")

for i in range(n):
	a = list(map(int, input().split()))
	mat.append(a)

rotate(mat)
printmat(mat)
