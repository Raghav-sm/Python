l = [1,2,5,3,9,6]
print("Orginal list is :",l)
l.append(8)
print("Appended list is :",l)
l.sort()
print("Sorted list is :",l)
l.sort(reverse = True)
print("Reverse sort list is :",l)
print(l.index(5)) # o/p is 3 cuz 3rd position
l.insert(0,10)
print("Inserted list is :",l)

a = [1,2,3,4,5]
b = [6,7,8,9,10]
a.extend(b)
print("Extended a list is :",a)