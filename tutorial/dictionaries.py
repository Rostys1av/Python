#Dictionaries = {"key":"value"}

persone = {"name": "John Smith",
           "address":"Baker str",
           "job":"manager"}

print(persone)

print(persone["address"])

#add key and value to dictionary

persone["city"] = "Kiev"

#Use in to see if the key in the dictionary

print(persone)

print("name" in persone)

#Use not in to see if the key doesn't exist in a dictionary

print("car" not in persone)

print("name" not in persone)

#Use "del" to delete key-value

del (persone["city"])

print(persone)

#Change the value of a key

persone["name"] = "Valentin"

print(persone)