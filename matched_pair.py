st = input()
stack = []
count = True
open_brackets = ['(', '{', '[']
for element in st:
    if element in open_brackets:
        stack.append(element)
    else:
        if element == ')' and stack[-1] == '(':
            stack = stack[:len(stack)-1]
        elif element == '}' and stack[-1] == '{':
            stack = stack[:len(stack)-1]
        elif element == ']' and stack[-1] == '[':
            stack = stack[:len(stack)-1]
        else:
            count = False
            break
if stack != []:
    count = False
if count:
    print('YES')
else:
    print('NO')
        
