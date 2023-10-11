# Method in set
s1 = {1,2,3,4}
s2 = {4,5,6,7}
print(s1.union(s2)) # this is just displaying union 
# If we want to update value then 
# we use the update function
s1.update(s2)
print(s1,s2)


#intersection 
print("Intersection")
s3 = {9,8,7,6}
s4 = {5,4,3,2,7}
print(s3.union(s4))
print(s3.intersection(s4))
# then issubset and issuperset methods 