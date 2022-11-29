string = str(input("Enter a number  "))
p = ""
for i in string:
	if i not in p:
		p = p + i
print(p)
