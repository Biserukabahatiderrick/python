text=input("enter text:")

not_vowels=""

vowels="aioueAIOUE"

for char in text:
    if char not in  vowels:
        not_vowels+=char
print("the non vowels are",not_vowels)        


