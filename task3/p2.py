n = int(input("Enter number of students: "))
print("Enter the students names and their degrees: ")
stud = []
for i in range(n):
        name = str(input())
        degree = float(input())
        stud.append([name, degree])

for i in range(n - 1):
        for j in range(i + 1, n):
            if stud[j][1] < stud[i][1]:
                switch = stud[i]
                stud[i] = stud[j]
                stud[j] = switch
last2 = 0
sort = []
for i in range(n):
    if stud[i][1] == stud[1][1]:
        last2 = stud[i][1]
        sort.append(stud[i])

sort.sort()
for i in range(len(sort)):
    print(sort[i][0])

