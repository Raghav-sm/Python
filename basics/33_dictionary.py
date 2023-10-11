dict = {
      "A" : 1,
      "B": 2,
      "C" : 3
        }
print(dict["B"]) # Acessing Key Value
# or 
print(dict.get("B")) 
# If B doesnt exist then secind part will not throw error
#it will simply show as None

print("Acessing all keys ",dict.items())