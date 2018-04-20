#Dictionaries 2 = {"key":"value"}

persone = {"name": "John Smith",
           "address":"Baker str",
           "job":"manager",
           "city":"Keiv"}

#key() method

print(persone.keys())
print("--------------------")

#value() method

print(persone.values())
print("---------------------")

#item() method

print(persone.items())
print("--------------------")

#pop() mwthod
persone.pop('address')
print(persone)
persone.popitem()
print(persone)
print("--------------------")

#copy() method

new_dictionary = persone.copy()

print(new_dictionary)

print("--------------------")

#clear() method

new_dictionary.clear()

print(new_dictionary)