s = str(input("Enter number: "))
s1 = ''.join(sorted(s))
s2 = s1[::-1]
m = int(int(s2) - int(s1))

for i in range(100):
    if(m == 6174):
        print(i + 1)
        break
    else:
        if (m < 10):
            m = m * 1000
        if (m < 100):
            m = m * 100
        if (m < 1000):
            m = m * 10
        s3 = str(m)
        s4 = ''.join(sorted(s3))
        s5 = s4[::-1]
        m = int(int(s5) - int(s4))