class Car:
    def __init__(self,paint, interior, tires, engine):
        self.paintP = paint
        self.interiorI = interior
        self.tiresT = tires
        self.engineE = engine
    def setValues(self, newPaint, newInterior, newTires, newEngine):
        self.paintP = newPaint
        self.interiorI = newInterior
        self.tiresT = newTires
        self.engineE = newEngine

    def getPaint(self):
        return self.paintP
    def getInterior(self):
        return self.interiorI
    def getTires(self):
        return self.tiresT
    def getEngine(self):
        return self.engineE

def main():
    paintP = input("What color do you want your paint to be?")
    interiorI = input("What do you want the interior to be?")
    tiresT = input("What kind of tires do you want?")
    engineE = input("What kind of engine do you want?")

    carClass = Car(paintP,interiorI,tiresT,engineE)
    print("Your vechicle is ready........")
    print("Paint:     ", carClass.getPaint())
    print("Interior:  ", carClass.getInterior())
    print("Tires:     ", carClass.getTires())
    print("Engine:    ", carClass.getEngine())

main()
    
