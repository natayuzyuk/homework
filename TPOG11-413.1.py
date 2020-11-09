import sqlite3 as sql


con = sql.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `salary` ('id' INTEGER PRIMARY KEY, 'salary' DOUBLE, 'currency' STRING)")
    cur.execute("CREATE TABLE IF NOT EXISTS `position` ('id' INTEGER PRIMARY KEY, 'position' STRING, 'division' STRING)")
    cur.execute("CREATE TABLE IF NOT EXISTS `worker` ('id' INTEGER PRIMARY KEY, 'salary_id' INTEGER, 'position_id' INTEGER, 'firstname' STRING, 'lastname' STRING, FOREIGN KEY (salary_id) references salary(id), FOREIGN KEY (position_id) references position(id) )")

    name = input("Name\n> ")
    surname = input("Surname\n> ")
    position = input("Position\n> ")
    salary = input("salary\n> ")
    cur.execute(f"INSERT INTO 'salary' (salary, currency) VALUES ('{salary}', 'dollar')")
    cur.execute(f"INSERT INTO 'position' (position, division) VALUES ('{position}', 'IT Department')")
    cur.execute(f"INSERT INTO 'worker' (salary_id, position_id, firstname, lastname)  VALUES (1,1, '{name}', '{surname}')")

    cur.execute("SELECT firstname, lastname, salary, position  FROM 'worker' JOIN 'salary' ON 'salary'.id=salary_id JOIN 'position' ON "
                "'position'.id=position_id ")
    rows = cur.fetchall()
    for row in rows:
        print(row[0], row[1], row[2], row[3])

con.commit()
cur.close()