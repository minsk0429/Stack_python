from ArrayStack import ArrayStack
s = ArrayStack(100)

msg = input("Enter a string: ")
for c in msg:
    s.push(c)

print("Reversed string is: ", end='')
while not s.isEmpty():
    print(s.pop(), end='')
print()