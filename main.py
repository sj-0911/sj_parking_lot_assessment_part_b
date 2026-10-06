# File: sanjeev_parking_lot_tracker_part_b.py
# Description: This is Part B of the assessment (parking lot tracker). It uses OOP, which was different from the procedural solution from Part A that I made previously.
# Author: Sanjeev J
# Date created: 04/10/2026

class ParkingBay:

# this is the constructor; it initialises the attributes (that are private) so that it restricts unauthorised access from users
    def __init__(self, bayNumber):
        self.__bayNumber = bayNumber
        self.__number_plate = ""
        self.__occupancy = False

    def parkCar(self, plate):





    def removeCar():



# this is 3rd method (1st getter) under the class that will return the boolean value. Since I initialised it as private, the user will use this public method to access it.
    def isOccupied(self):
        return self.__occupancy



# this is the 4th method (2nd getter) which returns the bay number of a given one.
    def getBayNumber(self):
        return self.__bayNumber



# this is the 5th method (3rd getter) which will return the license plate. The task sheet says for purposes of "display or saving", and I'll figure the display part out later.
    def getPlate(self):