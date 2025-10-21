import sqlite3

db = sqlite3.connect("gestion.db")

db.execute("create table if not exists person(code integer, name text)")
db.execute("insert into person(code,name) values(?,?)",(10,"Karim"))
db.execute("insert into person(code,name) values(?,?)",(11,"Amal"))
db.execute("insert into person(code,name) values(?,?)",(12,"Reda"))
db.execute("delete from person where code=10")
db.execute("update person set name='Radi' where code=12")

db.row_factory = sqlite3.Row
cursor = db.execute("select * from person")
for row in cursor:
    print(row["code"],row["name"])
db.close()