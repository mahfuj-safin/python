class Number:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def largest(self):

    if self.a >= self.b and self.a >= self.c:
      return f"The largest number is: {self.a}"

    elif self.b >= self.a and self.b >= self.c:
      return f"The largest number is: {self.b}"
    else:
      return f"The largest number is: {self.c}"

    
a = int(input("Enter number a = "))
b = int(input("Enter number b = "))
c = int(input("Enter number c = "))
value = Number(a,b,c)
result = value.largest()
print(result)