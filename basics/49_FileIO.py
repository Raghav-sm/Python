f = open('README.md','r')
ff = f.read()
print(ff)
f.close() 

#Appending a File
f = open("README.md","a")
ff = f.write('Append test succesfull xD')

#reading a file  | #Alternative method
with open('README.md','r') as f:
  f.read()
  print(f)
#This method closes on its own,Big W situation

#f = open("README.md","a/rb/jpg") we can open it in a,w,r,rb(binary) etc...

with open('README.md','w') as f:
  f.write("Basics of FileIO is cleared")

f = open('README.md','r')
ff = f.read()
print(ff)
f.close()