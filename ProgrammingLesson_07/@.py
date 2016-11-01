sentence = input("Write a sentence:")
top = 0

while top < sentence.count("a")>0:
    sentence = sentence[0 : sentence.index("a")]+"@"+ sentence[sentence.index("a")+1 :len(sentence)] 
    
    

    
print("You sentence with @'s for a's ......",sentence)
     
