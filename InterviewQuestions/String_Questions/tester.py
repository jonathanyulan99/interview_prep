dict_stuff = []

dict_stuff.append({"jon":1,"alex":2,"name":3})
dict_stuff.append({"jonathan":11, "alexander":22,"names":33})

for list_dict in dict_stuff:
    for key in list_dict:
        print(list_dict[key])
    print()

print(dict_stuff,sep=",")

class Book():
    def __init__(self,title,pages):
        self.title = title 
        self.pages = pages 
        
    def is_long(self):
        return self.pages > 100
    
    def __str__(self):
        return f"{self.title} is {self.pages} pages long."

    def __eq__(self,other_book):
        return (self.title == other_book.title) and (self.pages == other_book.pages)
    
    def __hash__(self):
        return hash(self.title) ^ hash(self.pages)

book1 = Book("A Christmas Carol",120)
book2 = Book("A Christmas Carol",120)
print("Book is long:",book1.is_long())
print(book1)
print(book1==book2)
print(hash(book1))
print(id(book1))
print(hash(book2))
print(id(book2))
print(type(book1))

