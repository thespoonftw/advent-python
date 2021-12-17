import math
from days.dayBase import DayBase

def getFuelCost(mass: int) -> int:
    return math.floor(mass / 3) - 2

def getRecursiveFuelCost(mass: int) -> int:
    x = math.floor(mass / 3) - 2
    if x < 0:
        return 0
    else:
        return x + getRecursiveFuelCost(x)

class Day01(DayBase) : 

    def PartOne(self) -> int:
        counter = 0
        for line in self.data:
            x = getFuelCost(int(line))
            counter += x
        return counter

    def PartTwo(self) -> int:
        counter = 0
        for line in self.data:
            x = getRecursiveFuelCost(int(line))
            counter += x
        return counter

