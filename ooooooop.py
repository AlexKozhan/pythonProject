class Super_Car(Easy_Car):
    def __init__(self, color, mark, size, wheel_size):
        super().__init__(color, mark, size)
        self.wheel_size = wheel_size
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color
    def getMark(self):
        return self.mark
    def setMark(self, mark):
        self.mark = mark
    def getSize(self):
        return self.size
    def setSize(self, size):
        self.size = size
    def getWheel_size(self):
        return self.wheel_size
    def setWheel_size(self, wheel_size):
        self.wheel_size = wheel_size
    def c(self):
        print(self.color, self.mark, self.size, self.wheel_size)
    def __str__(self):
        return f"{self.color}{self.mark}{self.size}{self.wheel_size}"
obj3 = Super_Car("White", "BMW", "140sm", "13")