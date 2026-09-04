class Father:
  def work(self):
    print("Father is working")
class Mother:
  def cook(self):
    print("Mother is cooking")
class child(Father, Mother):
  def study(self):
    print("Child is studying")

child1 = child()
child1.work()
child1.cook()
child1.study()