#Syntax
# def fun(Parameter):
   #Code
# # fun(blabla) calling function


# #passing a function so we can define later
# def Greatno(a , b):
#     pass
#It means i will write the function later.
# types of Arguments

#1. Default arguments
# def Add(a=10,b=5):
#     print("The addition of a and b is :",a+b)
# #if no arugments passed it will take 10 n 5 as default

#2.Required arguments
# def Add(a,b=5,c = 0):
#     print("The addition of a and b is :",a+b+c)
    #Here giving value of a is compulsary
def Average(*numbers): # numbers = tuple type | Average(**numbers) = dict tyope
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The average of numbers is :",sum/len(numbers))
Average(10,5)
