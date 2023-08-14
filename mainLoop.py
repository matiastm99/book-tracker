import sqlite3
from menuPrinter import printMenu
from sqlQueries import initDB, add, update, delete, showAllByName, showAllByStatus

def mainLoop():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    initDB(cur)
    
    while True:
            printMenu()
            opt = int(input("Enter an option: "))
        
            if opt == 1:
                title = input("Enter the title: ").lower()
                status = input("Enter the status: ").lower()
                add(cur, title, status)
            elif opt == 2:
                title = input("Enter the title: ").lower()
                status = input("Enter the status: ").lower()
                update(cur, title, status)
            elif opt == 3:
                title = input("Enter the title: ").lower()
                delete(cur, title)
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
