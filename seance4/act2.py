import sqlite3

db = sqlite3.connect("gestion2.db")

def ins(V1,V2):
    db.execute("insert into formation(id, titre) values(?,?)",(V1,V2))




db.execute("create table if not exists formation(id integer, titre text)")
db.execute("create table if not exists etudiant(code integer, nom text, email text)")

db.execute("insert into formation(id, titre) values(?,?)",(1,"Python"))
db.execute("insert into formation(id, titre) values(?,?)",(2,"html"))

db.execute("insert into etudiant(code, nom, email) values(?,?,?)",(1,"youssef","youssed@gmail.com"))
db.execute("insert into etudiant(code, nom, email) values(?,?,?)",(2,"sara","sara@gmail.com"))

ins(3,"java")

db.row_factory = sqlite3.Row
cursor = db.execute("select * from formation")
for row in cursor:
    print(row["id"],row["titre"])

