import sqlite3

conn=sqlite3.connect("ghostfreak.db")

cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name varchar(100),path varchar(1000))")

# query="INSERT INTO sys_command VALUES(null,'onenote','C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneNote 2016.exe')"
# cursor.execute(query)
# conn.commit()
# conn.close()

# cursor.execute("CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name varchar(100),path varchar(1000))")

# query="INSERT INTO web_command VALUES(null,'google','http://google.com')"
# cursor.execute(query)
cursor.execute("DELETE from sys_command WHERE name='onenote'")
conn.commit()
conn.close()