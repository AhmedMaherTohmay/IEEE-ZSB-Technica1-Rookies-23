istr = input()
s2 = input()
result = []

def permute(a, i, length):
	if i == length:
		result.append(''.join(a) )
	else:
		for j in range(i, length):
			a[i], a[j] = a[j], a[i]
			permute(a, i + 1, length)
			a[i], a[j] = a[j], a[i]

permute(list(istr), 0, len(istr))
c = (result)
m = 0

for i in range(len(c)):
   if(c[i] in s2):
        print("true")
        m += 1
        break
if(m == 0):
    print("false")
