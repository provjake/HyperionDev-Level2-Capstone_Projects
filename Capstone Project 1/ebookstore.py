# importing the sqlite module
import sqlite3

# creating a database called ebookstore
db = sqlite3.connect('ebookstore')

cursor = db.cursor()  # getting a cursor object

# creating a table called books
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS books
    (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)
    '''
    )

# list containing table data
table_data = [
    (3001,'A Tale of Two Cities','Charles Dickens',30),
    (3002,'Harry Potter and the Philosopher\'s Stone','J.K. Rowling',40),
    (3003,'The Lion, the Witch and the Wardrobe','C. S. Lewis',25),
    (3004,'The Lord of the Rings','J.R.R Tolkien',37),
    (3005,'Alice in Wonderland','Lewis Carroll',12)
    ]

# inserting table data into the table
cursor.executemany(
    '''
    INSERT OR IGNORE INTO books
    (id, Title, Author, Qty) VALUES(?,?,?,?)''',
    table_data
    )

db.commit() # saving changes to databases

print() # empty line

choice = "" # initializing choice

# while loop to execute tasks
while choice != 0:

    print("Enter the number of what you would like to do (eg 0 to exit)\n")

    # initializing choices string
    choices = "1. Enter book\n2. Update book\n3. "
    option = "Delete book\n4. Search books\n0. Exit\n\n"

    choices = choices + option

    choice = int(input(choices)) # asking the user for choice input

    # entering a book
    if choice == 1:

        # try block
        try:

            # asking for book id
            id = int(input("Enter book id: "))

            # Asking for book title
            Title = input("Enter book title: ")

            # asking for authors name
            Author = input("Enter the author's name: ")

            # asking for quantity of the book
            Qty = int(input("Enter the quantity of the book: "))

            print() # empty line

            # adding book to the table
            cursor.execute(
                '''
                INSERT INTO books(id, Title, Author, Qty)
                VALUES(?,?,?,?)''', (id, Title, Author, Qty)
                )

            print("Book has been added successfully.\n")

            db.commit() # saving changes to databases
            
        # handling exceptions
        except ValueError as error:

            print("\nIvalid input!")

            print(error,"\n")

        except sqlite3.IntegrityError as error:

            print("\nBook id already exists.")
            
            print(error,"\n")
    
    # Updating a book
    elif choice == 2:

        # asking the user for the id of the book
        id = int(input("Enter the id of the book you want to update: "))

        print("Enter the number what you would like to update (e.g 1 for id).\n")

        # initializing choice string
        options = "1. Title\n2. Author\n3. Qty\n\n"

        # asking the user for the update they would like to make
        option = int(input(options))

        if option == 1:

            # try block
            try:

                # asking the user for the updated book title
                Title = input("Enter the updated book title: ")

                print() # empty line

                # updating title of the book
                cursor.execute(
                    '''
                    UPDATE books
                    SET Title = ?
                    WHERE id = ?
                    ''',(Title,id)
                    )

                print("Book title has been updated successfully.\n")

                db.commit() # saving changes to databases

            # handling exception
            except ValueError as error:

                # displaying error message
                print("Ivalid input!")

                print(error)

        elif option == 2:

            # try block
            try:

                # asking the user for the updated author
                Author = input("Enter the updated book author: ")

                print() # empty line

                # updating author of the book
                cursor.execute(
                    '''
                    UPDATE books
                    SET Author = ?
                    WHERE id = ?
                    ''',(Author,id)
                    )

                print("Author's name has been updated successfully.\n")

                db.commit() # saving changes to databases

            # handling exception
            except ValueError as error:

                # displaying error message
                print("Ivalid input!")

                print(error)

        elif option == 3:

            # try block
            try:

                # asking the user for the updated quantity
                Qty = int(input("Enter the updated book quantity: "))

                print() # empty line

                # updating quantity of the book
                cursor.execute(
                    '''
                    UPDATE books
                    SET Qty = ?
                    WHERE id = ?
                    ''',(Qty,id)
                    )

                print("Quantity of books has been updated successfully.\n")

                db.commit() # saving changes to databases

            # handling exception
            except ValueError as error:

                # displaying error message
                print("Ivalid input!")

                print(error)

        else:

            print("Oops - incorrect input")
            
    # deleting a book
    elif choice == 3:

        # try block
        try:

            # asking the user for the book id
            id = int(input("Enter the id of the book you want to delete: "))

            print() # empty line

            # deleting the secified book
            cursor.execute(
                '''
                DELETE FROM books
                WHERE id = ?
                ''',(id,)
                )

            print("Book has been deleted successfully.\n")

            db.commit() # saving changes to databases

        # handling exception
        except ValueError as error:

            # displaying error message
            print("Ivalid input!")

            print(error)
    
    # searching for a book by title or author
    elif choice == 4:
        
        print("Search for book by entering the information required below.\n")

        # Asking for authors name
        Author = input("Enter the author's name: ")

        # asking for book title
        Title = input("Enter the book title: ")

        print() # empty line

        # Searching for a book
        cursor.execute(
            '''
            SELECT id, Title, Author, Qty FROM books
            WHERE Title = ? OR Author = ?
            ''',(Title, Author)
            )

        # fetching all matching records
        books = cursor.fetchall()

        # when a book(s) is not found
        if len(books) == 0:

            print("Book could not be found in the database.\n")
         
        else:

            print("Your search results are displayed below.\n")
            
            # displaying books
            for book in books:

                print(f"{book[0]} {book[1]}  {book[2]} {book[3]}")

            print() # empty line
        
    # Exiting the code
    elif choice == 0:

        db.close() # closing connection to database
        
        print('database connection closed')

        print("Goodbye") # Exiting the code

    else:

        print("Oops - incorrect input.\n")
