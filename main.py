import sqlite3

def initDB(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS books(title varchar(255), status varchar(255));")

def addBook(cur, title, status):
    cur.execute("INSERT INTO books VALUES (?,?);", (title, status))

def updateBook(cur, title, status):
    cur.execute("UPDATE books SET status=? WHERE title=?;", (status, title))

def deleteBook(cur, title):
    cur.execute("DELETE FROM books WHERE title=?;", (title, ))

def showAllByName(cur):
    for row in cur.execute("SELECT * FROM books ORDER BY title ASC;"):
        print(f"Title: {row[0].title()} - Status: {row[1].title()}")

def showAllByStatus(cur):
    for row in cur.execute("SELECT * FROM books ORDER BY status ASC"):
        print(f"Title: {row[0].title()} - Status: {row[1].title()}")

def printMenu():
    print("")
    print("1. Add a book")
    print("2. Update a book status")
    print("3. Delete a book")
    print("4. Show all books")
    print("0. Exit")
    print("")

if __name__ == "__main__":
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    initDB(cur)
    
    while True:
        printMenu()
        opt = int(input("Enter an option: "))
        
        if opt == 1:
            title = input("Enter the title: ").lower()
            status = input("Enter the status: ").lower()
            addBook(cur, title, status)
        elif opt == 2:
            title = input("Enter the title: ").lower()
            status = input("Enter the status: ").lower()
            updateBook(cur, title, status)
        elif opt == 3:
            title = input("Enter the title: ").lower()
            deleteBook(cur, title)
        elif opt == 4:
            print("")
            show = int(input("Show by name(1) or status(2): "))
            if show == 1:
                print("")
                showAllByName(cur)
            elif show == 2:
                print("")
                showAllByStatus(cur)
            else:
                print("ERROR: unknown option")
        elif opt == 0:
            break
        else:
            print("ERROR: unknown option")
    con.commit()
    con.close()
