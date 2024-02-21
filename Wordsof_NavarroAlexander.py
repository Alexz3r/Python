#Navarro ALexander john V.
#BSCS 2-A

phrase = input("Type in: ")
phrase_splited = phrase.split(' ')

word_list = []
for i in phrase_splited:
    if i not in word_list:
        word_list.append(i)
    else:
        continue
word_list.sort()
print((' ').join(word_list))

