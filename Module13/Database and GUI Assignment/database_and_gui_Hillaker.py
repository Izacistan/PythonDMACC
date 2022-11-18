import sqlite3
from sqlite3 import Error
import tkinter as tkr


# DECLARE FUNCTIONS
def create_database():
    # Create a Database called "pythonsqlite.db"
    def create_connection(db):
        """ Connect to a SQLite database """
        try:
            conn = sqlite3.connect(db)
            print(sqlite3.version)
        except Error as err:
            print(err)
        finally:
            conn.close()

    if __name__ == '__main__':
        create_connection("pythonsqlite.db")

    # Create Connection to Database and Create Two Tables, Person and Student
    def create_connection(db):
        """ Connect to a SQLite database
        :param db: filename of database
        :return connection if no error, otherwise None"""
        try:
            conn = sqlite3.connect(db)
            return conn
        except Error as err:
            print(err)
        return None

    def create_table(conn, sql_create_table):
        """ Creates table with give sql statement
        :param conn: Connection object
        :param sql_create_table: a SQL CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(sql_create_table)
        except Error as e:
            print(e)

    def create_tables(database):

        sql_create_person_table = """ CREATE TABLE IF NOT EXISTS person (
                                            id integer PRIMARY KEY,
                                            firstname text NOT NULL,
                                            lastname text NOT NULL
                                        ); """

        sql_create_student_table = """CREATE TABLE IF NOT EXISTS student (
                                        id integer PRIMARY KEY,
                                        major text NOT NULL,
                                        begin_date text NOT NULL,
                                        end_date text,
                                        FOREIGN KEY (id) REFERENCES person (id)
                                    );"""

        # create a database connection
        conn = create_connection(database)
        if conn is not None:
            # create projects table
            create_table(conn, sql_create_person_table)
            # create tasks table
            create_table(conn, sql_create_student_table)
        else:
            print("Unable to connect to " + str(database))

    if __name__ == '__main__':
        create_tables("pythonsqlite.db")


# Create Person Function
def create_person():
    def create_connection(db):
        """ Connect to a SQLite database
        :param db: filename of database
        :return connection if no error, otherwise None"""
        try:
            conn = sqlite3.connect(db)
            return conn
        except Error as err:
            print(err)
        return None

    def create_person(conn, person):
        """Create a new person for table
        :param conn:
        :param person:
        :return: person id
        """
        sql = ''' INSERT INTO person(firstname,lastname)
                  VALUES(?,?) '''
        cur = conn.cursor()  # cursor object
        cur.execute(sql, person)
        return cur.lastrowid  # returns the row id of the cursor object, the person id

    if __name__ == '__main__':
        conn = create_connection("pythonsqlite.db")
        with conn:
            person = ('Rob', 'Thomas')
            global person_id
            person_id = create_person(conn, person)


# Create Student Function
def create_student():
    def create_connection(db):
        """ Connect to a SQLite database
        :param db: filename of database
        :return connection if no error, otherwise None"""
        try:
            conn = sqlite3.connect(db)
            return conn
        except Error as err:
            print(err)
        return None

    def create_student(conn, student):
        """Create a new person for table
        :param conn:
        :param student:
        :return: student id
        """
        sql = ''' INSERT INTO student(id, major, begin_date)
                  VALUES(?,?,?) '''
        cur = conn.cursor()  # cursor object
        cur.execute(sql, student)
        return cur.lastrowid  # returns the row id of the cursor object, the student id

    if __name__ == '__main__':
        conn = create_connection("pythonsqlite.db")
        with conn:
            student = (person_id, 'Songwriting', '2000-01-01')
            student_id = create_student(conn, student)


def view_person_table():
    def create_connection(db):
        """ Connect to a SQLite database
        :param db: filename of database
        :return connection if no error, otherwise None"""
        try:
            conn = sqlite3.connect(db)
            return conn
        except Error as err:
            print(err)
        return None

    def select_all_persons(conn):
        """Query all rows of person table
        :param conn: the connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM person")

        rows = cur.fetchall()

        return rows  # return the rows

    if __name__ == '__main__':
        conn = create_connection("pythonsqlite.db")
        with conn:
            rows = select_all_persons(conn)
            for row in rows:
                print(row)





def view_student_table():
    def create_connection(db):
        """ Connect to a SQLite database
        :param db: filename of database
        :return connection if no error, otherwise None"""
        try:
            conn = sqlite3.connect(db)
            return conn
        except Error as err:
            print(err)
        return None

    def select_all_students(conn):
        """Query all rows of person table
        :param conn: the connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM student")

        rows = cur.fetchall()

        return rows  # return the rows

    if __name__ == '__main__':
        conn = create_connection("pythonsqlite.db")
        with conn:
            rows = select_all_students(conn)
            for row in rows:
                print(row)


# GUI
MAIN_WINDOW = tkr.Tk()
MAIN_WINDOW.geometry('400x200')  # Resize window to adequately show buttons
# Title
MAIN_WINDOW.title("Database and GUI Assignment - Hillaker")

# Buttons

# Create Database and Tables button
database_and_table_button = tkr.Button(MAIN_WINDOW, text="Create Database and Tables", width=30,
                                       command=create_database)
database_and_table_button.grid(row=5)

# Add Person button
create_person_button = tkr.Button(MAIN_WINDOW, text="Add Person", width=30, command=create_person)
create_person_button.grid(row=10)

# Add Student button
create_person_button = tkr.Button(MAIN_WINDOW, text="Add Student", width=30, command=create_student)
create_person_button.grid(row=15)

# View Person Table button
view_person_button = tkr.Button(MAIN_WINDOW, text="View Person Table", width=30, command=view_person_table)
view_person_button.grid(row=20)



# View Student Table button
view_student_button = tkr.Button(MAIN_WINDOW, text="View Student Table", width=30, command=view_student_table)
view_student_button.grid(row=25)

MAIN_WINDOW.mainloop()
