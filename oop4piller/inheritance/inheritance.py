class Animal:
  def eat (self):
    print("Animal is eating")

class dog(Animal):
  def bark(self):
    print("Dog is barking")

result = dog()
result.eat()
result.bark()