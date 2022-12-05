li = []
a = list(input())


for i in a:

    if i in ['(', '{', '[']:
        li.append(i)
    elif i == ')' and li[-1] == '(':
        li.pop()
    elif i == '}' and li[-1] == '{':
        li.pop()
    elif i == ']' and li[-1] == '[':
        li.pop()
    else:
        li.append(i)

if len(li) == 0:
    print("True")
else: print("False")


