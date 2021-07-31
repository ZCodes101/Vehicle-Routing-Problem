from datetime import *
from Package_Manager import *
from CSV_Data_Reader import *

DAY_STARTING_TIME = "8:00 AM"

# Takes the start of day time, which is 8 AM, updates the wrong address,
# 410 S State St, Salt Lake City, UT 84111
# and get the truck route information before delivering the packages
# insures that the trucks is traveling at a constant 18 mph
# space-time Complexity O(n^2)
def startTheDay(endTime, startTime=DAY_STARTING_TIME):
    currentDateTime = datetime.strptime(startTime, '%I:%M %p')
    endDateTime = datetime.strptime(endTime, '%I:%M %p')
    counter = 0
    while currentDateTime < endDateTime:
        if currentDateTime == datetime.strptime('10:20 AM', '%I:%M %p'):
            get_hash_table().getValue('9')[0:4] = '410 S State St', 'Salt Lake City', 'UT', '84111'
            thirdTruck.leavingTime = '10:20 AM'
        for trck in getTrucks():
            if trck.leavingTime != '':
                if trck.startedToRoute == False and datetime.strptime(trck.leavingTime, '%I:%M %p') <= currentDateTime:
                    trck.startedToRoute = True
                    trck.nextPackage = getDistance('0', getlocationIndex(trck.locations[trck.visitedPoints]))
                    for i in trck.packagesKeys:
                        get_hash_table().getValue(str(i))[7] = 'En Route'
            if trck.startedToRoute and trck.isFinished == False:
                trck.travelledDistance += 18 / 60
                if trck.lengthOfRoute() > trck.travelledDistance:
                    for index in range(len(trck.packagesKeys)):
                        if get_hash_table().getValue(trck.packagesKeys[index])[7] == "En Route":
                            if trck.getDistanceFromStart(index) <= trck.travelledDistance + 18 / 60:
                                counter += 1
                                get_hash_table().getValue(trck.packagesKeys[index])[7] = 'Delivered'
                                get_hash_table().getValue(trck.packagesKeys[index])[9] = currentDateTime.strftime(
                                    '%I:%M %p')
                elif trck.isFinished == False:
                    trck.isFinished = True
        currentDateTime += timedelta(minutes=1)


# Takes the start of day time, which is 8 AM, updates the wrong address,
# 410 S State St, Salt Lake City, UT 84111
# and get the truck route information before delivering the packages
# prints the total of packages successfully delivered before deadline
# insures that the trucks is traveling at a constant 18 mph
# space-time Complexity O(n^2)
def endTheDay(endTime, startTime=DAY_STARTING_TIME):
    currentDateTime = datetime.strptime(startTime, '%I:%M %p')
    endDateTime = datetime.strptime(endTime, '%I:%M %p')
    counter = 0
    while currentDateTime < endDateTime:
        if currentDateTime == datetime.strptime('10:20 AM', '%I:%M %p'):
            get_hash_table().getValue('9')[0:4] = '410 S State St', 'Salt Lake City', 'UT', '84111'
            thirdTruck.leavingTime = '10:20 AM'
        for trck in getTrucks():
            if trck.leavingTime != '':
                if trck.startedToRoute == False and datetime.strptime(trck.leavingTime, '%I:%M %p') <= currentDateTime:
                    trck.startedToRoute = True
                    print(trck.name + " started delivering packages.")
                    trck.nextPackage = getDistance('0', getlocationIndex(trck.locations[trck.visitedPoints]))
                    for i in trck.packagesKeys:
                        get_hash_table().getValue(str(i))[7] = 'En Route'
            if trck.startedToRoute and trck.isFinished == False:
                trck.travelledDistance += 18 / 60
                if trck.lengthOfRoute() > trck.travelledDistance:
                    for index in range(len(trck.packagesKeys)):
                        if get_hash_table().getValue(trck.packagesKeys[index])[7] == "En Route":
                            if trck.getDistanceFromStart(index) <= trck.travelledDistance + 18 / 60:
                                counter += 1
                                get_hash_table().getValue(trck.packagesKeys[index])[7] = 'Delivered'
                                get_hash_table().getValue(trck.packagesKeys[index])[9] = currentDateTime.strftime(
                                    '%I:%M %p')
                                print(trck.name, 'delivered package', trck.packagesKeys[index],
                                      "- Time: %s:%s" % (currentDateTime.hour, currentDateTime.minute))
                elif not trck.isFinished:
                    print(trck.name, "has finished delivery at: ", currentDateTime.hour, ':',
                          currentDateTime.minute)
                    trck.isFinished = True
        currentDateTime += timedelta(minutes=1)
    print(counter, 'packages has been successfully delivered')
    print()
