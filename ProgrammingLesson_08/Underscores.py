sentence = input("Write a sentence:")

def replace(sentence):
    if sentence.count(" ") > 0:
        return replace(sentence[0 : sentence.index(" ")]+"_"+ sentence[sentence.index(" ")+1 :len(sentence)])
    else:
        return sentence

print(replace(sentence))
        
