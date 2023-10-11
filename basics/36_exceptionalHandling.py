try :
  a = int(input("Enter the table you want: "))
  print(f"The Multipliation of {a} is : ")
  for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
  print(e)
print("Some important lines of code ")
#If we give string as input then the program stops and further the program doesnt run 
#So its important to use exception handling

try:
  a = int(input("Enter the Index: "))
  b = [4,5]
  print(b[a])
except IndexError:
  print("Numbers kalthkolo Raajkumara")
except ValueError:
  print("Ninganthru Value illa,Number agdhru kodu")