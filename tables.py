from select import select
import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()


# cur.execute("""CREATE TABLE IF NOT EXISTS students(
#     user_id INT PRIMARY KEY,
#     f_name TEXT NOT NULL,
#     age INT NOT NULL,
#     group_study TEXT NOT NULL,
#     gender TEXT ,
#     direction TEXT NOT NULL);
# """)
# conn.commit()

# cur.execute("""INSERT INTO students(user_id, f_name, age, group_study,gender,direction) 
#    VALUES('1', 'Alex Smith', '22', 'Z68','M','Python');
#    """)
# conn.commit()
# cur.execute("""INSERT INTO students(user_id, f_name, age, group_study,gender,direction) 
#    VALUES('2', 'Nikita Neilko', '23', 'Z69','M','Python');
#    """)
# conn.commit()
# cur.execute("""INSERT INTO students(user_id, f_name, age, group_study,gender,direction) 
#    VALUES('3', 'Alesya Uvarova', '21', 'Z68','W','Python');
#    """)
# conn.commit()
# cur.execute("""INSERT INTO students(user_id, f_name, age, group_study,gender,direction) 
#    VALUES('4', 'Sasha Baranov', '30', 'Z68','M','Python');
#    """)
# conn.commit()
# cur.execute("""INSERT INTO students(user_id, f_name, age, group_study,gender,direction) 
#    VALUES('5', 'Alex Razmanov', '22', 'Z69','M','Python');
#    """)
# conn.commit()
# cur.execute("""INSERT INTO students(user_id, f_name, age, group_study,gender,direction) 
#    VALUES('6', 'Andrey Ivanov', '21', 'Z68','M','Python');
#    """)
# conn.commit()
# cur.execute("""INSERT INTO students(user_id, f_name, age, group_study,gender,direction) 
#    VALUES('7', 'Masha Petrova', '24', 'Z68','W','Python');
#    """)
# conn.commit()
# cur.execute("""INSERT INTO students(user_id, f_name, age, group_study,gender,direction) 
#    VALUES('8', 'Katya Sidorova', '18', 'Z68','W','Python');
#    """)
# conn.commit()
# cur.execute("""INSERT INTO students(user_id, f_name, age, group_study,gender,direction) 
#    VALUES('9', 'Pavel Kek', '88', 'Z68','M','Python');
#    """)
# conn.commit()
# cur.execute("""INSERT INTO students(user_id, f_name, age, group_study,gender,direction) 
#    VALUES('10', 'Artur Pirogov', '14', 'Z68','M','Python');
#    """)
# conn.commit()

cur.execute("SELECT * FROM students;")
one_result = cur.fetchall()
print(one_result)

# cur.execute("""CREATE TABLE IF NOT EXISTS auditorium(
#     user_id INT PRIMARY KEY,
#     f_name TEXT NOT NULL,
#     direction TEXT NOT NULL);
# """)
# conn.commit()

# cur.execute("""INSERT INTO auditorium(user_id,f_name,direction) 
#    VALUES(1, 'TMS314','Python');
#    """)
# conn.commit()
# cur.execute("""INSERT INTO auditorium(user_id,f_name,direction) 
#    VALUES(2, 'TMS333','Python');
#    """)
# conn.commit()

cur.execute("SELECT * FROM auditorium;")
one_result = cur.fetchall()
print(one_result)
