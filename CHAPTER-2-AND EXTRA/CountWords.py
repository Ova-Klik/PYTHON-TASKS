

vowel=0
consonant=0

word=input("Enter a word: ").lower()

for letter in word:

    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowel+=1
    else:
        consonant += 1

print(f"The number of vowel in word is: {vowel} And the number of Consonants in word is: {consonant}")


