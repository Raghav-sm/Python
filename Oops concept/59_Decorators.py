def greet(fx):
  def mfx(*args , **kwargs):
    print("Welcome to function")
    fx(*args ,**kwargs) # #args is for tupels **kwargs for dictionaries
    print("Thank you for using the function")
  return mfx

@greet #decorator or greet(hello())
def hello():
  print("Hello world")
@greet
def add( a , b):
  print(a+b)

#greet(add)( 4 , 5 )              Both these methods works too but @greet better
#greet(hello)() # this or above mthod Anyone is fyn
add(4,5)