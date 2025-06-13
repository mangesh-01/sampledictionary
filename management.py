books_list = {
    "r s agarawal" : 2 ,
    "Gunahon ka devta" : 5,
    "84" : 3
}



print("Welcome to library management system")
print("1. Add Entry \n2. Add Book \n3. Available Books List")
option = input("Please select your option : ")
if option == '1' :
    bookName = input(print("Enter book's name: "))
    if bookName in books_list: 
            if books_list[bookName] > 0:
             books_list[bookName] -= 1
             print(f"{bookName} is lent successfully.")
            else:
             print("Sorry book is unavailable.")


elif option == '2' : 
    bookName = input("Enter the name of book: ")
    qty = input("Enter the number of copies: ")
    if bookName in books_list:
        books_list[bookName] += qty
    
    else:
        books_list[bookName] = qty
    print(f"{bookName} added successfully.")


elif option == '3' :
    print("List of books: \n")
    print(books_list)
