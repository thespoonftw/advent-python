import math
from days.dayBase import DayBase

def Compute(input: str, noun: int, verb: int) -> int:
    split = input.split(',')
    values = list(map(int, split))
    values[1] = noun
    values[2] = verb
    indexer = 0
    while True:
        opcode = values[indexer]

        if opcode == 1:
            a = values[values[indexer + 1]]
            b = values[values[indexer + 2]]
            values[values[indexer + 3]] = a + b

        elif opcode == 2:
            a = values[values[indexer + 1]]
            b = values[values[indexer + 2]]
            values[values[indexer + 3]] = a * b

        elif opcode == 99:
            break

        indexer += 4
    #print(",".join(map(str, values)))
    return values[0]

class Day02(DayBase) : 

    def PartOne(self) -> int:
        return Compute(self.data[0], 12, 2)

    def PartTwo(self) -> int:
        returner = 0
        requiredOutput = 19690720
        for x in range(100):
            for y in range(100):
                if Compute(self.data[0], x, y) == requiredOutput:
                    returner = x * 100 + y
                    break
                
        return returner

