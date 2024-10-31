sentence=input("enter a sentence:")
words=sentence.lower().split()

char_freq={}

for word in words:
    if word in char_freq:
        char_freq[word]+=1
    else:
        char_freq[word]=1
print(char_freq)    

    