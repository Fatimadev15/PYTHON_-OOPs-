class Triangle:
    __count = 0

    def __init__(self, a, b, c):
        self.__sideA = a
        self.__sideB = b
        self.__sideC = c
        Triangle.__count += 1

    @classmethod
    def default (cls):
        return cls(1.0,1.0,1.0)
    # for_one parameter
    @classmethod
    def equilateral(cls,x):
        return cls(x,x,x)
    # for_two parameter
    @classmethod
    def isosceles(cls,x,y):
        return cls(x,x,y)
    # for clone
    @classmethod
    def from_existing(cls, triangle):
        return cls(triangle.sideA, triangle.sideB, triangle.sideC)
    
    @property
    def sideA(self):
        return self.__sideA
    @sideA.setter
    def sideA(self,value):
        self.__sideA = value
    @property
    def sideB(self):
        return self.__sideB 
    @sideB.setter
    def sideB(self,value):
        self.__sideB = value
    @property
    def sideC(self):
        return self.__sideC
    @sideC.setter
    def sideC(self,value):
        self.__sideC = value

    # for object count

    @classmethod
    def object_count(cls):
        return cls.__count 

    def perimeter(self):
        return self.__sideA + self.__sideB + self.__sideC 
    def is_right_angled(self):
        sides = sorted([self.__sideA, self.__sideB, self.__sideC])
        return abs((sides[0]**2 + sides[1]**2) - sides[2]**2) < 0.0001

    def __str__(self):
        return f"Triangle with sides {self.__sideA}, {self.__sideB}, {self.__sideC}"