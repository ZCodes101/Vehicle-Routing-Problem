
from Route import startTheDay,endTheDay
from CSV_Data_Reader import get_hash_table, reset_hash_table
from Package_Manager import getTotalDistance

if __name__ == "__main__":
    # This is the display message that is shown when the user runs the program. The interface is accessible from here
    # The total Space-time complexity of the entire program is O(n^2)
    # Memory and computational time is nearly linear throughout the program
    print('******************************')
    print('WGUPS Package Routing Program!')
    print('******************************\n')
    print('************************************************************')
    print("Total distance traveled: ", getTotalDistance(), "miles")
    print('************************************************************\n')

    inputOption = -1
    # Use a loop for user input; Space-time complexity O(n^2)
    # 1 finds single package at x time,
    # 2 finds all packages at x time
    # 3 prints the trucks delivery route and total miles,
    while inputOption != 0:
        print('Enter 1 to find a single  package by ID number at a specific time',
              '\nEnter 2 to list all packages at a specific time',
              '\nEnter 3 to view the truck routes'
              '\nEnter 0 to exit')

        listB = list(get_hash_table().table)
        inputOption = int(input('> '))
        if inputOption == 1:
            reset_hash_table()
            inputTime1 = input('Enter a time (HH:MM AM/PM): ')
            packageID = input('Enter the package ID Number: ')
            startTheDay(inputTime1)
            for obj in list(get_hash_table().table):
                if obj[0] == packageID:
                    print('Package:', obj[0], obj[1][0], obj[1][4], obj[1][1], obj[1][3], obj[1][5], obj[1][7],
                          obj[1][9])
            print()
            exit()

        elif inputOption == 2:

            inputTime2 = input('Enter a time (HH:MM AM/PM): ')
            startTheDay(inputTime2)
            for obj in listB:
                print('Package:', obj[0], obj[1][0], obj[1][4], obj[1][1], obj[1][3], obj[1][5], obj[1][7], obj[1][9])
            exit()

        elif inputOption == 3:
            inputTime0 = '01:00 PM'
            endTheDay(inputTime0)
            print("Total distance traveled: ", getTotalDistance(), "miles")
            exit(0)
