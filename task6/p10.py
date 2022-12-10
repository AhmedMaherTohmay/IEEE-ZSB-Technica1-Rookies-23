for test in range(int(input())):

    count, remove = map(int, input().split())
    friends = map(int, input().split())
    s = []
    for i in friends:
        while remove and s and s[-1] < i:
            s.pop()
            remove -= 1

        s.append(i)

    print(' '.join(map(str, s)))

