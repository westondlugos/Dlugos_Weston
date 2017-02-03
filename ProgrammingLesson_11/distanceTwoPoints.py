
import math

class distance:
    def __init__(self, x1, y1, x2, y2):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2
        self.distance = 0
    def setValues(self,newX1, newY1, newX2, newY2):
        self.xOne = newX1
        self.yOne = newY1
        self.xTwo = newX2
        self.yTwo = newY2
        self.distance = 0

    def getMPH(self):
        self.distance = math.sqrt((self.xTwo - self.xOne)*(self.xTwo - self.xOne)+(self.yTwo - self.yOne)*(self.yTwo-self.yOne));
        return self.distance
    def getx1(self):
        return self.xOne
    def gety1(self):
        return self.yOne
    def getx2(self):
        return self.xTwo
    def gety2(self):
        return self.yTwo
   
    
def main():
    xOne = int(input("Enter an x coordinate:"))
    yOne= int(input("Enter another x coordinate:"))
    xTwo = int(input("Enter a y coordinate:"))
    yTwo = int(input("Enter another y coordinate:"))

    new = distance(xOne, yOne, xTwo, yTwo)

    print("The distance between x1 and x2 is:",new.getMPH(),"and the distance between y1 and y2 is:",new.getMPH())
main()
    
    
 
    
        
        
