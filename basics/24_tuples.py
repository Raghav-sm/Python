tup = (1,2,3,3,4,3,4,5,2,6,5,4,8)
tup2 = tup[0:2] #when any changes to tuple ,a new tuple is formed
print("Tuple is :",tup)
print("Sliced Tuple is :",tup2)
 
 #tuple methods
tup1 = (1,3,6,4,3,6,4,6,3,4,8)
c = tup1.count(4)
print('''No of item "4" in tuple is ''',c)
d = tup1.index(4,7,-1) #7,-1 is slicing to find target 4
print("Index of 4 is in :",d)