

word = input("enter a word:")
stop = len(word)
start = 0

def tree(start,stop,word):
    if start <= stop:
        print("{:>20}".format(word[0:start]))
        start = start + 1
        return tree(start,stop,word)

tree(start,stop,word)
        
