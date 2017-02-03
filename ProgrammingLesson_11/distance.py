

class MilesPerHour:
    def __init__(self, distance, hours, minutes):
        self.distanceD = distance
        self.hoursH = hours
        self.minutesM = minutes
        mph = 0
    def setValues(self, newDistance, newHours, newMinutes):
        self.distanceD = newDistance
        self.hoursH = newHours
        self.minutesM = newMinutes

        mph = 0

    def getDist(self):
        return self.distanceD
    def getHours(self):
        return self.hoursH
    def getMin(self):
        return self.minutesM
    def getMPH(self):
        mph = self.distanceD / (self.hoursH)
        return mph
    

def main():
    distanceD = int(input("How far did you go?"))
    hoursH = int(input("How long did it take in hours?"))
    minutesM = int(input("How long did it take in minutes?"))

    milesPerHour = MilesPerHour(distanceD,hoursH,minutesM)
    print(milesPerHour.getDist(), "miles in ", milesPerHour.getHours(), "hours = ", milesPerHour.getMPH(),"mph")
main()



    
    
    
    
        
    
    
