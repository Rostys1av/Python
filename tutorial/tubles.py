# Tuples = ()
#tuples stores objects in a specific way
#tuples inmutable. This means they cannot change

# Tuplas syntax
print("--------------------")

empty_tuple = ()

print(empty_tuple)

print("--------------------")

city_dalla = ("lattitute","longgitute")
print(city_dalla)

print("--------------------")

one_value =("one value needs coma",)
print(one_value)
print("--------------------")

print(city_dalla[1])

print("--------------------")

#IN a tuple

print("lattitute" in  city_dalla)
print("--------------------")

#city_dalla[0] = ("lattit22ute")
#slice
print(city_dalla[0:])
print(city_dalla[::-1])

#index shows wich index your value has
print("--------------------")
print(city_dalla.index("lattitute"))

#count - count how many values such as you entered in a tuple
print(city_dalla.count("lattitute"))
