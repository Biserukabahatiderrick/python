user_input=input("enter text:")

words=user_input.split(" ")

text_dict={}

for word in words:
    if word in text_dict:
        text_dict[word]+=1
    else:
        text_dict[word]=1
print(text_dict)            








