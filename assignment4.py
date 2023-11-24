import psycopg2


#========================================(functions)==========================================


#function to create students table in database
def create_table():
    sql_query = ''' CREATE TABLE IF NOT EXISTS students(
                            student_id SERIAL,
                            first_name VARCHAR(255) NOT NULL,
                            last_name VARCHAR(255) NOT NULL,
                            email VARCHAR(255) UNIQUE NOT NULL,
                            enrollment_date DATE DEFAULT CURRENT_DATE,
                            PRIMARY KEY (student_id))'''

    cursor.execute(sql_query)

    connect.commit()



#function that populates the student table with all the inital data
def populate_init_data():
    #try executing the sql query
    try:
        sql_query = '''INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
                        ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
                        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
                        ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');'''
        cursor.execute(sql_query)
        connect.commit()
    #cancel if any errors occur
    except Exception as e:
        connect.rollback()


def getAllStudents():

    #sql query to retrieve all data from students table
    cursor.execute('SELECT * FROM STUDENTS')

    #print data to the terminal
    data = cursor.fetchall()
    print("-------------------------")
    print("Printing All Students")
    for row in data: 
        print(row)



def addStudent(firstName,lastName,email,date):
    #try executing the sql query
    try:
        sql_query = '''INSERT INTO students(first_name, last_name, email, enrollment_date) VALUES(%s,%s,%s,%s)'''
        values = (firstName,lastName,email,date)
        cursor.execute(sql_query,values)
        connect.commit()
    #cancel if any errors occur and print error message
    except Exception as e:
        print("Invalid input")
        connect.rollback()



def updateStudentEmail(student_id, new_email):
    #try executing the sql query
    try:
        sql_query = '''UPDATE students SET email=%s WHERE student_id = %s'''
        values = (new_email,student_id)
        cursor.execute(sql_query,values)
        connect.commit()
    #cancel if any errors occur and print error message
    except Exception as e:
        print("Invalid input")
        connect.rollback()

def deleteStudent(student_id):
    #try executing the sql query
    try:
        sql_query = '''DELETE FROM students WHERE student_id=%s'''
        value = (student_id)
        cursor.execute(sql_query,value)
        connect.commit()
    #cancel if any errors occur and print error message
    except Exception as e:
        print("Invalid input")
        connect.rollback()


#=======================================================================



#============================(connect to server)===============================

#credentials to connect to server
hostname = 'localhost'
database= 'Students'
username ='postgres'
password ='fall23'
port_id = 5432


#connect to the database
connect = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = password,
    port = port_id
)

cursor = connect.cursor()
#======================================


#creating students table and populating initial data
create_table()
populate_init_data()

#====================(menu)========================================


while True:

#display options to the user
    print("-------------------------")
    print("1- Get all students")
    print("2- Add a student")
    print("3- Update a students email")
    print("4- Delete a Student")
    print("0- Exit")
    choice = input("Please enter your choice: ")

#calls getAllStudents function
    if(choice=='1'):
        getAllStudents()

#gathers info of new student and calls addStudent function 
    elif(choice=='2'):
        print("Please provide the following information of the new student")
        firstName = input("Please enter the first name: ")
        lastName = input("Please enter the last name: ")
        email = input("Please enter the email: ")
        date = input("Please enter the enrollment date (20xx-mm-dd): ")
        addStudent(firstName,lastName,email,date)

#asks for user id , updated email and updates the database
    elif(choice=='3'):
        getAllStudents()
        print("-------------------------")
        student_id = input("Please enter the id of the student you would like to edit: ")
        new_email = input("Please enter the new email: ")
        updateStudentEmail(student_id,new_email)

#asks for user id , and deletes from database
    elif(choice=='4'):
        getAllStudents()
        print("-------------------------")
        student_id = input("Please enter the id of the student you would like to delete: ")
        deleteStudent(student_id)

    elif(choice=='0'):
        #close the database connection and cursor before exiting the program
        sql_query = 'DROP TABLE students;'
        cursor.execute(sql_query)
        connect.commit()
        cursor.close()
        connect.close()
        break
    else:
        ("Invalid input please try again")