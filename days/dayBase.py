import os

class DayBase:

    def PartOne(self) -> int:
        return 0
    
    def PartTwo(self) -> int:
        return 0

    def LoadTest(self) -> list[str]:
        num = self.__class__.__name__[-2:]
        with open(os.getcwd() + '\\data\\test' + num + '.txt') as f:
            return f.readlines()

    def LoadInput(self) -> list[str]:
        num = self.__class__.__name__[-2:]
        with open(os.getcwd() + '\\data\\input' + num + '.txt') as f:
            return f.readlines()

    def __init__(self):
        print("====== " + self.__class__.__name__ + " ======")
        test = self.LoadTest()
        input = self.LoadInput()
        self.data = test
        print("Part One Test: " + str(self.PartOne()))
        self.data = input
        print("Part One Input: " + str(self.PartOne()))
        self.data = test
        print("Part Two Test: " + str(self.PartTwo()))
        self.data = input
        print("Part Two Input: " + str(self.PartTwo()))

