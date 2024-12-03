import sqlite3

con=sqlite3.connect("blog_project.db")
try:
    command = "DELETE FROM frontend_users;"
    cursor = con.cursor()
    cursor.execute(command)
    con.commit()
except Exception as e:
    print(f"Error: {e}")  # Log or handle the error
finally:
    con.close()
