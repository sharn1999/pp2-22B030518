
import csv
import psycopg2

conn = psycopg2.connect(dbname='mock_data', user='postgres', password='196235', host='127.0.0.1')
conn.autocommit = True
cur = conn.cursor()
cur.execute(
    """create table MOCK_DATA (
        username VARCHAR(50),
        phone VARCHAR(50),
        user_id INT
    );"""
)

with open('MOCK_DATA.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip the header row
    for row in reader:
        cur.execute("""INSERT INTO MOCK_DATA (username, phone, user_id) VALUES (%s, %s, %s)""", (row[0], row[1], row[2]))
def update():
    c = input("update name or phone? ")
    if c == 'name':
        old_first_name = str(input("Write name of user: "))
        new_first_name = str(input("Write name of new user: "))
        update_query_name = "UPDATE MOCK_DATA SET username = %s WHERE username = %s"
        cur.execute(update_query_name, (new_first_name, old_first_name))
        
    elif(c == 'phone'):
        old_phone = str(input("Write phone of user: "))
        new_phone = str(input("Write phone of new user: "))
        update_query_phone = "UPDATE MOCK_DATA SET phone = %s WHERE phone = %s"
        cur.execute(update_query_phone, (new_phone, old_phone))
def delete():
    delUsername = str(input("write name of user: "))
    delete_query = f"DELETE FROM MOCK_DATA WHERE username = '{delUsername}'"
    cur.execute(delete_query)

ex = True
while ex:
    command = input("what command are you want? write 1 for update user, write 2 for delete user, write 3 for delete table, write 4 for exit: ")
    if command == "1":
        update()
    if command == "2":
        delete()
    if command == "3":
        cur.execute("""DROP TABLE MOCK_DATA""")
    if command == "4":
        ex = False
    
# INSERT INTO MOCK_DATA (username, phone, user_id) VALUES ('Olzhas', '+7 (707) 768-8988', 101); - command for console