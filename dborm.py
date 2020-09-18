import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    database="crm"
)

cursor = db.cursor(dictionary=True)

def getAll():
    cursor.execute("SELECT * FROM blog_post ORDER BY created_at DESC;")
    result = cursor.fetchall()
    return result
    
def create(title, content, author):
    date = datetime.utcnow()
    cursor.execute("INSERT INTO blog_post(title,content,author, created_at) VALUES(%s, %s, %s, %s)",(title, content, author, date))
    db.commit()

def getOnePost(id):
    id = int(id)
    cursor.execute("SELECT * FROM blog_post WHERE id=%s",(id,))
    result = cursor.fetchall()
    return result

def deletePost(id):
    cursor.execute("DELETE FROM blog_post WHERE id=%s", (id,))
    db.commit()

def updatePost(id, title, content):
    cursor.execute("UPDATE blog_post SET title=%s, content=%s WHERE id=%s",(title, content, id))
    db.commit()