class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def show_details(self):
        print(f"title is {title}, author is {author}, isbn is {isbn}")

books=[]
n=int(input("enter no.of books"))
for i in range(n):
    title=input(f"enter the title of book {i+1}")
    author=input("enter the author of book")
    isbn=input("enter isbn pf book")
    book=Book(title,author,isbn)
    books.append(book)

for n in books:
    n.show_details()

# wanted=input("enter the  wanted title")
# for n in books:
#     if(n.title==wanted):
#       n.show_details()


