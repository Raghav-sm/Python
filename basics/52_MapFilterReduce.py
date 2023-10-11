#Traditional method
def cube(x):
  return x*x*x

List = [1,2,3,4,5]
NewList = []
for item in List:
  NewList.append(cube(item))
print(NewList)

#Using Map
MapL = map(cube,List)
# print("Using map",NewL) it will return map object
# convert it to list
print("Using map",list(MapL))


#using Filter
def Filter_fx(a):
  return a>30
    
FilterL = filter(Filter_fx,MapL)
print(list(FilterL))
