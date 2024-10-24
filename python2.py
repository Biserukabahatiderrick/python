camel_case=input("enter camel case:")

snake_case=""

for char in camel_case:
    if char.isupper():
        snake_case+="_"+char.lower()
    else:
        snake_case+=char
print("the snake case is ",snake_case)            