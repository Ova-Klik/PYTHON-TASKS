words = input("Kindly enter a Word: ");

reversed_word="";

for word in range(len(words)-1,-1,-1):
   
    reversed_word+=words[word];
        
print ("Reversed word is: " + reversed_word)
