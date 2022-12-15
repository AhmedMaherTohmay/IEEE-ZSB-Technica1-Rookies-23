n = int(input())
stud = []
for i in range(n):             # getting input
        name = str(input())
        degree = float(input())
        stud.append([name, degree])

for i in range(n - 1):               # comparing each input to sort them
        for j in range(i + 1, n):
            if stud[j][1] < stud[i][1]:
                switch = stud[i]
                stud[i] = stud[j]
                stud[j] = switch

sort = []
sort2 = []
stud.sort
for i in range(1, n):               # appending numbers ecept first one in list
    if stud[i][1] != stud[0][1]:
        last2 = stud[i][1]
        sort.append(stud[i])


for i in range(1, len(sort)):        # comparing them again but this time with second one
    if sort[i][1] == sort[0][1]:     #  as I already deleted the first one
        sort2.append(sort[i][0])

sort2.append(sort[0][0])              # not forgetting to add the second one in case if not 
                                      # finding any similar's
sort2.sort()
for i in range(len(sort2)):
    print(sort2[i])
