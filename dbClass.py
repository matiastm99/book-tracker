import sqlite3

class DataBase():
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.initDB = self.cur.execute("CREATE TABLE IF NOT EXISTS books(title varchar(255), status varchar(255));")

    def add(self, title, status):
        self.cur.execute("INSERT INTO books VALUES (?,?);", (title, status))
        self.con.commit()

    def update(self, title, status):
        self.cur.execute("UPDATE books SET status=? WHERE title=?;", (status, title))
        self.con.commit()

    def delete(self, title):
        self.cur.execute("DELETE FROM books WHERE title=?;", (title, ))
        self.con.commit()

    def showByName(self):
        for row in self.cur.execute("SELECT * FROM books ORDER BY title ASC;"):
            print(f"Title: {row[0].title()} - Status: {row[1].title()}")

    def showByStatus(cur):
        for row in self.cur.execute("SELECT * FROM books ORDER BY status ASC"):
            print(f"Title: {row[0].title()} - Status: {row[1].title()}")

    def close(self):
        self.con.close()
