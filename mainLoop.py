from menuPrinter import printMenu
from dbClass import DataBase

def mainLoop():
    db = DataBase("books.db")

    while True:
            printMenu()
            opt = int(input("Enter an option: "))
        
            if opt == 1:
                title = input("Enter the title: ").lower()
                status = input("Enter the status: ").lower()
                db.add(title, status)

            elif opt == 2:
                title = input("Enter the title: ").lower()
                status = input("Enter the status: ").lower()
                db.update(title, status)

            elif opt == 3:
                title = input("Enter the title: ").lower()
                db.delete(title)

            elif opt == 4:
                print("")
                show = int(input("Show by name(1) or status(2): "))
                if show == 1:
                    print("")
                    db.showByName()
                elif show == 2:
                    print("")
                    db.showByStatus()
                else:
                    print("ERROR: unknown option")
                    
            elif opt == 0:
                break
            else:
                print("ERROR: unknown option")
    
    db.close()
