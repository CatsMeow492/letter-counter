import string 
text = input()
dict = {}
#your code goes here

alphabet = list(string.ascii_lowercase)

for i in range(26):
    letter = alphabet[i] 
    if text.count(letter) != 0:
        dict[letter] = text.count(letter)
        

print(dict)
