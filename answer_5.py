file = open("text.txt1", "r")
text=file.read()
file.close
word_count={}
word=text.split()
for i in word:
    if i in word_count:
        word_count[i] +=1
    else:
        word_count[i]=1
print(word_count)
