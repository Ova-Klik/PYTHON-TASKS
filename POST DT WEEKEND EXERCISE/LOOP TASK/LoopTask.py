
string = "Kashamadupe"
reversed_string=""
space = len(string)
for char in range(len(string)-1,-1,-1):
    reversed_string = reversed_string + string[char]
print(f"{reversed_string}")


