grid = []

for i in range(3):
    grid.append(list(map(int, input().split())))

row, column = 5,5      # Making a 5x5 null matirx
arr = [[0 for i in range(column)] for j in range(row)]

for i in range(1,4):                # Handling edge cases
    for j in range(1,4):
        arr[i][j] = grid[i-1][j-1]   # modifying null matrix to fit the grid matrix in the center


for i in range(1,4):                      # if the sum of the element and its nearest neighbor elements is 1
    for j in range(1,4):                   # then the light at that element will be OFF '0'
        if sum([arr[i][j-1], arr[i][j+1], arr[i-1][j], arr[i+1][j]], arr[i][j]) % 2:
            print('0', end='')
        else:                                  # else it will be ON '1'
            print('1', end='')
    print()
