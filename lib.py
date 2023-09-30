members = ["james", "mary"]
          # 0    1    2    3    4
library = ["A", "B", "C", "D", "E"]
menu = "1. Borrow a book   2. Login    3.Signup"
borrowed_books = []
login_status = False

while True :
  print (menu)
  choice = input("> ")

  if choice == "1":
    if login_status: # check that the curent user/member is logged in
      
      id = 1 # set a count for display
      for book in library:
        print(id, "", book) # we display the attched id along with the book name
        id = id + 1 # we increase the value of the id.
      # allow the user pick a book
      selected_id = int(input("enter book id: "))
      book_index = selected_id - 1 # subtract 1 from the selected book id to get the actual index of the book

      # take out the book and add it to the borrowed list
      selected_book = library.pop(book_index)
      borrowed_books.append(selected_book)
      print(library)
      print(borrowed_books)
      
  elif choice == "2": 
    username = (input('Enter your user name '))
    if username in members :
      print ('Sucessfully logged in ')
      login_status = True
    elif username not in members:
      print ('name unknown')
      
  elif choice == "3":
    ...
  else:
    print("Invalid input")