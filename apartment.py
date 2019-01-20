# IMPORT LIBRARY TO USE THE DATETIME FUNCTION
from datetime import datetime
from datetime import timedelta

# CLASS definition the ApartmentA and ApartmentB object
# ApartmentA
class ApartmentA(object):
    def __init__(self):
        self.type = "Apartment A"
        self.occupant = 0
        self.capacity = 2
        self.bedroom = 2
        self.kitchen = True
        self.laundry = True
        self.bathroom = False
        self.rental = 300
        self.duration = 140
# self. is for initialize attributes of an object
# self. use to create a new object : instance
    # used to return a string representation of the object
    def __str__(self): 
        return "This bedroom can be occupied by " + str(self.capacity) + ". This unit consists of 2 bedrooms. " + \
               "There are kitchen and laundry facilities available for use. The price for rental is " + str(self.rental) + "\n" + \
               "----------------------------------------------------------\n" + \
               "PAYMENT DETAILS:\n" + \
               "Utility charges:\t\tRM100\n" + \
               "Rental deposit:\t\t\tRM300\n" + \
               "Rental for current month:\tRM300\n"+ \
               "Total payment:\t\t\tRM700\n" + \
               "----------------------------------------------------------\n"

# ApartmentB
class ApartmentB(object):
    def __init__(self):
        self.type = "Apartment B"
        self.occupant = 0
        self.capacity = 3
        self.bedroom = 2
        self.master_bedroom = 1
        self.kitchen = False
        self.laundry = False
        self.bathroom = True
        self.rental = 200
        self.master_rental = self.rental + (self.rental * 0.4)
        self.duration = 140

    # used to return a string representation of the object
    def __str__(self):
        return "APARTMENT DESCRIPTION:\n" +  \
               "This bedroom can be occupied by " + str(self.capacity) + ". This unit consists of 3 bedrooms, " + \
               "which one of it is a master bedroom with attached bathroom but there are no kitchen and laundry facilities available for use. " + \
               "The price for rental is " + str(self.rental) + ", but for students staying in the master bedroom will be paying an additional 40%, " + \
               "which result in a total of " + str(self.master_rental) + "\n" + \
               "----------------------------------------------------------\n" + \
               "PAYMENT DETAILS FOR REGULAR ROOM:\n" + \
               "Utility charges:\t\tRM100\n" + \
               "Rental deposit:\t\t\tRM200\n" + \
               "Rental for current month:\tRM200\n"+ \
               "Total payment:\t\t\tRM500\n" + \
               "----------------------------------------------------------\n" + \
               "PAYMENT DETAILS FOR MASTER ROOM:\n" + \
               "Utility charges:\t\tRM100\n" + \
               "Rental deposit:\t\t\tRM280\n" + \
               "Rental for current month:\tRM280\n"+ \
               "Total payment:\t\t\tRM660\n" + \
               "----------------------------------------------------------\n"

# LIST definition
a_available = [ApartmentA(), ApartmentA(), ApartmentA(), ApartmentA(), ApartmentA()]
b_available = [ApartmentB(), ApartmentB(), ApartmentB(), ApartmentB(), ApartmentB()]
# store the details of the occupant in the form of tuple data structure, will be updated when the file is opened
a_occupant_list = []
b_occupant_list = []
# removed student after the loop
a_occupant_list_kicked = []
b_occupant_list_kicked = []
# store the number of student that lives in apartment A and apartment B
a_occupant_number = 0
b_occupant_number = 0
# store the details of the student kicked out
a_occupant_kicked = []
b_occupant_kicked = []

### FUNCTION definition ###
def print_menu():
    print("Here is the list of available features of this program: ")
    print("1. Check-in")
    print("2. Check-out")
    print("3. Look up the apartment state")
    print("4. Search for a student")
    print("5. Exit program")

def look_apartment_state():
    # if there is any student in any apartment A or apartment B
    if (len(a_occupant_list) + len(b_occupant_list) > 0):
        for check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number in a_occupant_list:
            print("----------------------------------------")
            print("### STUDENT DETAILS ###")
            print("Name: " + name)
            print("StudentID: " + TPNumber)
            print("Apartment type: " + apartment_type)
            print("Bedroom type: " + bedroom_type.upper())
            print("Room number: " + room_number)
            print("Check-out date: " + str(check_out_date_string))
            print("Days remaining: " + str(days_remaining_string))
        
        for check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number in b_occupant_list:
            print("----------------------------------------")
            print("### STUDENT DETAILS ###")
            print("Name: " + name)
            print("StudentID: " + TPNumber)
            print("Apartment type: " + apartment_type)
            print("Bedroom type: " + bedroom_type.upper())
            print("Room number: " + room_number)
            print("Check-out date: " + str(check_out_date_string))
            print("Days remaining: " + str(days_remaining_string))
            
    else:
        print("There is no student registered in either Apartment A or Apartment B.")
    
def search_for_student():
    print("Do you want to search the student based on its name or studentID number?")
    print("1. Search by the name of the student")
    print("2. Search by the studentID of the student")
    option_chosen = ""
    
    # check for the number of feature typed by the user
    while (option_chosen != "1" and option_chosen != "2"):
        option_chosen = input("Please choose one of the features available: ")
        if (option_chosen == "1"):
            student_name = input("Please enter the name of the student: ")
            student_status = student_search_by_name(student_name)
            
            # check if the student was found or not after the search
            # if the student_status is not None, it means the student is in the apartment list
            if (student_status != False):
                print("We found the student in the list. Here is the student details:")
                for check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number in student_status:
                    print("----------------------------------------")
                    print("### STUDENT DETAILS ###")
                    print("Name: " + name)
                    print("StudentID: " + TPNumber)
                    print("Apartment type: " + apartment_type)
                    print("Bedroom type: " + bedroom_type.upper())
                    print("Room number: " + room_number)
                    print("Check-out date: " + str(check_out_date_string))
                    print("Days remaining: " + str(days_remaining_string))
                    print("----------------------------------------")
                    return student_status
            else:
                print("We cannot find the student in the list.")
                return False
                
        elif (option_chosen == "2"):
            student_id = input("Please enter the studentID number of the student: ")
            student_status = student_search_by_id(student_id)
            
            # check if the student was found or not after the search
            # if the student_status is not None, it means the student is in the apartment list
            if (student_status != False):
                print("We found the student in the list. Here is the student details:")
                for check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number in student_status:
                    print("----------------------------------------")
                    print("### STUDENT DETAILS ###")
                    print("Name: " + name)
                    print("StudentID: " + TPNumber)
                    print("Apartment type: " + apartment_type)
                    print("Bedroom type: " + bedroom_type.upper())
                    print("Room number: " + room_number)
                    print("Check-out date: " + str(check_out_date_string))
                    print("Days remaining: " + str(days_remaining_string))
                    print("----------------------------------------")
                    return student_status
            else:
                print("We cannot find the student in the list.")
                return False
            
        else:
            print("We did not recognize your input. Please provide your input in the right format.")
            
def student_search_by_name(student_name):
    # LOOK FOR THE STUDENT IN EACH ROOM AND EACH APARTMENT
    # look for the student in apartmentA
    student_found = False
    student_data = []
    for check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number in a_occupant_list:
        if (student_name == name):
            student_found = True
            student_data.append((check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number))
            break
    
    # if the student is not found on apartmentA, look for the student in apartmentB instead
    for check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number in b_occupant_list:
        if (student_name == name):
            student_found = True
            student_data.append((check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number))
            break
        
    # check the result after looking for the student in the apartment occupant list
    if (student_found == True):
        return student_data
    else:
        return False
    
def student_search_by_id(student_id):
    # LOOK FOR THE STUDENT IN EACH ROOM AND EACH APARTMENT
    # look for the student in apartmentA
    student_found = False
    student_data = []
    for check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number in a_occupant_list:
        if (student_id == TPNumber):
            student_found = True
            student_data.append((check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number))
            break
    
    # if the student is not found on apartmentA, look for the student in apartmentB instead
    for check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number in b_occupant_list:
        if (student_id == TPNumber):
            student_found = True
            student_data.append((check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number))
            break
        
    # check the result after looking for the student in the apartment occupant list
    if (student_found == True):
        return student_data
    else:
        return False
    
def program_start():
    print_menu()
    option_chosen = ""
    
    # check for the number of feature typed by the user
    while (option_chosen != "1" and option_chosen != "2" and option_chosen != "3" and option_chosen != "4" and option_chosen != "5"):
        option_chosen = input("Please choose one of the features available: ")
        if (option_chosen == "1"):
            check_in()
        elif (option_chosen == "2"):
            check_out()
        elif (option_chosen == "3"):
            look_apartment_state()
        elif (option_chosen == "4"):
            search_for_student()
        elif (option_chosen == "5"):
            break
        else:
            print("We did not recognize your input. Please provide your input in the right format.")
            
def read_data():
    # OPEN AND READ THE LATEST STATUS OF THE APARTMENT
    try:
        f = open("apartment_state.txt", "r")
        # read the file line by line
        line = f.readline()
        # read the file and update the state of apartment A
        for i in range(len(a_available)):
            # read the last character on the file and assign it to the occupant
            a_available[i].occupant = int(line[-2])
            # after using the data on the current line, read and use the data on the next line
            line = f.readline()

        # read the file and update the state of apartment B
        for i in range(len(b_available)):
            b_available[i].occupant = int(line[29])
            b_available[i].bedroom = int(line[59])
            b_available[i].master_bedroom = int(line[88])
            # after using the data on the current line, read and use the data on the next line
            line = f.readline()

    # DO NOT FORGET TO CLOSE THE FILE AFTER FINISHED USING IT, WHETHER IT IS SUCCESSFUL OR NOT WHEN OPENING THE FILE
    finally:
        f.close()

    try:
        f = open("apartment_state.txt", "r")
        # GET THE LIST OF ALL THE LINES IN THE TEXTFILE
        lineList = f.readlines()
        # read the file and update the occupant number of apartment A
        a_occupant_number = int(lineList[-2][-2])
        # read the file and update the occupant number of apartment B
        b_occupant_number = int(lineList[-1][-2])

    # DO NOT FORGET TO CLOSE THE FILE AFTER FINISHED USING IT, WHETHER IT IS SUCCESSFUL OR NOT WHEN OPENING THE FILE
    finally:
        f.close()

    # RETRIEVE THE DATA FROM THE PROGRAM DATA FILE
    try:
        f = open("program_data.txt", "r")
        # read the file line by line
        line = f.readline()
        # read the file and update the tuple that hold the data of the apartment A occupant
        for i in range(a_occupant_number):
            # put in the data in the empty tuple, restore any data stored in the file to the program
            data_in_string = str(line[:-1])
            # remove the bracket of the tuple in string
            data_in_string = data_in_string[2:-2]
            # clean up the data from unnecessary whitespace and characters, store the data in an array
            data_in_array = data_in_string.split("', '")
            # convert the data to tuple
            data_in_tuple = tuple(data_in_array)
            # add the data in form of tuple to the list
            a_occupant_list.append(data_in_tuple)
            line = f.readline()

        # read the file and update the tuple that hold the data of the apartment B occupant
        for i in range(b_occupant_number):
            # put in the data in the empty tuple, restore any data stored in the file to the program
            data_in_string = str(line[:-1])
            # remove the bracket of the tuple in string
            data_in_string = data_in_string[2:-2]
            # clean up the data from unnecessary whitespace and characters, store the data in an array
            data_in_array = data_in_string.split("', '")
            # convert the data to tuple
            data_in_tuple = tuple(data_in_array)
            # add the data in form of tuple to the list
            b_occupant_list.append(data_in_tuple)
            line = f.readline()
            
    # DO NOT FORGET TO CLOSE THE FILE AFTER FINISHED USING IT, WHETHER IT IS SUCCESSFUL OR NOT WHEN OPENING THE FILE
    finally:
        f.close()

def write_data():
    # UPDATE THE STATUS OF THE APARTMENT WHEN THE PROGRAM EXITS
    ### UPDATE THE APARTMENT_STATE FIRST ###
    # check the student living status in apartmentA
    for check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number in a_occupant_list:
        # convert the date as a string into date as an object to calculate the days remaining
        check_out_datetime_string = check_out_date_string
        check_out_datetime_object = datetime.date(datetime.strptime(check_out_datetime_string, '%Y-%m-%d'))
        current_date = datetime.date(datetime.now())
        days_remaining = str((check_out_datetime_object - current_date).days)
        # CHECK IF THE STUDENT LIVES BEYOND THE TIME LIMIT, ONLY WRITE THE DATA ON THE FILE IF THE STUDENT STILL ALLOWED TO LIVE IN THE APARTMENT
        if (int(days_remaining) <= 0):
            # check the student belongs to which apartment and which room number to update the apartment room status back to available
            a_available[int(room_number)].occupant -= 1
            a_available[int(room_number)].bedroom += 1
            # add it to the report at the end of the program running
            # convert the data to tuple
            data_in_tuple_kicked = tuple([name, TPNumber, apartment_type, bedroom_type, room_number])
            data_in_tuple_list = tuple([check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number])
            # add the data in form of tuple to the list
            a_occupant_kicked.append(data_in_tuple_kicked)
            a_occupant_list_kicked.append(data_in_tuple_list)
            # reduce the occupant number due to the student being kicked out of the apartment
            global a_occupant_number
            a_occupant_number -= 1
    
    # kick out the student after looping
    for i in range(len(a_occupant_list_kicked)):
        if (a_occupant_list_kicked[i] in a_occupant_list):
            a_occupant_list.remove(a_occupant_list_kicked[i])
    
    # check the student living status in apartmentB
    for check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number in b_occupant_list:
        # convert the date as a string into date as an object to calculate the days remaining
        check_out_datetime_string = check_out_date_string
        check_out_datetime_object = datetime.date(datetime.strptime(check_out_datetime_string, '%Y-%m-%d'))
        current_date = datetime.date(datetime.now())
        days_remaining = str((check_out_datetime_object - current_date).days)
        # CHECK IF THE STUDENT LIVES BEYOND THE TIME LIMIT, ONLY WRITE THE DATA ON THE FILE IF THE STUDENT STILL ALLOWED TO LIVE IN THE APARTMENT
        if (int(days_remaining) <= 0):
            # check the student belongs to which apartment and which room number to update the apartment room status back to available
            if (bedroom_type == "R"):
                b_available[int(room_number)].occupant -= 1
                b_available[int(room_number)].bedroom += 1
                # add it to the report at the end of the program running
                # convert the data to tuple
                data_in_tuple_kicked = tuple([name, TPNumber, apartment_type, bedroom_type, room_number])
                data_in_tuple_list = tuple([check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number])
                # add the data in form of tuple to the list
                b_occupant_kicked.append(data_in_tuple_kicked)
                b_occupant_list_kicked.append(data_in_tuple_list)
                # reduce the occupant number due to the student being kicked out of the apartment
                global b_occupant_number
                b_occupant_number -= 1
                
            # if it is a master bedroom
            elif (bedroom_type == "M"):
                b_available[int(room_number)].occupant -= 1
                b_available[int(room_number)].master_bedroom += 1
                # add it to the report at the end of the program running
                # convert the data to tuple
                data_in_tuple_kicked = tuple([name, TPNumber, apartment_type, bedroom_type, room_number])
                data_in_tuple_list = tuple([check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number])
                # add the data in form of tuple to the list
                b_occupant_kicked.append(data_in_tuple_kicked)
                b_occupant_list_kicked.append(data_in_tuple_list)
                # reduce the occupant number due to the student being kicked out of the apartment
                b_occupant_number -= 1

    # kick out the student after looping
    for i in range(len(b_occupant_list_kicked)):
        if (b_occupant_list_kicked[i] in b_occupant_list):
            b_occupant_list.remove(b_occupant_list_kicked[i])
    
    ### ###
    try:
        f = open("apartment_state.txt", "w")
        # check and write down the occupied space in APARTMENT A
        for i in range(len(a_available)):
            f.write(a_available[i].type + " Room " + str(i) + " occupant: " + str(a_available[i].occupant) + "\n")

        # check and write down the occupied space in APARTMENT B
        for i in range(len(b_available)):
            f.write(b_available[i].type + " Room " + str(i) + " occupant: " + str(b_available[i].occupant) + ", regular bedroom available: " + str(b_available[i].bedroom) + \
                    ", master bedroom available: " + str(b_available[i].master_bedroom) + "\n")

        # check and write down the student and unit occupied in APARTMENT A
        # write the data in a human-readable format
        for check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number in a_occupant_list:
            # convert the date as a string into date as an object to calculate the days remaining
            check_out_datetime_string = check_out_date_string
            check_out_datetime_object = datetime.date(datetime.strptime(check_out_datetime_string, '%Y-%m-%d'))
            current_date = datetime.date(datetime.now())
            days_remaining = str((check_out_datetime_object - current_date).days)
            # CHECK IF THE STUDENT LIVES BEYOND THE TIME LIMIT, ONLY WRITE THE DATA ON THE FILE IF THE STUDENT STILL ALLOWED TO LIVE IN THE APARTMENT
            if (int(days_remaining) > 0):
                f.write("Check out date: " + check_out_date_string + ", days remaining: " + days_remaining + ", name: " + name + \
                    ", StudentID: " + TPNumber + ", apartment type " + apartment_type +  ", bedroom_type: " +  bedroom_type + ", room number: " + room_number + "\n")
            
        # check and write down the student and unit occupied in APARTMENT B
        # write the data in a human-readable format
        for check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number in b_occupant_list:
            # convert the date as a string into date as an object to calculate the days remaining
            check_out_datetime_string = check_out_date_string
            check_out_datetime_object = datetime.date(datetime.strptime(check_out_datetime_string, '%Y-%m-%d'))
            current_date = datetime.date(datetime.now())
            days_remaining = str((check_out_datetime_object - current_date).days)
            # CHECK IF THE STUDENT LIVES BEYOND THE TIME LIMIT, ONLY WRITE THE DATA ON THE FILE IF THE STUDENT STILL ALLOWED TO LIVE IN THE APARTMENT
            if (int(days_remaining) > 0):
                f.write("Check out date: " + check_out_date_string + ", days remaining: " + days_remaining + ", name: " + name + \
                    ", StudentID: " + TPNumber + ", apartment type " + apartment_type +  ", bedroom_type: " +  bedroom_type + ", room number: " + room_number + "\n")

        # write down total student living in apartment A
        f.write("Total student living in apartment A: " + str(len(a_occupant_list)) + "\n")

        # write down total student living in apartment B
        f.write("Total student living in apartment B: " + str(len(b_occupant_list)) + "\n")
        
    # DO NOT FORGET TO CLOSE THE FILE AFTER FINISHED USING IT, WHETHER IT IS SUCCESSFUL OR NOT WHEN OPENING THE FILE
    finally:
        f.close()        
            
    # THIS FILE IS INTENDED FOR THE PROGRAM TO STORE THE APARTMENT DATA, NOT FOR THE PROGRAM USER
    try:
        f = open("program_data.txt", "w")
        # check and write down the student and unit occupied in APARTMENT A
        for i in range(len(a_occupant_list)):
            # write the data
            f.write(str(a_occupant_list[i]) + "\n")

        # check and write down the student and unit occupied in APARTMENT B
        for i in range(len(b_occupant_list)):
            # write the data
            f.write(str(b_occupant_list[i]) + "\n")

    # DO NOT FORGET TO CLOSE THE FILE AFTER FINISHED USING IT, WHETHER IT IS SUCCESSFUL OR NOT WHEN OPENING THE FILE
    finally:
        f.close()
        
    # PRINT OUT THE STUDENT THAT WAS KICKED OUT OF THE APARTMENT
    print("LEAVING STUDENTS: ")
    # Apartment A kicked out list
    if ((len(a_occupant_kicked) == 0) and (len(b_occupant_kicked) == 0)):
        print("No student is leaving today.")
        
    for name, TPNumber, apartment_type, bedroom_type, room_number in a_occupant_kicked:
        print("----------------------------------------------------------")
        print("Name: " + name)
        print("StudentID: " + TPNumber)
        print("Apartment type: " + apartment_type)
        print("Bedroom type: " + bedroom_type)
        print("Room number: " + room_number)

    # Apartment B kicked out list
    for name, TPNumber, apartment_type, bedroom_type, room_number in b_occupant_kicked:
        print("----------------------------------------------------------")
        print("Name: " + name)
        print("StudentID: " + TPNumber)
        print("Apartment type: " + apartment_type)
        print("Bedroom type: " + bedroom_type)
        print("Room number: " + room_number)

def check_in():
    # current state of the program, whether it is still running or not. Consider as the "flag" of the program that determines when the program terminates
    program_running = True
    while (program_running != False):
        name = input("Please enter the name of the student: ")
        TPNumber = input("Please enter the student identification number: ")
        # current status of the student before register for an apartment room
        student_get_room = False
        
        # CHECK FOR TPNUMBER BEFORE UPDATING THE APARTMENT STATUS
        # check the TPNumber of the student that lives in Apartment A
        def check_for_student(list_provided_a, list_provided_b):
            for check_out_date_string, days_remaining_string, nameInList, TPNumberInList, apartment_type, bedroom_type, room_number in list_provided_a:
                if (TPNumber == TPNumberInList):
                    print("The student is already registered in the apartment list.")
                    return False
            # check the TPNumber of the student that lives in Apartment B
            for check_out_date_string, days_remaining_string, nameInList, TPNumberInList, apartment_type, bedroom_type, room_number in list_provided_b:
                if (TPNumber == TPNumberInList):
                    print("The student is already registered in the apartment list.")
                    return False
        
        # execute the function
        student_found = check_for_student(a_occupant_list, b_occupant_list)
        if (student_found == False):
            return
            
        # ask for the current time and date, and convert it into date format YYYY-MM-DD
        check_in_date = datetime.date(datetime.now())
        # add 140 days for check-out date
        check_out_date = datetime.date(datetime.now() + timedelta(days=140))
        days_remaining = (check_out_date - datetime.date(datetime.now())).days
        
        # search for a room for the student WHILE the student does not have a room
        while (student_get_room != True):
            apartment_requested = input("Please select the type of apartment that you want (A/B) ")
            apartment_type = None

            # check for the apartment type selected by the user
            while ((apartment_type != "A") or (apartment_type != "B")):
                if (apartment_requested.upper() == "A"):
                    print("ApartmentA")
                    apartment_type = "ApartmentA"
                    print(ApartmentA())
                    break
                
                elif (apartment_requested.upper() == "B"):
                    print("ApartmentB")
                    apartment_type = "ApartmentB"
                    print(ApartmentB())
                    break
                
                else:
                    print("Sorry, we do not have that type of apartment.")
                    apartment_requested = input("Please select the type of apartment that you want (A/B) ")

            # ASSIGN STUDENT TO APARTMENT A
            if (apartment_type == "ApartmentA"):
                # bedroom type is regular by default
                bedroom_type = "R"
                # iterate through every room in apartmentA to find an available space for the student
                for i in range(len(a_available)):
                    if (a_available[i].occupant < a_available[i].capacity):
                        global a_occupant_number
                        a_occupant_number += 1
                        a_available[i].occupant += 1
                        a_available[i].bedroom -= 1
                        apartment_type = a_available[i].type
                        
                        student_get_room = True
                        # print the details of the student apartment room assignment
                        print("Student assigned to ApartmentA unit, room number " + str(i))
                        print("Total occupant(s): " + str(a_available[i].occupant))
                        print("----------------------------------------")
                        print("### STUDENT DETAILS ###")
                        print("Name: " + name)
                        print("StudentID: " + TPNumber)
                        print("Apartment type: " + apartment_type)
                        print("Bedroom type: " + bedroom_type.upper())
                        print("Room number: " + str(i))
                        print("Check-in date: " + str(check_in_date))
                        print("Check-out date: " + str(check_out_date))
                        print("----------------------------------------")

                        # update the file with details of the student in the form of tuple data structure
                        # the first item is CHECKOUT DATE
                        a_occupant_list.append((str(check_out_date), str(days_remaining), name, TPNumber, apartment_type, bedroom_type.upper(), str(i)))
                        break

            # ASSIGN STUDENT TO APARTMENT B
            elif (apartment_type == "ApartmentB"):
                # ask if the student want a regular or master bedroom, initialize the variable in an empty state
                bedroom_type = ""
                # check for the format of the input, testing the input
                while ((bedroom_type.upper() != "R") and (bedroom_type.upper() != "M")):
                    bedroom_type = input("Which bedroom type do you want? Regular or Master? (R/M) ")
                    if (bedroom_type.upper() == "M"):
                        # iterate through every MASTER room in apartmentB to find an available space for the student
                        for i in range(len(b_available)):
                            # check if the occupant is not full AND there is a master bedroom available
                            if (b_available[i].occupant < b_available[i].capacity and b_available[i].master_bedroom != 0 and student_get_room == False):
                                global b_occupant_number
                                b_occupant_number += 1
                                b_available[i].occupant += 1
                                b_available[i].master_bedroom -= 1
                                apartment_type = b_available[i].type
                                
                                student_get_room = True
                                # print the details of the student apartment room assignment
                                print("Student assigned to ApartmentB unit, room number " + str(i))
                                print("Total occupant(s): " + str(b_available[i].occupant))
                                print("----------------------------------------")
                                print("### STUDENT DETAILS ###")
                                print("Name: " + name)
                                print("StudentID: " + TPNumber)
                                print("Apartment type: " + apartment_type)
                                print("Bedroom type: " + bedroom_type.upper())
                                print("Room number: " + str(i))
                                print("Check-in date: " + str(check_in_date))
                                print("Check-out date: " + str(check_out_date))
                                print("----------------------------------------")
                                # update the file with details of the student in the form of tuple data structure
                                # the first item is CHECKOUT DATE
                                b_occupant_list.append((str(check_out_date), str(days_remaining), name, TPNumber, apartment_type, bedroom_type.upper(), str(i)))
                                break

                        if (student_get_room == False):
                            # if the program reach here, it means there is no master bedroom available, search for regular room instead
                            change_bedroom_type = ""
                            # check for the format of the input, testing the input
                            while ((change_bedroom_type.upper() != "Y") and (change_bedroom_type.upper() != "N")):
                                change_bedroom_type = input("We cannot find any empty master bedroom in apartment B. Do you want to search " + \
                                                        "for a regular bedroom instead? (Y/N) ")
                                if (change_bedroom_type.upper() == "Y"):
                                    bedroom_type = "R"
                                    # iterate through every REGULAR room in apartmentB to find an available space for the student
                                    for i in range(len(b_available)):
                                        # check if the occupant is not full AND there is a regular bedroom available
                                        if (b_available[i].occupant < b_available[i].capacity and b_available[i].bedroom != 0 and student_get_room == False):
                                            b_occupant_number += 1
                                            b_available[i].occupant += 1
                                            b_available[i].bedroom -= 1
                                            apartment_type = b_available[i].type
                                            
                                            student_get_room = True
                                            # print the details of the student apartment room assignment
                                            print("Student assigned to ApartmentB unit, room number " + str(i))
                                            print("Total occupant(s): " + str(b_available[i].occupant))
                                            print("----------------------------------------")
                                            print("### STUDENT DETAILS ###")
                                            print("Name: " + name)
                                            print("StudentID: " + TPNumber)
                                            print("Apartment type: " + apartment_type)
                                            print("Bedroom type: " + bedroom_type.upper())
                                            print("Room number: " + str(i))
                                            print("Check-in date: " + str(check_in_date))
                                            print("Check-out date: " + str(check_out_date))
                                            print("----------------------------------------")
                                            # update the file with details of the student in the form of tuple data structure
                                            # the first item is CHECKOUT DATE
                                            b_occupant_list.append((str(check_out_date), str(days_remaining), name, TPNumber, apartment_type, bedroom_type.upper(), str(i)))
                                            break

                                    # IF THE STUDENT STILL DOES NOT GET A ROOM, IT MEANS NO ROOM AVAILABLE FOR TYPE B
                                    if (student_get_room == False):
                                        print("We cannot get a room")
                                
                                elif (change_bedroom_type.upper() == "N"):
                                    # continue the program flow, jump to conclusion that the room is not available for the student
                                    break
                                else:
                                    print("We did not recognize your input. Please provide your input in the right format.")
                            
                    elif (bedroom_type.upper() == "R"):
                        # iterate through every REGULAR room in apartmentB to find an available space for the student
                        for i in range(len(b_available)):
                            # check if the occupant is not full AND there is a regular bedroom available
                            if (b_available[i].occupant < b_available[i].capacity and b_available[i].bedroom != 0 and student_get_room == False):
                                b_occupant_number += 1
                                b_available[i].occupant += 1
                                b_available[i].bedroom -= 1
                                apartment_type = b_available[i].type
                                
                                student_get_room = True
                                # print the details of the student apartment room assignment
                                print("Student assigned to ApartmentB unit, room number " + str(i))
                                print("Total occupant(s): " + str(b_available[i].occupant))
                                print("----------------------------------------")
                                print("### STUDENT DETAILS ###")
                                print("Name: " + name)
                                print("StudentID: " + TPNumber)
                                print("Apartment type: " + apartment_type)
                                print("Bedroom type: " + bedroom_type.upper())
                                print("Room number: " + str(i))
                                print("Check-in date: " + str(check_in_date))
                                print("Check-out date: " + str(check_out_date))
                                print("----------------------------------------")
                                # update the file with details of the student in the form of tuple data structure
                                # the first item is CHECKOUT DATE
                                b_occupant_list.append((str(check_out_date), str(days_remaining), name, TPNumber, apartment_type, bedroom_type.upper(), str(i)))
                                break

                        if (student_get_room == False):
                            # if the program reach here, it means there is no regular bedroom available, search for master room instead
                            change_bedroom_type = ""
                            # check for the format of the input, testing the input
                            while ((change_bedroom_type.upper() != "Y") and (change_bedroom_type.upper() != "N")):
                                change_bedroom_type = input("We cannot find any empty regular bedroom in apartment B. Do you want to search " + \
                                                        "for a master bedroom instead? (Y/N) ")
                                if (change_bedroom_type.upper() == "Y"):
                                    bedroom_type = "M"
                                    # iterate through every REGULAR room in apartmentB to find an available space for the student
                                    for i in range(len(b_available)):
                                        # check if the occupant is not full AND there is a regular bedroom available
                                        if (b_available[i].occupant < b_available[i].capacity and b_available[i].master_bedroom != 0 and student_get_room == False):
                                            b_occupant_number += 1
                                            b_available[i].occupant += 1
                                            b_available[i].master_bedroom -= 1
                                            apartment_type = b_available[i].type
                                            
                                            student_get_room = True
                                            # print the details of the student apartment room assignment
                                            print("Student assigned to ApartmentB unit, room number " + str(i))
                                            print("Total occupant(s): " + str(b_available[i].occupant))
                                            print("----------------------------------------")
                                            print("### STUDENT DETAILS ###")
                                            print("Name: " + name)
                                            print("StudentID: " + TPNumber)
                                            print("Apartment type: " + apartment_type)
                                            print("Bedroom type: " + bedroom_type.upper())
                                            print("Room number: " + str(i))
                                            print("Check-in date: " + str(check_in_date))
                                            print("Check-out date: " + str(check_out_date))
                                            print("----------------------------------------")
                                            # update the file with details of the student in the form of tuple data structure
                                            # the first item is CHECKOUT DATE
                                            b_occupant_list.append((str(check_out_date), str(days_remaining), name, TPNumber, apartment_type, bedroom_type.upper(), str(i)))
                                            # if the student has been assigned a room, no need to check for another available room
                                            break
                                        
                                    # IF THE STUDENT STILL DOES NOT GET A ROOM, IT MEANS NO ROOM AVAILABLE FOR TYPE B
                                    if (student_get_room == False):
                                        print("We cannot get a room")
                                        
                                elif (change_bedroom_type == "N"):
                                    # continue the program flow, jump to conclusion that the room is not available for the student
                                    break
                                else:
                                    print("We did not recognize your input. Please provide your input in the right format.")

                    else:
                        print("We did not recognize your input. Please provide your input in the right format.")

                    
            # check after iterating through the apartment unit, whether the student get a room or still does not get a room
            if (student_get_room == False):
                print("We are sorry. We cannot find your requested room in apartment " + apartment_type + ". Please choose another type of room or apartment unit.")
                request_again = ""
                
                # check for the format of the input, testing the input
                while ((request_again.upper() != "Y") and (request_again.upper() != "N")):
                    request_again = input("Do you want to request for another apartment unit? (Y/N) ")
                    # check if the student want to request for a room again
                    if (request_again.upper() == "Y"):
                        # start the program again, this time from requesting the room
                        student_get_room = False
                    elif (request_again.upper() == "N"):
                        # END THE PROGRAM, USING THE FLAG DECLARED AT THE START OF THE PROGRAM
                        student_get_room = True
                        program_running = False
                    else:
                        print("We did not recognize your input. Please provide your input in the right format.")
                    
            elif (student_get_room == True):
                register_another = ""
                while ((register_another.upper() != "Y") and (register_another.upper() != "N")):
                    register_another = input("You have been assigned a room. Do you want to register another student? (Y/N) ")
                    if (register_another.upper() == "Y"):
                        # RESET THE PROGRAM FLAG
                        program_running = True
                    elif (register_another.upper() == "N"):
                        # END THE PROGRAM, USING THE FLAG DECLARED AT THE START OF THE PROGRAM
                        student_get_room = True
                        program_running = False
                    else:
                        print("We did not recognize your input. Please provide your input in the right format.")

def check_out():
    print("Select the student that you want to check out")
    # will store an array if the data was found, return False if data not found
    student_search = search_for_student()
    if (student_search == False):
        return
    else:
        student_to_be_kicked = None
        for check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number in student_search:
            if (apartment_type == "Apartment A"):
                # check the student belongs to which apartment and which room number to update the apartment room status back to available
                a_available[int(room_number)].occupant -= 1
                a_available[int(room_number)].bedroom += 1
                # add it to the report at the end of the program running
                # convert the data to tuple
                data_in_tuple_kicked = tuple([name, TPNumber, apartment_type, bedroom_type, room_number])
                data_in_tuple_list = tuple([check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number])
                # add the data in form of tuple to the list
                a_occupant_kicked.append(data_in_tuple_kicked)
                student_to_be_kicked = data_in_tuple_list
                global a_occupant_number
                a_occupant_number -= 1
    
                # kick out the student after looping
                a_occupant_list.remove(student_to_be_kicked)
                print("The student has been checked out from the apartment.")
                
            # check the student living status in apartmentB
            elif (apartment_type == "Apartment B"):
                # check the student belongs to which apartment and which room number to update the apartment room status back to available
                if (bedroom_type == "R"):
                    b_available[int(room_number)].occupant -= 1
                    b_available[int(room_number)].bedroom += 1
                    # add it to the report at the end of the program running
                    # convert the data to tuple
                    data_in_tuple_kicked = tuple([name, TPNumber, apartment_type, bedroom_type, room_number])
                    data_in_tuple_list = tuple([check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number])
                    # add the data in form of tuple to the list
                    b_occupant_kicked.append(data_in_tuple_kicked)
                    student_to_be_kicked = data_in_tuple_list
                    global b_occupant_number
                    b_occupant_number -= 1
                    
                    # kick out the student after looping
                    b_occupant_list.remove(student_to_be_kicked)
                    print("The student has been checked out from the apartment.")
                    
                # if it is a master bedroom
                elif (bedroom_type == "M"):
                    b_available[int(room_number)].occupant -= 1
                    b_available[int(room_number)].master_bedroom += 1
                    # add it to the report at the end of the program running
                    # convert the data to tuple
                    data_in_tuple_kicked = tuple([name, TPNumber, apartment_type, bedroom_type, room_number])
                    data_in_tuple_list = tuple([check_out_date_string, days_remaining_string, name, TPNumber, apartment_type, bedroom_type, room_number])
                    # add the data in form of tuple to the list
                    b_occupant_kicked.append(data_in_tuple_kicked)
                    student_to_be_kicked = data_in_tuple_list
                    b_occupant_number -= 1
    
                    # kick out the student after looping
                    b_occupant_list.remove(student_to_be_kicked)
                    print("The student has been checked out from the apartment.")
        
### PROGRAM FLOW STARTS HERE ###
print("Hello, welcome to the student apartment registration system. What can I do for you today? ")
program_running = True

read_data()

while (program_running == True):
    program_start()
    run_again = None
    while (run_again != "Y" and run_again != "N"):
        run_again = input("Do you want to do another operation again? (Y/N) ")
        if (run_again.upper() == "Y"):
            print("Restarting the program...")
            print("----------------------------------------------------------")
            program_running = True
            break
        elif (run_again.upper() == "N"):
            print("Thank you for using our apartment registration service.")
            program_running = False
            break
        else:
            print("We did not recognize your input. Please provide your input in the right format.")
            
write_data()

# Freeze the screen when the program exits
print("----------------------------------------------------------")
input("Press Enter to exit the program...")
