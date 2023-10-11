def dbl(x):
  return x*2
a = int(input("Enter the Value of the no to be doubled: "))
result =dbl(a)
print("The double is ",result)
# WE can do small function using lambda function
#__________double functions____________
double = lambda x : x*2
print(double(5))

cube = lambda x:x**3
print("The cube is :",cube(3))
avg = lambda x,y: (x+y)/2
print("The avg is ",avg(4,6))


#usually its used to pass functions 
def cubini(fx,value):
  return value + fx(value)
print(cubini(cube,2))