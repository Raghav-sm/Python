class Person:
  def __init__(self,Name,Occupation):
    self.Name = Name
    self.Occupation = Occupation 

      
  def info(self):
    print(f"The person name is {self.Name} and he/she is a {self.Occupation}.")

a = Person('Raghav','Software Developer')
a.info()