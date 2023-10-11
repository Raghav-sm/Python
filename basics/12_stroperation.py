#len function
fruit = "Watermelon"
length = len(fruit)
print(length)

#slicing
fruit = "Watermelon"
print(fruit[:5])
print(fruit[0:len(fruit)-5])
print(fruit[-10:len(fruit)-5]) 
#if left side negative index is given 
# then it does len() on its own.
print(fruit[-10:-1])