import math

class triangleArea:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def Area(self):
    s = (self.a + self.b + self.c) / 2
    area = math.sqrt((s*(s-self.a)*(s - self.b)*(s - self.c)))
    return area

a = int(input("Enter number a = "))
b = int(input("Enter number b = "))
c = int(input("Enter number c = "))
value = triangleArea(a,b,c)
result = value.Area()
print("The triangle area is = ", result)