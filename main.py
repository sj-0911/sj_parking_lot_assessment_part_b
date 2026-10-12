# File: sj_parking_lot_tracker_part_b.py (the file-related functions branch)
# Description: The branch of Part B assessment that is used to code the file-related functions.
# Author: &lt;Student Name&gt;
# Date created: &lt;Date&gt;
def saveData():
    file = open("parking_data.txt", "w")
    # If I've coded this correctly, the only difference I see is that I replace the bottom 3 lines of code with the public methods instead.
    for bay in lstBays:
        bayNumber = bay.getBayNumber()
        s_plate = bay.getPlate()
        b_occupied = bay.isOccupied()
# i asked gemini (the ai engine) about adding a "\n" at the end of the file.write() built in function; i've put a screenshot of the chat in my documentation
        file.write(str(bayNumber) + "," + s_plate + "," + str(b_occupied) + "\n")
    file.close()
    print("Thank you user. Your data has been successfully saved to parking_data.txt")