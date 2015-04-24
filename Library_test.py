#  Library_test.py
#  Author: Tyler Peek
#  Date: April 24th, 2015
#
#  Summary: A simple model of a public library
#  using opject-oriented Python. The Library class
#  has a list of shelves. The Shelves class has a
#  list of books and is aware of the library it is
#  in. The Books class is aware of the shelf it is
#  on. All three objects have modified __str__ 
#  methods. Each argument in all three classes has
#  a default value if none is provided.
#  
# 


#  A list of Shelves can be added at creation time or afterwards.
class Library:
    def __init__(self, name = "Library", shelves = []):
        self.name = name
        self.shelves = shelves
        if len(self.shelves) == 0:
            self.shelves = []
        else:
            for each_shelf in shelves:
                each_shelf.library = self

    def addShelf(self, shelf):
        if shelf.library == None:
            self.shelves.append(shelf)
            shelf.library = self
        else:
            print shelf.name + " already belongs to " + self.name + "."

    def removeShelf(self, shelf):
        if shelf in shelves:
            self.shelves.remove(shelf)
        else:
            print shelf.name + " Shelf is not in " + self.name

    def getShelvesCount(self):
        return len(self.shelves)

    def getBooksCount(self):
        count = 0
        for eachShelf in self.shelves:
            count = count + eachShelf.getBooksCount()
        return count

    def __str__(self):
        if len(self.shelves) != 0:
            if len(self.shelves) == 1:
                result = "The " + self.name + " has " + str(len(self.shelves)) + " shelf:\n\n"
            else:
                result = "The " + self.name + " has " + str(len(self.shelves)) + " shelves:\n\n"
            for eachShelf in self.shelves:
                result = result + str(eachShelf) + "\n"
            return result
        else:
            return "The " + self.name + " is empty."


#  A list of Books can be added at creation time or afterwards.
class Shelf:
    def __init__(self, name = "No Name", books = [], library = None):
        self.name = name
        self.books = books
        self.library = library

        if len(self.books) == 0:
            self.books = []
        else:
            for eachBook in books:
                eachBook.shelf = self
        

    def addBook(self, book):
        self.books.append(book)

    def removeBook(self, book):
        self.books.remove(book)

    def getBooksCount(self):
        return len(self.books)

    def __str__(self):
        if len(self.books) != 0:
            result = self.name + " Shelf:\n"
            for eachBook in self.books:
                result = result + str(eachBook) + "\n"
            return result
        else:
            return self.name + " Shelf is empty."


#  A Shelf can be added at creation time or afterwards.
class Book:
    def __init__(self, name = "No Title", shelf = None):
        self.name = name
        self.shelf = shelf
        if self.shelf != None:
            self.shelf.addBook(self)

    def enshelf(self, shelf):
        if self.shelf == None:
            self.shelf = shelf
            self.shelf.addBook(self)
        else:
            print self.name + " is already on " + self.shelf.name + " shelf."

    def unshelf(self):
        if self.shelf != None:
            self.shelf.removeBook(self)
            self.shelf = None
        else:
            print self.name + " is not currently on a shelf."
    
    def __str__(self):
        return self.name



lib1 = Library("Nikiski Library")
print lib1


book1 = Book("1")
#  Books can be added at Shelf creation time...
shelf1 = Shelf("A", [book1])
shelf2 = Shelf("B")
book2 = Book("2")
#  or afterwards.
book2.enshelf(shelf2)
#  Or they can be added at Book creation time.
book3 = Book("3", shelf1)

lib1.addShelf(shelf1)
lib1.addShelf(shelf2)
#  Shelves cannot be added twice.
lib1.addShelf(shelf1)
print lib1

shelf3 = Shelf("Reference")
shelf4 = Shelf("Magazines")

book4 = Book("Python Tips and Tricks")
book5 = Book("Boy's Life")

book4.enshelf(shelf3)

#  Shelves can be added at Library creation time...
lib2 = Library("Seattle Public Library", [shelf3])
#  or afterwards.
lib2.addShelf(shelf4)
book5.enshelf(shelf4)
#  Books cannot be enshelfed twice.
book5.enshelf(shelf1)
print lib2

book1.unshelf()
book5.unshelf()
#  Books cannot be unshelfed twice.
book5.unshelf()
book5.enshelf(shelf1)

print lib1
print lib2
