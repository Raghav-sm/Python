a= "raghav!!!!!!!!"
print(a.upper()) #RAGHAV!!!!!
print(a.rstrip("!"))# raghac | it removes the trailing targeted character
desciption = "python is good for aiml" #Python is good for aiml
print(desciption.capitalize()) #capital is added

b = "watermelon is a good fruit"
print(b.endswith("is",8,13)) #True is printed
print(b.find("is")) #11
#we can use b.index() tooo but if target char isnt 
#present then index=error ,find = -1

#isalnum() only letters n numbers,no space
c = "Whadupblr7"
print(c.isalnum()) # True
print(c.isalpha()) #False
#isalpha numbers excluded