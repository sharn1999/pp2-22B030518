
import csv
import psycopg2
import psycopg2.extras

conn = psycopg2.connect(dbname='mock_data2', user='postgres', password='196235', host='127.0.0.1')
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
def records():
    inp = str(input('Write name or phone: '))
    func = """CREATE OR REPLACE FUNCTION totalRecords(pattern TEXT)
            RETURNS SETOF mock_data AS $$
                BEGIN
                    RETURN QUERY SELECT * FROM mock_data
                    WHERE username LIKE '%' || pattern || '%' OR phone LIKE '%' || pattern || '%';
                END;
            $$ LANGUAGE plpgsql;"""
    cur.execute(func)
    cur.execute("SELECT * FROM totalRecords(%s)", (inp,))
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.execute("DROP FUNCTION totalrecords(pattern TEXT);")
def add():
    
    n = str(input("what name will be add? "))
    p = str(input("what phone will be add? "))
    proc = """CREATE PROCEDURE add_user(name TEXT, phoneNum TEXT)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            UPDATE mock_data SET phone = phoneNum WHERE username = name;
            INSERT INTO mock_data (username, phone) VALUES (name, phoneNum);
        END;
        $$;"""
    # cur.execute(proc)
    cur.execute("CALL add_user(%s, %s)", (n, p))
    # cur.execute("DROP PROCEDURE add_user(name TEXT, phoneNum TEXT);")

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
    procDel = """CREATE PROCEDURE delete_user(name TEXT)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        DELETE FROM MOCK_DATA WHERE username = name;
    END;
    $$;"""
    # cur.execute(procDel)
    cur.execute("CALL delete_user(%s)", (delUsername,))
    # cur.execute("DROP PROCEDURE delete_user(name TEXT);")

dataListNames = ['Olzhas', 'Asan', 'Ermek']
dataListPhones = ['+77777777', '8234234', '11111111']
proc2 = """CREATE PROCEDURE add_users(name TEXT, phoneNum TEXT)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        INSERT INTO mock_data (username, phone) VALUES (name, phoneNum);
    END;
    $$;"""
# cur.execute(proc2)

for i in range(len(dataListNames)):
    cur.execute("CALL add_users(%s, %s)", (dataListNames[i], dataListPhones[i]))

ex = True
while ex:
    command = input("what command are you want? write 1 for return record, write 2 for add user, write 3 for update user, write 4 for delete user, write 5 for exit: ")
    if command == "1":
        records()
    elif command == "2":
        add()
    elif command == "3":
        update()
    elif command == "4":
        delete()
    elif command == "5":
        cur.execute("""DROP TABLE MOCK_DATA""")
        ex = False
    
# INSERT INTO MOCK_DATA (username, phone, user_id) VALUES ('Olzhas', '+7 (707) 768-8988', 101); - command for console

