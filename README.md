COMP 3005 Assignment 4

Aly Matrawy

101174487

November 23, 2023

Link to youtube video: https://youtu.be/6Z98fXLH-EY


Setup instructions for the database

- Create a database in your server
- Enter the credentials of your database/server between lines 97 and 102
- run the program for the rest

Steps to compile and run your application
- open your terminal and ensure you are in the correct directory (../assignment4)
- copy the following command in your terminal to install psycop (needed to connect to database): pip install psycopg2-binary
- to run enter the following command in your terminal : python assignment4.py


A brief explanation of each function in the application.

create_table:
    creates students table in the database using CREATE query


populate_init_data:
    populates table with initial data provided in the specs using INSERT query

getAllStudents:
    retrieves all data from students table using SELECT and prints it to the terminal

addStudent:
    adds student to students table using INSERT query and the inputted parameters

updateStudentEmail: 
    uses UPDATE query to updates student email of the student id of the inputted parameters

deleteStudent:
    uses DELETE query to delete student of the student whos id is the inputted parameters

Rest of program: 

- connects to the server/database using credentials

Menu: 
- infinite while loop which asks the user what they would like to do , if statements handles each case, asks user for necessary information and calls the corresponding function




