
word = input("Enter a word:")
word2 = input("Enter another word:")
word3 = input("Enter another word:")

def makeCenter(word):
    if len(word) >= 20:
        return word
    else:
        return makeCenter(" " + word + " ")

print(makeCenter(word))
print(makeCenter(word2))
print(makeCenter(word3))
