import string 
text = input()
dict = {}

alphabet = list(string.ascii_lowercase)

#Return in order of appearence
for letter in text:
    if alphabet.count(letter) != 0:
        dict[letter] = text.count(letter)
        
print("In order of appearence: ")
print(dict)

dict = {}

#Return in alphabetical order
alphabet = list(string.ascii_lowercase)

for i in range(26):
    letter = alphabet[i] 
    if text.count(letter) != 0:
        dict[letter] = text.count(letter)
        
print("In alphabetical order: ")
print(dict)
