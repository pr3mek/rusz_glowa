phrase = "Podaj jajko!"
plist = list(phrase)
print(phrase)
print(plist)

remove_list = ['P', 'a', 'j', 'k']

for letter in remove_list:
    if letter in plist:
        plist.remove(letter)

for i in range(2):
    plist.pop(len(plist) - 1)


new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
