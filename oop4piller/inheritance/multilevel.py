class grandparent:
  def __init__(self):
    print("Grandparent constructor")

class parent(grandparent):
  def __init__(self):
    super().__init__()
    print("Parent constructor")
class child (parent):
  def __init__(self):
    super().__init__()
    print("child constructor")

child1 = child()