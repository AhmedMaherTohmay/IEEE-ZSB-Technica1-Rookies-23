def maxheap(arr, n, i):

	largest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and arr[l] > arr[largest]:
		largest = l

	if r < n and arr[r] > arr[largest]:
		largest = r

	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]

		maxheap(arr, n, largest)

arr = list(map(int, input().split()))

n = len(arr)
n2 = int(len(arr) / 2)

for i in range(n2, -1, -1):
    maxheap(arr, n, i)

for i in arr:
    print(i, end=" ")
