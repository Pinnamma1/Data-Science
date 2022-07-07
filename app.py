class calculater:
    def __init__(self,a=0,b=20):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def subtraction(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
obj = calculater(a=2,b=3)
print(f'This is Addition {obj.addition()}')
