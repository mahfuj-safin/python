class Annimal:
  def sound(self):
    print("Annimal Sound")

class dog(Annimal):
  def sound(self):
    print("Woof")

class cat(Annimal):
  def sound(self):
    print("Meow")

def make_sound(Annimal):
  Annimal.sound()

Dog = dog()
Cat = cat()
make_sound(Dog)
make_sound(Cat)