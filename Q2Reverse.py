# Create a program that will accept a word and output the word one letter at a time in reverse.
word = input("Enter a word: ")
for i in range(len(word)-1,-1,-1):
    print(word[i])