# Create a program that will prompt the user for a word, and return a 'word triangle'. For example, if the user types in the word "PYTHON", your program will output:
# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON
word = input("Enter a word: ")
length = len(word)
for row in range(length):
    for col in range(row+1):
        print(word[col], end="")
    print()