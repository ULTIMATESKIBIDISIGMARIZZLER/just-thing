e=input("dic")
words=e.lower().split()
words_count={}

for word in words:
    if word in words_count:
        words_count[word]+=1
    else:
        words_count[word]=1

sort=list(words_count.items())

for i in range(len(sort)):
    for j in range(0, len(sort)-i-1):
        if sort[j][1]<sort[j+1][1]:    
           sort[j],sort[j+1]=sort[j+1],sort[j]

top5=sort[:5]
top10=sort[:10]

print("top 5 words", top5)
print("top 10words", top10)