class student:
  def  studentinfo(self):

    self.__name = input("Name: ")
    self.__roll = input ("Roll: ")

  def PutStudent(self):
    print("Name : ", self.__name, "Roll : ", self.__roll)

class bsc (student):
  def getBsc(self):
    self.studentinfo()
    self.__p = int(input("Physics Marks: "))
    self.__m = int(input("Math Marks: "))

  def putBsc(self):
    self.PutStudent()
    print("marks is: ", self.__p, self.__m)

class ba (student):

  def getBa(self):
    self.studentinfo()
    self.__h = int(input("History marks: "))

  def putba(self):
    self.PutStudent()
    print("marks is subject: ", self.__h)

student1 = bsc()
student1.getBsc()
student1.putBsc()