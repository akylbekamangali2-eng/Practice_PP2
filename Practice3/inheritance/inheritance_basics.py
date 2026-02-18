class Person:
  def __init__(self, fname, lname,age,country):
    self.firstname = fname
    self.lastname = lname
    self.age=age
    self.country=country

  def getinfo(self):
    print(self.firstname, self.lastname, self.age,self.country)

class Student(Person):
  pass

class Azim(Student):
  pass

x = Person("Akylbek", "Amangali",18,"Kaz")
x.getinfo()