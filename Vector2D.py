import math

class Vector2D:
    __X = 0
    __Y = 0

    def __init__(self, x, y) -> None:
        self.__X = x
        self.__Y = y

    def GetX(self):
        return self.__X
    def GetY(self):
        return self.__Y

    def AddX(self, x):
        self.__X = self.__X + x
    
    def AddY(self, y):
        self.__Y = self.__Y + y

    def AddVector(self, vectorToAdd):
        self.AddX(vectorToAdd.GetX())
        self.AddY(vectorToAdd.GetY())

    def DistanceTo(self, toVector):
        return math.sqrt((toVector.GetX() - self.GetX())**2 + (toVector.GetY() - self.GetY())**2)
    
    def ToString(self):
        return "("+str(self.__X)+str(self._Y)+")" 