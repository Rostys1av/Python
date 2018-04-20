#For-loop itarating through characters in a string

address = "123 main str" #string itarable

for i in address: #it just print every symbols
    print(i)

print("----------------------------")

#For-loop itarating through a list

favorite_books = ["War",
                  "Rich",
                  "Drizzt",
                  "WOW"]

for books in favorite_books:
    print("My favorite books is", books)

print("----------------------------")

#For-loop in tuple

numbers = ("sex","tape","dead pool")

for films in numbers:
    print(films)
print("----------------------------")

#For-loop in a dictionary through key-value pairs

dictionary = {"name":"John","Sex":"male","height":"185"}

for z in dictionary:
    print(z)
print("----------------------------")

favorite_books = ["War",
                  "Rich",
                  "Drizzt",
                  "WOW"]

for books in favorite_books:
    if books == "Drizzt":
        break
    print("My favorite books is", books)