for test in range(int(input())):  # getting every case dynamically

    count, remove = map(int, input().split())
    friends = map(int, input().split())
    s = []
    for i in friends:
        while remove and s and s[-1] < i:  # making sure not get out of range
            s.pop()                        # removing friend after checking 
            remove -= 1

        s.append(i)                              # appending the remaining friends 

    print(' '.join(map(str, s)))

