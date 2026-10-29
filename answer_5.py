with open("text.txt", "r") as file:
    text=file.read()
word_count={}
words=text.split()
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print(word_count)
