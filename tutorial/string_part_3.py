#String are sequence of characters
#Accesing characters in a string
#String are made up of characters, they are indexed based

#index within string
#[START:STOP:STEP]

index1 = "This is index string in Python, is helpfull"
print(index1[0])
print(index1[0:4])
print(index1[5:])
print(index1[:-4])
print(index1[4:-4])

print("Stop------------------------->")
print(index1[0:10:2])
print(index1[::2])
print(index1[::-1])


print("find()------------------------>")

print(index1.find("is", 6))