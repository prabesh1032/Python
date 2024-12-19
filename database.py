import sqlite3
conn=sqlite3.connect('example.db')
cursor=conn.cursor()
#create
# cursor.execute('''
# CREATE TABLE users(
# id INTEGER PRIMARY KEY,
# name TEXT,
# age INTEGER               
# )
# ''')
#insert
cursor.execute('''
INSERT INTO users(name,age)
VALUES ('Pra',29)
''')
# #delete
cursor.execute('''
DELETE FROM users
               WHERE age = 29
''')
#update
cursor.execute('''
UPDATE users
SET name='Sabin'
WHERE age=21
''')
cursor.execute('SELECT * FROM users')
c = cursor.fetchall()
print(c)
for r in c:
    print(r)
conn.close() 


