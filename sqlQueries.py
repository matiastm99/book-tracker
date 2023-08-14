def initDB(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS books(title varchar(255), status varchar(255));")

def add(cur, title, status):
    cur.execute("INSERT INTO books VALUES (?,?);", (title, status))

def update(cur, title, status):
    cur.execute("UPDATE books SET status=? WHERE title=?;", (status, title))

def delete(cur, title):
    cur.execute("DELETE FROM books WHERE title=?;", (title, ))

def showAllByName(cur):
    for row in cur.execute("SELECT * FROM books ORDER BY title ASC;"):
        print(f"Title: {row[0].title()} - Status: {row[1].title()}")

def showAllByStatus(cur):
    for row in cur.execute("SELECT * FROM books ORDER BY status ASC"):
        print(f"Title: {row[0].title()} - Status: {row[1].title()}")
