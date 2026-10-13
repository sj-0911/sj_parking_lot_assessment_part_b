# File: sj_parking_lot_tracker_part_b.py (the file-related functions branch)
# Description: The branch of Part B assessment that is used to code the file-related functions.
# Author: Sanjeev J
# Date created: 12/10/2026
def saveData():
    file = open("parking_data.txt", "w")
    # If I've coded this correctly, the only difference I see is that I replace the bottom 3 lines of code with the public methods instead.
    for bay in lstBays:
        bayNumber = bay.getBayNumber()
        s_plate = bay.getPlate()
        b_occupied = bay.isOccupied()
        file.write(str(bayNumber) + "," + s_plate + "," + str(b_occupied) + "\n")
    file.close()
    print("Thank you user. Your data has been successfully saved to parking_data.txt")

def loadData():
    file = open("parking_data.txt", "r")
    for line in file:
        clean_line = line.strip()
        if clean_line != "":
          list_data = clean_line.split(",")
          
          i_bay = int(list_data[0])
          s_plate = list_data[1]
          s_occupied = list_data[2]

          if s_occupied == "True":
            b_occupied = True
            lstBays[i_bay - 1].parkCar(s_plate)
          else:
            b_occupied = False


    file.close()
    print("Thank you user. The data has been successfully loaded from parking_data.txt")