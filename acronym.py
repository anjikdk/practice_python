print("Acronym Example")
s = str(input("Enter any String with two words: "))
text = s.split()
acronym = " "

for s1 in text:
    print(s1)
    acronym = acronym+s1[0]

print(acronym)


user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    print(i)
    a = a+i[0]
print(a)
