
import math

class QuadraticEquation:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def find_roots(self):
    discriminant = self.b**2 - 4*self.a*self.c

    if discriminant > 0:
      root1 = (-self.b + math.sqrt(discriminant)) / (2*self.a)
      root2 = (-self.b - math.sqrt(discriminant)) / (2*self.a)

      return root1, root2

    elif discriminant ==0:
      root = -self.b / (2*self.a)
      return root

    else:
      return "No real roots"


equation = QuadraticEquation(2, 6, 3)
result = equation.find_roots()

print("Roots:", result)