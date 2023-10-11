try:
  a = int(input("Enter the Index: "))
  b = [4,5]
  print(b[a])
except IndexError:
  print("Numbers kalthkolo Raajkumara")
except ValueError:
  print("Ninganthru Value illa,Number agdhru kodu")
finally: 
  print("Always Executed")
  #Whats the point of finally when we directly give statments
  #when the above code is in function then finally is required 

'''
def funx():
  try:
    a = int(input("Enter the Index: "))
    b = [4,5]
    print(b[a])
  except IndexError:
    print("Numbers kalthkolo Raajkumara")
  except ValueError:
    print("Ninganthru Value illa,Number agdhru kodu")
  finally: 
    print("Always Executed")

x = funx()
print(x)
  
'''