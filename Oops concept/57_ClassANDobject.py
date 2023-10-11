class Person:
  name = "FH"
  occupation = "FBbf"
  Salary = "434"
  def info(self):
    print(f"The person name is {self.name} and he/she is a {self.occupation}.")

a = Person()
a.name = "Raghav"
a.occupation = "Software developer"
a.info()