# hotel_manager

 ---- THIS PROJECT IS FREE AND OPEN SOURCE IF YOU ARE A COLLAGE STUDENT FEEL FREE TO USE MY CODE FOR YOUR ASSINGEMNTS AND ADD MORE TO THIS ----
                                 ---- MADE BY ARYAN RATHORE +91-9685071745, aryanrathore13572002@gmail.com ----


DISCRIPTION:-

a hotel database management system that uses MySQL for the database (stroring and managing the data) and Python for data processing and output. 
this software provides a powerful and flexible tool for managing the data and operations of a hotel.

FEATURES :-
1. manages data like customer, room, and booking details by storing/deleting/adding/updating the data in a mysql database.

2. has text files that keep a track customers bills and check -in/out times and manager's logins using PYTHON fileIO 

3. command line GUI with simple inputs so anyone can use it as long as they can read

WHAT IS A HOTEL_DATABASE:-

A hotel database management system is a software application that is used to store, organize, and manage the data related to a hotel's operations. It typically includes information about guests, rooms, reservations, and staff, as well as financial and accounting data.

THE hotel_database HAS 3 TABLES:-

1. customer :- this table has the information of the customer like their id and what room they are staying in

2. room :- this table has the information of the rooms like room_type and who is staying in the room (via customer id)

3. booking_details :- this table has the information of the booking datials of the customer like their pay amount method and no. of people they are staying with

THE SOFTWARE USES 2 THINGS TO OPERATE:-

1. PYTHON:-

The system may also use Python to process the data from the database and present it to the user. Python is a high-level programming language that is known for its readability and simplicity. It can be used to write scripts that can extract data from the database, perform calculations and analysis, and generate reports and other outputs.

2. MYSQL:-

The system may use MySQL as the database to store the data. MySQL is a popular open-source relational database management system that is widely used in the hospitality industry. It allows for efficient storage and retrieval of data and offers robust security features to protect sensitive information.


HOW TO SETUP THE HOTEL_MANAGER :-

1. IMPORT THE MYSQL DATABASE NAMED hotel_database

2. there are 2 text files that keep the track of the following info:-

2A. BILLS.TXT this file keeps track of the when a user is checking in or out with this it also keeps their booking information if the manager needs

2B. MANAGER_LOGINS.TXT this file keeps track of who is logging into the system at what date and time.

3. CHANGE OR ADD YOUR USERNAME AND PASSWORD AT LINE 786. 

4. now that you have imported the database there is only 1 thing you need to do that is TO CHACNGE THE FILE PATH OF BILLS.TXT AND MANAGER_LOGINS.TXT in your hotel_manager python file i have mentioned in the comments which which functions will require a file path change and what functions use them.

5. after importing the database and changing the file paths you are all set and done.

6. every function has a docstring which disribes how the function works and what it does. 

7. i tried to keep the program simple so anyone who knows the basics of python can solve it 








