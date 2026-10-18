# File: sanjeev_parking_lot_tracker_part_b.py
# Description: This is Part B of the assessment (parking lot tracker). It uses OOP, which was different from the procedural solution from Part A that I made previously.
# Author: Sanjeev J
# Date created: 04/10/2026

class ParkingBay:

# this is the constructor; it initialises the attributes (that are private) so that it restricts unauthorised access from users
    def __init__(self, bayNumber):
        self.__bayNumber = bayNumber
        self.__s_plate = ""
        self.__occupancy = False

    # this is a mutator method that will record the entry of a car in the parking bay (the list of objects). True is returned upon successful parking, and basic validation is included.
    def parkCar(self, s_plate):
        if self.__occupancy:
            print("Error: Bay is already occupied.")
            return False
        elif s_plate == "":
            print("Error: Plate number cannot be empty.")
            return False
        else:
            self.__s_plate = s_plate
            self.__occupancy = True
            return True
    # this is the second mutator method that will remove the car. It validates whether the user is trying to remove from an unoccupied bay (to which it denies it and displays an error), and removes it successfully if no user input flaws are there.
    def removeCar(self):
        if not self.__occupancy:
            print("Error: Bay is already empty.")
            return False
        else:
            self.__s_plate = ""
            self.__occupancy = False
            return True

# this is 3rd method (1st getter) under the class that will return the boolean value. Since I initialised it as private, the user will use this public method to access it.
    def isOccupied(self):
        return self.__occupancy



# this is the 4th method (2nd getter) which returns the bay number of a given one.
    def getBayNumber(self):
        return self.__bayNumber



# this is the 5th method (3rd getter) which will return the license plate. The task sheet says for purposes of "display or saving", and I'll figure the display part out later.
    def getPlate(self):
        return self.__s_plate


# everything from here onwards stay outside the class; the communicate with one another when the public method is called to access the lstBays.


def viewStatus(lstBays):
    bay_symbols = []
    for bay in lstBays:
        # I think you call the public method here instead of directly accessing the list (and the .txt file)
        if bay.isOccupied():
            s_plate = bay.getPlate()
            # I am going to implement the feedback Ms Constanza has given me, and include the license plates on occupied bays as well.
            bay_symbols.append(f" {s_plate} ")
        else:
            bay_symbols.append(" Free ")

    print(f"""
    
        -------------------- -------------------- -------------------- -------------------- --------------------      
       |       Bay 1:       |        Bay 2:      |        Bay 3:      |        Bay 4:      |        Bay 5:      |
       |{bay_symbols[0]:^20}|{bay_symbols[1]:^20}|{bay_symbols[2]:^20}|{bay_symbols[3]:^20}|{bay_symbols[4]:^20}|
       |                    |                    |                    |                    |                    |
        -------------------- -------------------- -------------------- -------------------- --------------------
        -------------------- -------------------- -------------------- -------------------- --------------------      
       |       Bay 6:       |        Bay 7:      |        Bay 8:      |        Bay 9:      |        Bay 10:     |
       |{bay_symbols[5]:^20}|{bay_symbols[6]:^20}|{bay_symbols[7]:^20}|{bay_symbols[8]:^20}|{bay_symbols[9]:^20}|
       |                    |                    |                    |                    |                    |
        -------------------- -------------------- -------------------- -------------------- --------------------
        
        """)

def calculateTotals(lstBays):
    free_bays = 0
    occupied_bays = 0


    for bay in lstBays:
        if bay.isOccupied():
            occupied_bays += 1
        else:
            free_bays += 1
# I will add something to show the total number of bays; I feel like adding occupied bays and free bays is more appropriate than setting a default value of 10 for total bays
    total_bays = free_bays + occupied_bays

    print("The number of free bays available is: " + str(free_bays))
    print("The number of occupied bays available is: " + str(occupied_bays))
    print("The number of total bays are: " + str(total_bays))

def recordEntry(lstBays):
    s_bay = input("Please enter bay number to enter your car (1 - 10): ")

# I have implemented my Part A feedback here; in case the bay count expands in size, my validation is scalable and doesn't need to be modified (I've referenced the .isdigit() built-in function in my documentation)
# Link: https://www.geeksforgeeks.org/python/python-string-isdigit-method/
    while not s_bay.isdigit() or not (1 <= int(s_bay) <= len(lstBays)):
        print("Invalid bay number. Please choose between 1 and 10.")
        s_bay = input("Please enter bay number to enter your car (1 - 10): ")

    i_bay = int(s_bay)
    # Since lists are zero index, I make sure to subtract one to prevent errors in the boundary numbers (without it, bay 10 from user input could mean bay 11 which would not exist)
    desired_bay = lstBays[i_bay - 1]

    if desired_bay.isOccupied():
        print("Sorry, the bay is already occupied.")
    else:
        s_plate = input("Please enter your license plate: ")

        while s_plate == "":
            print("Error: Number plate cannot be empty.")
            s_plate = input("Please enter your license plate: ")

    # I just realised that I need to call the public method somewhere within the function, so I'm assigning it to a variable so it gets called (given that if it passes the validation checks)
        desired_bay.parkCar(s_plate)
        print("Success! Your car " + s_plate + " has been parked in " + s_bay)

def removeCar(lstBays):
    s_bay = input("Please enter bay number to remove your car (1 - 10): ")

# This is the other line where I've implemented my Part A feedback on validation
    while not s_bay.isdigit() or not (1 <= int(s_bay) <= len(lstBays)):
        print("Invalid bay number. Please choose between 1 and 10.")
        s_bay = input("Please enter bay number to remove your car (1 - 10): ")


    i_bay = int(s_bay)
    desired_bay = lstBays[i_bay - 1]

    if not desired_bay.isOccupied():
        print("Error: Bay is already empty. ")
    else:
        desired_bay.removeCar()
        print("Success! Your car has been removed.")

def displayMenu():
    lstBays = [
        ParkingBay(1),
        ParkingBay(2),
        ParkingBay(3),
        ParkingBay(4),
        ParkingBay(5),
        ParkingBay(6),
        ParkingBay(7),
        ParkingBay(8),
        ParkingBay(9),
        ParkingBay(10),
    ]

    loadData(lstBays)

    while_running = True
    while while_running:
        print("Hello! Below are the menu options for Sanjeev's Parking Lot Tracker:")
        print("1. Record car entering the bay")
        print("2. Remove car from bay")
        print("3. View status of bays")
        print("4. Display statistics ")
        print("5. Save data and exit")

        user_choice = input("Please select an option from 1-5: ")

        while not user_choice.isdigit() or not (1 <= int(user_choice) <= len(lstBays)):
            print("Invalid choice. Please choose only provided menu options")
            user_choice = input("Please select an option from 1-5: ")

        if user_choice == "1":
            print("Option 1 selected.")
            recordEntry(lstBays)
        elif user_choice == "2":
            removeCar(lstBays)
        elif user_choice == "3":
            print("Option 3 selected.")
            viewStatus(lstBays)
        elif user_choice == "4":
            calculateTotals(lstBays)
        elif user_choice == "5":
            saveData(lstBays)
            while_running = False
            print("The program will exit now. Thank you for using the program.")

        else:
            print("Error: Selection not valid. Please choose only the provided options (1-5)")


# File: sj_parking_lot_tracker_part_b.py (the file-related functions branch)
# Description: The branch of Part B assessment that is used to code the file-related functions.
# Author: Sanjeev J
# Date created: 12/10/2026
def saveData(lstBays):
    file = open("parking_data.txt", "w")
    # If I've coded this correctly, the only difference I see between part a & b is that I replace the bottom 3 lines of code with the public methods instead.
    for bay in lstBays:
        if bay.isOccupied():
            bayNumber = bay.getBayNumber()
            s_plate = bay.getPlate()
            b_occupied = bay.isOccupied()
            file.write(str(bayNumber) + "," + s_plate + "," + str(b_occupied) + "\n")
    file.close()
    print("Thank you user. Your data has been successfully saved to parking_data.txt")


def loadData(lstBays):
    try:
        file = open("parking_data.txt", "r")
        for line in file:
            clean_line = line.strip()
            if clean_line != "":
                list_data = clean_line.split(",")

                i_bay = int(list_data[0])
                s_plate = list_data[1]
                s_occupied = list_data[2]

                if s_occupied == "True":
                    lstBays[i_bay - 1].parkCar(s_plate)

        file.close()
        print("Thank you user. The data has been successfully loaded from parking_data.txt")
        # This is where I got inspiration for the try-except structure: https://realpython.com/ref/builtin-exceptions/filenotfounderror/
    except FileNotFoundError:
        print("Unfortunately, your file cannot be loaded to this program at the moment. Please ensure that the parking_data.txt file exists.")

displayMenu()







