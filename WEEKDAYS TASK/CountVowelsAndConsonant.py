string = input("Kindly enter a String: ")

countVowels = 0
countConsonants = 0
capLetter = ' '

for index in range(0, len(string)):
    letter = string[index]

    if ord(letter) >= 97 and ord(letter) <= 122:
        capLetter = chr(ord(letter) - 32)
    else:
        capLetter = letter

    if capLetter == 'A' or capLetter == 'E' or capLetter == 'I' or capLetter == 'O' or capLetter == 'U':
        countVowels += 1
    else:
        countConsonants += 1

print(f"\nVowels in word: {countVowels}")
print(f"Consonants in word: {countConsonants}")
