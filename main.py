s = input()
l = len(s)
m = 0
ind = 0
count = 0
word = ""
maxWordCount = 0;
maxWordUsing = ""
for i in range(l):
    if s[i] != ' ':
        count += 1
    else:
        word = s[i-count:i]
        if s.count(word) > maxWordCount:
            maxWordCount = s.count(word)
            maxWordUsing = word
        if count > m:
            m = count
            ind = i - count
        count = 0


if count > m:
    m = count
    ind = i - count + 1

print("Найдовше слово: "+s[ind:ind + m])
print("Слово з найбільшою кількістю використань: "+maxWordUsing)
