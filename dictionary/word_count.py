#wordcount

txt="hai hai hai hello hello hai hello"

words=txt.split(" ")

word_count={}

for w in words:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)
print(max(word_count))
