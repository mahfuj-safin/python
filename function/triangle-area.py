# triangle area 

import math
def triangle_area(a, b, c):
  if (a+b) > c and (b+c) > a and (a + c) > b:
      s = (a + b + c) / 2
      area = math.sqrt(s*(s-a)*(s-b)*(s-c))
  return area

# input
a = float(input("Enter sides a: "))
b = float(input("Enter sides b: "))
c = float(input("Enter sides c: "))
result = triangle_area(a, b, c)
print(result)