x = 3 
print(x)
def Hello():
  global x
  x = 4
  print(f"Global Variable accessed inside a function is : {x}")
Hello()