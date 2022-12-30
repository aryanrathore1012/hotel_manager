########################################################### CREDITS ##############################################################################################

'''
                                                  WELCOME TO THE HOTEL_MANAGER

                THIS PROGRAM MANAGES A HOTEL'S CUSTOMERS, BILLS AND ROOMS USING A MYSQL DATABASE (HOTEL_DATABASE)

                                                    MADE BY : ARYAN RATHORE 
                                            COMPUTER SCIENCE ENGINEER AT VIT BHOPAL

                                                        CONTACT INFO
                                                       +91-9685071745
                                                aryanrathore13572002@gmail.com
                                               aryan.rathore2021@vitbhopal.ac.in

'''

########################################################### IMPORTS ##############################################################################################

import mysql.connector as c
import datetime as dt
from tabulate import tabulate
import time

########################################################### FUNCTIONS ############################################################################################


'''                                                        IMPORTANT NOTE                                                              
                BEFORE YOU RUN THE PROGRAM MAKE SURE YOU READ AND FOLLOW THE LINES BELOW OTHERWISE THE PROGRAM WONT RUN  '''

# 1

''' THERE ARE IN TOTAL OF 16 FUNCTIONS THAT CALL EACH OTHER, "EVERY FUNCTION HAS A DOCSTRING LIKE THIS SPECIFIES WHAT THAT FUNCTION DOES
                                                    AND HOW THE THE FUNCTION WORKS"                                                      '''

# 2

'''   I HAVE TO SPECIFY A FILE PATH TO OPEN THE LOG (BILLS.TXT, MANAGER_LOGINS.TXT) FILES IF YOU ARE USING OR COPY PASTING MY CODE
    MAKE YOU CHANGE THE FILE PATHS I HAVE SPECIFIED WHICH FUNCTIONS NEED A 'FILE PATH CHANGE' SO MAKE SURE YOU CHANGE THEM FIRST '''

#----------------------------------------------------------------------------------------------------------------------------------------

def hotel_ui(): # done
    '''
        This is the mai user interface this will show the manager all the details about the hotels like :-
        1. how many total rooms are there in the hotel | done 
        2. how many rooms are avaible/unavaible in the hotel | done
        3. case switch that ask the manager to check further room details, check in or check out | done 

    '''

    # sql query to get all the rooms 
    cursor1.execute("SELECT * FROM room")
    rooms_data = cursor1.fetchall()

    # sql query to get all avaible rooms
    cursor1.execute("SELECT COUNT(*) FROM `room` WHERE EMPTY = 'NO';")
    unavaible_rooms = cursor1.fetchone()

    # sql query to get all avaible rooms
    cursor1.execute("SELECT COUNT(*) FROM `room` WHERE EMPTY = 'YES';")
    avaible_rooms = cursor1.fetchone()

    # showing the current hotel status 

    print("\n**************************************************************************************************************************************************************\n")

    print("\n ------------------ The current status of the hotel ------------------ \n")
    print(f"\tThe current date_time is : {dt.datetime.now()}\n")
    print(f"\tThe total numbers of rooms in the hotel : {len(rooms_data)}")
    print(f"\t\t\t{avaible_rooms[0]} are AVAIBLE.")
    print(f"\t\t\t{unavaible_rooms[0]} are UNAVAIBLE. \n")
    print("\n----------------------------------------------------------------------\n")
    print("to check how many or which rooms are free press 3 in the hotel menu")
    print("to check the detailed information of all customers 4 in the hotel menu")
    print("to check in or out press 1 or 2 in the hotel menu")
    print("\n----------------------------------------------------------------------\n")
    print("YOU MAY SCROLL UP FOR THE OUTPUT, ENTER 1 BELOW TO SEE THE HOTEL MENU")
    print("\n----------------------------------------------------------------------\n")

    # asking the user if they wanna see the hotel menu or not 

    menu_input = input("Enter 1 if you want to see the hotel menu\nEnter 2 if you wanna quit here: ")

    if menu_input == '1':
        hotel_menu()
    elif menu_input == '2':
        print("\n--------------------------------------------------------------------------------------------------------------")
        print("\nThanks for using the database management system.")
        print("Made by Aryan Rathore. ")
        print("email : aryanrathore13572002@gmailcom")
        print("Phone number: +91 9685071745")
        print("\n--------------------------------------------------------------------------------------------------------------")
        quit()
    else:
        print("\n--------------------------------------------------------------------------------------------------------------\n")
        print("ERROR THE CHOICE YOU HAVE ENTERED DOSENT EXSIST PLEASE ENTER A CORRECT NUMBER AGAIN. ")
        print("\n--------------------------------------------------------------------------------------------------------------\n")
        time.sleep(5)
        hotel_ui()

#----------------------------------------------------------------------------------------------------------------------------------------

def hotel_menu(): # done
    print("\n*******************************************************************************************************************************")
    user_input = input('''
\t\t\t\t\t----------------- HOTEL_MENU ------------------

*******************************************************************************************************************************

--- MANAGER AND CUSTOMER BILL LOGS ---

press 9 to SEE MANAGER_LOGIN.TXT  (KEEPS TRACK OF WHEN ALL THE MANAGERS LOGGED IN) 

press 10 to SEE BILLS.TXT  (KEEPS TRACK OF check-in and out times of the customers and bill information) 

-------------------------------------------------------------------------------

--- LOOKUP IN HOTEL_DATABASE ---

press 3 to check the DETAILED INFORMATION OF ALL ROOMS in the hotel

press 4 to check the USER DETAILED INFORMATION

press 5 to check PAST BOOKINGS / BILL INFORMATION

press 6 to see INFORMATION OF ALL CUSTOMER, ROOMS, BOOKINGS WITH BILL LOG (BEST WAY)

-------------------------------------------------------------------------------

--- ROOMS --- 

INFORMATION FOR ROOMS PRESS 3

press 7 to ADD a new room to the hotel

press 8 to REMOVE a old room from the hotel

-------------------------------------------------------------------------------

--- CHECK-IN/OUT ---

Press 1 if you want to CHECK-IN a new customer

press 2 if you want to CHECK-OUT a new user 

-------------------------------------------------------------------------------

YOU MAY SCROOL UP TO SEE MORE INFO OR ENTER 11 TO QUIT

-------------------------------------------------------------------------------

Enter your choice here: ''')

    if user_input == "1":
        check_in()
    elif user_input == "2":
        check_out()
    elif user_input == "3":
        current_rooms_status()
    elif user_input == "4":
        get_user_info()
    elif user_input == "5":
        get_booking_info()
    elif user_input == "6":
        get_whole_booking_info()
    elif user_input == "7":
        add_room()
    elif user_input == "8":
        remove_room()
    elif user_input == "9":
        read_manager_logins_log()
    elif user_input == "10":
        bill_log_check()
    elif user_input == "11":
        print("\n--------------------------------------------------------------------------------------------------------------")
        print("\nThanks for using the database management system.")
        print("Made by Aryan Rathore. ")
        print("email : aryanrathore13572002@gmailcom")
        print("Phone number: +91 9685071745")
        print("\n--------------------------------------------------------------------------------------------------------------")
        quit()

    # incase the user makes a mistake the program will handle errors like this:- 

    else:
        print("\n--------------------------------------------------------------------------------------------------------------\n")
        print("ERROR THE CHOICE YOU HAVE ENTERED DOSENT EXSIST PLEASE ENTER A CORRECT NUMBER AGAIN. ")
        print("\n--------------------------------------------------------------------------------------------------------------\n")
        time.sleep(5)
        hotel_menu()

#----------------------------------------------------------------------------------------------------------------------------------------

def hotel_menu_choice(): # done
    '''
        after doing a specific task the program quits and the user has to start it again which is tedious
        so to prevent that this function will run
        1. case switch which asks the user to quit the program or use hotel menu to do another task. 
    '''

    ui = input('Enter 1 if you wanna want to use the hotel menu to see changes or do other task again\nEnter 2 to quit the program here: ')

    if ui == "1":
        hotel_menu()
    elif ui == "2":
        print("\n--------------------------------------------------------------------------------------------------------------")
        print("\nThanks for using the database management system.")
        print("Made by Aryan Rathore. ")
        print("email : aryanrathore13572002@gmailcom")
        print("Phone number: +91 9685071745")
        print("\n--------------------------------------------------------------------------------------------------------------")
        quit()
    
    # this runs in case the user enters an invalid value

    else:
        print("\n--------------------------------------------------------------------------------------------------------------\n")
        print("ERROR THE CHOICE YOU HAVE ENTERED DOSENT EXSIST PLEASE ENTER A CORRECT NUMBER AGAIN. ")
        print("\n--------------------------------------------------------------------------------------------------------------\n")
        time.sleep(5)
        hotel_ui()

#----------------------------------------------------------------------------------------------------------------------------------------

# this funtion is linked to bill_log_checkin so update file path there first:- 

def check_in(): # to finish
    '''
         in the hotel ui case swtich if the user chooses 'check in' option this function should run
         1. this function checks if the room that user wants is avaible or not | done
         2. takes all there info. | done
         3. takes all their booking info. | done 
         4. updates that the room status to unavaible | done
         5. adds to bill_log that customer checked in at timings
         6. prints success measage | done

    '''

    # --------------------------------------------------------------
    # 1. check for all the avaible rooms in the database

    cursor1.execute("SELECT * FROM `room` WHERE EMPTY = 'YES';")
    all_rooms_data = cursor1.fetchall()

    print("here is a table of all the rooms that are avaible:- \n")
    print(tabulate(all_rooms_data, headers=['room_number', 'room_type', 'room_rate', 'occupant', 'empty'], tablefmt='outline', numalign='center'))
    print("\n----------------------------------------------------------------------\n")

    # --------------------------------------------------------------
    # 2. entering the personal details of the user 

    print("\n--------------------------------------------------------------------------------------------------------------\n")
    room_number = input("Enter or COPY/PASTE the room_number of the room you wanna rent to the customer here (MAKE SURE IT IS A VALID ROOM OR EXPECT ERRORS) (integer): ")
    print("\n--------------------------------------------------------------------------------------------------------------\n")

    # if customer is new this will make a new entry else it will just update the room_number of the customer
    cust_input = input("Enter 1 if the customer has never visited the hotel before (new_customer)\nEnter 2 if the customer has visited the hotel before\n3 to check if the customer has visited or not here: ")

    # if a customer is new we will take all their info and save it to the database
    if cust_input == "1":

        customer_id = int(input("Enter a custom id (to uniquely identify them) of the customer here (can be any integer): "))
        name = input("Enter the name of the customer here: ")
        phone = int(input("enter the phone of the user here (must be an integer): ")) 
        age = int(input("Enter the age of the customer here (must be an integer): "))
        sex = input("Enter the sex of the customer here ('M' for male and 'F' for female): ")
        address = input("enter the address of the customer here: ") 
        adhar_number = int(input("Enter the adhar number of the customer here (must be an integer): "))
        bill_id = int(input("Enter the ID of their custom bill here (must be an integer): "))

        cursor1.execute(f"INSERT INTO customer  VALUES ({customer_id}, '{name}',{phone}, {age}, '{sex}', '{address}', {adhar_number}, '{room_number}', {bill_id})")

    # if the customer has already visited we will take their info from the database
    elif cust_input == "2":

        customer_id = int(input("Enter the id of the customer here (must be an integer) (check customer info from hotel menu for their customer_id): "))
        bill_id = int(input("Enter the ID of their custom bill here (must be an integer): "))

        # updating the room number the user is staying in and their new bill
        cursor1.execute(f"UPDATE customer SET room_number = '{room_number}', bill_id = {bill_id} WHERE customer_id = {customer_id}; ")
        main_connector.commit()

        cursor1.execute(f"SELECT * FROM customer WHERE customer_id = {customer_id}")
        customer_data = cursor1.fetchone()

        name = customer_data[1]
        phone = customer_data[2] 
        age = customer_data[3]
        sex = customer_data[4]
        address = customer_data[5]
        adhar_number = customer_data[6]

    else:
        print("\n----------------------------------------------------------------------\n")
        print("ERORR YOU HAVE ENTRED AN INVALID VALUE PLEASE RUN THE PROGRAM AGAIN ENTER A CORRECT VALUE. ")
        print("\n----------------------------------------------------------------------\n")
        quit()

    # --------------------------------------------------------------
    # 3. asking for the booking detais:-

    book_date = dt.date.today()
    book_time = dt.datetime.now().time()
    book_time = book_time.replace(microsecond=0)
    payment_amount = int(input("Enter the amount of payment here: "))
    payment_method = input("Enter the method of payment here: ")
    number_of_people = int(input("Enter the number of people living with the customer here: "))

    # creating their bill and adding data to booking details
    cursor1.execute(f"INSERT INTO booking_details VALUES ({bill_id},'{room_number}','{book_date}','{book_time}' ,{payment_amount},'{payment_method}',{number_of_people},{customer_id});")
    
    # --------------------------------------------------------------
    # 4. updating the booked rooms status to unavaible:-

    cursor1.execute(f"UPDATE room SET EMPTY = 'NO', occupant= {customer_id} WHERE room_number = '{room_number}';")

    # ----------------------------------------------------------------------
    # 5. updating and logging in the bil log that the customer has come in:-

    bill_log_checkin(bill_id, room_number, customer_id, name, age, sex, book_date, book_time, payment_amount, payment_method, number_of_people)

    # ------------------------------------------------------------------------------------------------------
    # 6. checking if the booking_details is successfully added to the database and printing a success measage:- 

    if cursor1.rowcount > 0:
        print("\n------------------------------------------------------------------------------------------\n")
        print(f"\t -------- SUCCESS WELCOME TO THE HOTEL {name} -------- \n")
        print(f"1. the user {customer_id}, {name} has been ssuccessfully added to the database. ")
        print(f"2. the booking_details / bill {bill_id} has been successfully added to the database. ")
        print(f"3. the {room_number} has been successfully updated to the database. ")
        print("\n-----------------------------------------------------------------------------\n")
        main_connector.commit()
    else:
        print(f"some error occured. ")


    # asks the user to quit or do another task
    hotel_menu_choice()
    
#----------------------------------------------------------------------------------------------------------------------------------------

# this funtion is linked to bill_log_checkout so update file path there first:- 

def check_out(): # done
    '''
        in the hotel ui case swtich if the user chooses 'check out' option this function should run
        1. update the database to make room EMPTY and show goodbye | done
        2. update the bill log | done

    ''' 

    # -----------------------------------------------------------------------------
    # getting the information from the database as a list filled with tuples

    cursor1.execute("SELECT * FROM `customer` WHERE room_number NOT LIKE '';")
    all_customers_data = cursor1.fetchall()
    print("Here is a list of all customer currently resinding in the hotel:- ")
    print("\n----------------------------------------------------------------------\n")
    print(tabulate(all_customers_data, headers=['customer_id','name','phone', 'age', 'sex','address','adhaar_number','room_number','bill_id'], numalign='centre', tablefmt='outline'))
    print("\n----------------------------------------------------------------------\n")

    # -----------------------------------------------------------------------------
    # 1. update the database to make room EMPTY

    customer_id = int(input("Enter or copy/paste the customer_id of the customer who is checking-out here (integer): "))

    cursor1.execute(f"UPDATE room SET EMPTY = 'YES', occupant = NULL WHERE occupant = {customer_id};")
    cursor1.execute(f"UPDATE `customer` SET room_number = '' WHERE customer_id = {customer_id};")

    if cursor1.rowcount > 0:
        main_connector.commit()
        print("\n--------------------------------------------------------------------------------\n")
        print("\t\t   ------- GOODBYE -------- \n")
        print("\t --- Hope you had a good stay at our hotel --- ")
        print("\n--------------------------------------------------------------------------------\n")


    # -----------------------------------------------------------------------------
    # 2. update the bill log
    
    cursor1.execute(f"SELECT * FROM customer WHERE customer_id = {customer_id};") 
    customer_data = cursor1.fetchone() 
    cursor1.execute(f"SELECT * FROM `booking_details` WHERE customer_id = {customer_id};") 
    booking_data = cursor1.fetchone() 

    bill_id = booking_data[0]
    room_number = booking_data[1]
    name = customer_data[1]
    age = customer_data[3]
    sex = customer_data[4]
    book_date = dt.datetime.now().date()
    book_time = dt.datetime.now().time()
    book_time = book_time.replace(microsecond=0)
    payment_amount = booking_data[4]
    payment_method = booking_data[5]
    number_of_people = booking_data[6]

    bill_log_checkout(bill_id, room_number, customer_id, name, age, sex, book_date, book_time, payment_amount, payment_method, number_of_people)

    # asks the user to quit or do another task
    hotel_menu_choice()

#----------------------------------------------------------------------------------------------------------------------------------------

def current_rooms_status(): # done
    '''
        this function shows the manager the status and info of all rooms if the 'check room status' option is selected
        1. should show the info of all the rooms in a nice clean way | done
        2. if too many rooms the manager should have a search room by room number option | this should be optional

    '''

    # getting the information from the database as a list filled with tuples
    cursor1.execute("SELECT * FROM room")
    all_rooms_data = cursor1.fetchall()
    
    print("\n----------------------------------------------------------------------\n")
    print("The information of the rooms in the hotel are as follows:- \n")
    print("if the occupant row is empty, it means that it is empty. \n")

    # showing the data in a tablular format using the tabulate module
    print(tabulate(all_rooms_data, headers=['room_number', 'room_type', 'room_rate', 'occupant', 'empty'], tablefmt='outline', numalign='center'))
    print("\n----------------------------------------------------------------------\n")

    # this is so that the user can do further task so they dont hace to run the progam again and again
    hotel_menu_choice()

#----------------------------------------------------------------------------------------------------------------------------------------

def get_user_info(): # done
    '''
        shows the manager the information of all users like name and room they stay in

    '''

    # getting the information from the database as a list filled with tuples
    cursor1.execute("SELECT * FROM `customer` ")
    all_customers_data = cursor1.fetchall()

    print("\n----------------------------------------------------------------------\n")
    print("The information of the customers who stayed hotel are as follows:- \n")

    # showing the data in a tablular format using the tabulate module
    print(tabulate(all_customers_data, headers=['customer_id','name','phone', 'age', 'sex','address','adhaar_number','room_number','bill_id'], numalign='centre', tablefmt='outline'))
    print("\n----------------------------------------------------------------------\n")

    # this is so that the user can do further task so they dont hace to run the progam again and again
    ui = int(input('Enter 1 if you wanna want to use the hotel menu to see changes or do other task again\nEnter 2 to quit the program here: '))

    if ui == 1:
        hotel_menu()
    else:
        print("\n--------------------------------------------------------------------------------------------------------------")
        print("\nThanks for using the database management system.")
        print("Made by Aryan Rathore. ")
        print("email : aryanrathore13572002@gmailcom")
        print("Phone number: +91 9685071745")
        print("\n--------------------------------------------------------------------------------------------------------------")
        quit()

#----------------------------------------------------------------------------------------------------------------------------------------

def get_booking_info(): # done
    '''
        shows the manager the information of all past bookings and and ongoing ones

    '''

    # getting the information from the database as a list filled with tuples
    cursor1.execute("SELECT * FROM `booking_details` ")
    all_customers_data = cursor1.fetchall()

    print("\n----------------------------------------------------------------------\n")
    print("The information of the bookings who stayed hotel are as follows:- \n")

    # showing the data in a tablular format using the tabulate module
    print(tabulate(all_customers_data, headers=['bill_id','room_number', 'book_date', 'book_time', 'payment_amount', 'payment_method', 'number_of_people', 'customer_id'], numalign='centre', tablefmt='outline'))
    print("\n----------------------------------------------------------------------\n")

    # this is so that the user can do further task so they dont hace to run the progam again and again
    hotel_menu_choice()

#----------------------------------------------------------------------------------------------------------------------------------------

# this funtion is linked to bill_log_check so update file path their first:- 

def get_whole_booking_info(): # to finish
    '''
        when the option is chosen this function will show the info of all tables in the hotel_database
        1. show the customers table
        2. show the rooms table
        3. show the booking_details table 
        4. show the bill log
    '''

    # -----------------------------------------------------------------------------------
    # 1. show the customers table

    # getting the information from the database as a list filled with tuples
    cursor1.execute("SELECT * FROM `customer` ")
    all_customers_data = cursor1.fetchall()

    print("\n----------------------------------------------------------------------\n")
    print("The information of the customers who stayed hotel are as follows:- \n")

    # showing the data in a tablular format using the tabulate module
    print(tabulate(all_customers_data, headers=['customer_id','name','phone', 'age', 'sex','address','adhaar_number','room_number','bill_id'], numalign='centre', tablefmt='outline'))

    # -----------------------------------------------------------------------------------
    # 2. show the rooms table

    # getting the information from the database as a list filled with tuples
    cursor1.execute("SELECT * FROM room")
    all_rooms_data = cursor1.fetchall()
    
    print("\n\n")
    print("The information of the rooms in the hotel are as follows:- \n")
    print("if the occupant row is empty, it means that it is empty. \n")

    # showing the data in a tablular format using the tabulate module
    print(tabulate(all_rooms_data, headers=['room_number', 'room_type', 'room_rate', 'occupant', 'empty'], tablefmt='outline', numalign='center'))

    # -----------------------------------------------------------------------------------
    # 3. show the booking_details table 

    # getting the information from the database as a list filled with tuples
    cursor1.execute("SELECT * FROM `booking_details` ")
    all_customers_data = cursor1.fetchall()

    print("\n\n")
    print("The information of the bookings who stayed hotel are as follows:- \n")

    # showing the data in a tablular format using the tabulate module
    print(tabulate(all_customers_data, headers=['bill_id','room_number', 'book_date', 'book_time', 'payment_amount', 'payment_method', 'number_of_people', 'customer_id'], numalign='centre', tablefmt='outline'))
    print("\n\n")

    print("\n-----------------------------------------------------------------------------------------------------------------------------\n")
    print("THE FIRST TABLE SHOWS CUSTOMER, ROOMS, BOOKINGS INFO YOU MAY SCROOL UP TO SEE ALL INFO")
    print("\n-----------------------------------------------------------------------------------------------------------------------------\n")

    # -----------------------------------------------------------------------------------
    # 4. show the booking_details table

    bill_log_check()
    
#----------------------------------------------------------------------------------------------------------------------------------------

def add_room(): # done
    '''
        if the manager needs they can add new rooms to this hotel so more customers can stay
        1. this functions add new rooms DEFAULT AVAIBLE | done

    '''


    # asking the user for values
    print("\n----------------------------------------------------------------------\n")
    room_number = int(input("Enter the new room's room number here: "))
    room_type = input("Enter the type of the room here: ")
    room_rate = int(input("Enter the rate of the room here: "))

    # entering these values into the database
    cursor1.execute(f"INSERT INTO room  VALUES ('{room_number}','{room_type}',{room_rate},NULL,'YES'); ")

    # saving the changes of the database
    main_connector.commit()

    # checking if the value has been inserted sucessfully
    if cursor1.rowcount > 0:
        print("\n----------------------------------------------------------------------\n")
        print(f"\nthe room {room_number}, {room_type}, {room_rate}, NULL, 'YES' has been successfully added to the database. ")
        print("\n----------------------------------------------------------------------\n")

    else:
        print("some error happend in enter the room data make sure room rate is an integer and others are alphanumeric. ")
    
    # this is so that the user can do further task so they dont hace to run the progam again and again
    hotel_menu_choice()

#----------------------------------------------------------------------------------------------------------------------------------------

def remove_room(): # done
    '''
        if the manager needs they can REMOPVES rooms from the hotel

    '''

    # first we show the user a list of all rooms
    cursor1.execute("SELECT * FROM room")
    all_rooms_data = cursor1.fetchall()

    print("\n----------------------------------------------------------------------\n")
    print("here is a list of all rooms in the hotel:- \n")
    print(tabulate(all_rooms_data, headers=['room_number', 'room_type', 'room_rate', 'occupant', 'empty'], tablefmt='outline', numalign='center'))
    print("\n----------------------------------------------------------------------\n")

    # then we ask for the room number
    room_number = int(input("\nEnter or copy/paste the room_number of room you wanna remove here: "))

    cursor1.execute(f"DELETE FROM room WHERE room_number = {room_number}")

    # saving the changes happened to database
    main_connector.commit()

    # checking if the row was actually deleted
    if cursor1.rowcount > 0:
        print("\n----------------------------------------------------------------------\n")
        print(f"the room {room_number} was successfully removed from the database. ")
        print("\n----------------------------------------------------------------------\n")
    else:
        print("due to an invalid query of server issue the value was not deleted from the hotel database. ")
    
    # this is so that the user can do further task so they dont hace to run the progam again and again
    hotel_menu_choice()

#----------------------------------------------------------------------------------------------------------------------------------------

# this function will require a file path check:- 

def bill_log_checkin(bill_id, room_number, customer_id, name, age, sex, book_date, book_time, payment_amount, payment_method, number_of_people): # done
    '''
        makes a bill and saves it into the bill log so the manager can check who checked in at what time 

    '''

    bill = f"check-in, {bill_id}, {room_number}, {customer_id}, {name}, {age}, {sex}, {book_date}, {book_time}, {payment_amount}, {payment_method}, {number_of_people}"
    
    bill_log_file_path = "F://aryans_code_notes//mySQL//hotel_management_system//bills.txt"

    with open(bill_log_file_path, 'a') as t:
        t.write("\n" + bill)

    print("\nThe bill log has successfully been updated. \n") 

#----------------------------------------------------------------------------------------------------------------------------------------

# this function will require a file path check:- 

def bill_log_checkout(bill_id, room_number, customer_id, name, age, sex, book_date, book_time, payment_amount, payment_method, number_of_people): # done
    '''
        shows the user the all the user and booking info in form of a bill 

    '''

    bill = f"check-out, {bill_id}, {room_number}, {customer_id}, {name}, {age}, {sex}, {book_date}, {book_time}, {payment_amount}, {payment_method}, {number_of_people}"
    
    bill_log_file_path = "F://aryans_code_notes//mySQL//hotel_management_system//bills.txt"

    with open(bill_log_file_path, 'a') as t:
        t.write("\n" + bill)

    print("\nThe bill log has successfully been updated. \n") 
    
#----------------------------------------------------------------------------------------------------------------------------------------

# this function will require a file path check:- 

def update_manager_logins_log(username, data_time):
    '''
        adds managers to the database with there unique manager login and password
    '''

    login_file_path = "F://aryans_code_notes//mySQL//hotel_management_system//manager_logins.txt"
    with open(login_file_path, 'a') as t:
        line = f"{username} logged into the database at {data_time}"

        t.write("\n" + line)

#----------------------------------------------------------------------------------------------------------------------------------------

# this function will require a file path check:- 

def read_manager_logins_log():
    '''
        adds managers to the database with there unique manager login and password
    '''

    login_file_path = "F://aryans_code_notes//mySQL//hotel_management_system//manager_logins.txt"

    with open(login_file_path, 'r') as t:
        content = t.read()
        content = content.split("\n")

    print("\n-----------------------------------------------------------------------------------------------------------------------------------\n")
    print("\t\t\t\t\t\t ----------------- MANAGER LOGIN LOG ----------------- \n")

    for line in content:
        print(line)
    
    print("\n-----------------------------------------------------------------------------------------------------------------------------------\n")

    hotel_menu_choice()

#----------------------------------------------------------------------------------------------------------------------------------------

# this function will require a file path check:- 

def bill_log_check(): # done 

    '''
        when the user Enters 11 in the hotel menu this function runs its main task is to:-
        1. read the bills.txt from the specific directory. | done
        2. show the manager all the details of check-in/out and bill information of the customers. | done
    '''
    
    # ---------------------------------------------------------------------
    # 1. read the bills.txt from the specific directory.

    bill_file_path = "F://aryans_code_notes//mySQL//hotel_management_system//bills.txt"

    with open(bill_file_path, 'r') as t:
        content = t.read()
        content = content.split("\n")
    
    # ---------------------------------------------------------------------
    # 2. show the manager all the details of check-in/out and bill information of the customers.

    print("\n-----------------------------------------------------------------------------------------------------------------------------------\n")
    print("\t\t\t\t\t\t ----------------- BILL LOG ----------------- \n")

    for details in content:

        details = details.split(", ")

        # checkin-out, bill_id, room_number, customer_id, name, age, sex, book_date, book_time, payment_amount, payment_method, number_of_people
        #      0        1            2           3         4     5    6     7           8               9              10         11

        print(f"The customer {details[3]}, {details[4]}, of age {details[5]}, '{details[6]}', {details[0]} at {details[7]} {details[8]}, their bill details: pay_amt : {details[9]}, pay_type : {details[10]}, stay_members : {details[11]}.  ")
        
    print("\n-----------------------------------------------------------------------------------------------------------------------------------\n")

    hotel_menu_choice()

#----------------------------------------------------------------------------------------------------------------------------------------

########################################################### MAIN ############################################################################################

if __name__ == "__main__":

    try:

        # connecting to the database:- 
        main_connector = c.connect(host="localhost", user="root", password="", database="hotel_database")
        cursor1 = main_connector.cursor()

        print("\n\n")
        print('''
************************************************************************************************************************************************************ 
    ***********  ***********  ***********  ***********  ***********  ***********  ***********  ***********  ***********  ***********  ***********  
     *********    *********    *********    *********    *********    *********    *********    *********    *********    *********    *********
      *******      *******      *******      *******      *******      *******      *******      *******      *******      *******      ******* 
       *****        *****        *****        *****        *****        *****        *****        *****        *****        *****        ***** 
        ***          ***          ***          ***          ***          ***          ***          ***          ***          ***          ***            
         *            *            *            *            *            *            *            *            *            *            *
************************************************************************************************************************************************************* ''')
        print("\n\t\tWELCOME TO THE HOTEL DATABASE. \n")
        print("\t\tMade by Aryan Rathore. ")
        print("\t\temail : aryanrathore13572002@gmailcom")
        print("\t\tPhone number: +91-9685071745\n\n")

        usernamei = input("Please Enter your username here (case sensitive): ")
        userpassi = input("Enter your password here: ")

#----------------------------------------------------------------------------------------------------------------------------------------

        '''
            VERY IMPORTANT NOTE: 
        
            to change or add more managers or diffrent id or passwords you can use this if condtion below
            to add/change/delete new managers or old ones

        '''

        if usernamei == "Aryan" and userpassi == "Gay1":
            print("\n--------------------------------------------------------------------------------------------------------------\n")
            print(f"\t\t\tWelcome {usernamei}, login date and time : {dt.datetime.now()}. \n")
            update_manager_logins_log(usernamei, dt.datetime.now())
            print("--------------------------------------------------------------------------------------------------------------\n")

#----------------------------------------------------------------------------------------------------------------------------------------
        
        else:
            print(f"\nFAILED, The username or password is incorrect run program again and try again. username = {usernamei}, password = {userpassi}")
            quit()
            
    except:
        print("\nCOULD NOT CONNECT TO THE DATABASE. \n")
        quit()

    hotel_ui()
    


