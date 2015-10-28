# INSERT Command
# import the sqlite3 library
import sqlite3

# Creating the population table
with sqlite3.connect("blog.db") as connection:
  c = connection.cursor()
  # If we want to create a new table, uncomment the next two lines
  c.execute("DROP TABLE IF EXISTS posts")
  c.execute("""CREATE TABLE posts
			  (title TEXT, post TEXT)
			  """)
  # insert multiple records using a tuple
  posts = [
   ("Good", "I\'m good."),
   ("Well", "I\'m well."), 
   ("Excellent", "I\'m excellent."), 
   ("Okay", "I\'m okay.")
  ]

  # insert data into table
  c.executemany('INSERT INTO posts VALUES(?, ?)', posts)
    	
  c.execute("SELECT title, post from posts")

  # fetchall() retrieves all records from the query
  rows = c.fetchall()
  # output the rows to the screen, row by row
  for r in rows:
    print r[0], r[1]

