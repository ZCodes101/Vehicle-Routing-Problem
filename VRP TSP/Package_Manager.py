from CSV_Data_Reader import *


# The Package Manager Class constructs the trucks, add cargo to the trucks, organize the trucks
# calculates the distance between routes then add the cargo on the best truck to deliver to be used in route data
class truck:
    def __init__(self):
        self.name = ''
        self.packagesKeys = []
        self.locations = []
        self.leavingTime = ''
        self.loadedCargo = 0
        self.startedToRoute = False
        self.shouldTurn = False
        self.travelledDistance = 0.0
        self.visitedPoints = 0
        self.nextPackage = 0
        self.isFinished = False

    def addCargo(self, key):
        self.packagesKeys.append(key)
        self.locations.append(get_hash_table().getValue(key)[0])
        self.loadedCargo += 1
        get_hash_table().getValue(key)[8] = "loaded"
    # space-time complexity O(n)
    def lengthOfRoute(self):
        length = getDistance('0', getlocationIndex(self.locations[0]))
        for i in range(len(self.locations) - 1):
            length += getDistance(getlocationIndex(self.locations[i]), getlocationIndex(self.locations[i + 1]))
        if (trck.shouldTurn):
            length += getDistance(getlocationIndex(self.locations[i + 1]), '0')
        return length

    def getRoute(self):
        result = self.locations
        result.insert(0, '0')
        result.append('0')
        return result
# space-time complexity O(n)
    def getDistanceFromStart(self, i):
        length = getDistance('0', getlocationIndex(self.locations[0]))
        for a in range(i):
            length += getDistance(getlocationIndex(self.locations[a]), getlocationIndex(self.locations[a + 1]))
        return length


# Use Nearest Neighbor to sort the truck locations
# Space-time complexity O(n^2)
def sortlocations(trck):
    for i in range(-1, len(trck.locations)):
        tmp = 999
        minIndex = -1
        if i == -1:
            loc1 = 0
        else:
            loc1 = getlocationIndex(trck.locations[i])
        for j in range(i + 1, len(trck.locations)):
            loc2 = getlocationIndex(trck.locations[j])
            if getDistance(loc1, loc2) < tmp:
                tmp = getDistance(loc1, loc2)
                minIndex = j
        if minIndex != -1:
            tmpLoc = trck.locations[minIndex]
            trck.locations[minIndex] = trck.locations[i + 1]
            trck.locations[i + 1] = tmpLoc


# gets the distances by index from the CSV Reader
# space-time complexity O(1)
def getDistance(index1, index2):
    return float(get_distance_data()[int(index1)][int(index2)])


# gets the location index from the CSV reader and set it as a new list
# sorts through list and return data to be used later to load trucks
# time complexity O(n^2)
def getlocationIndex(location):
    key_list = list(get_location_data().keys())
    for i in get_location_data():
        for k in key_list:
            if get_location_data()[k] == location:
                return k


# call the truck constructor and set the three trucks to it
# place trucks inside a list
# iterate though the hash table to load the three trucks with the conditionals constraints first
firstTruck = truck()
secondTruck = truck()
thirdTruck = truck()
firstTruck.name = "First Truck"
secondTruck.name = "Second Truck"
thirdTruck.name = "Third Truck"
truckList = [firstTruck, secondTruck, thirdTruck]

# Time complexity O(n)
for i in range(1, get_hash_size() + 1):
    key = str(i)
    if get_hash_table().getValue(key)[8] == 'loaded':
        pass
    elif get_hash_table().getValue(str(i))[6] == "Can only be on truck 2":
        secondTruck.addCargo(key)
    elif get_hash_table().getValue(str(i))[4] == "10:30:00":
        firstTruck.addCargo(key)
        if get_hash_table().getValue(str(i))[6].split(" ")[0] == "Must":
            firstKey = get_hash_table().getValue(str(i))[6].split(" ")[4]
            secondKey = get_hash_table().getValue(str(i))[6].split(" ")[6]
            if get_hash_table().getValue(firstKey)[8] != "loaded":
                firstTruck.addCargo(firstKey)
            if get_hash_table().getValue(secondKey)[8] != "loaded":
                firstTruck.addCargo(secondKey)
    elif get_hash_table().getValue(str(i))[6] == "Delayed on flight---will not arrive to depot until 9:05 am":
        secondTruck.addCargo(key)
    elif get_hash_table().getValue(str(i))[6] == "Wrong address listed":
        thirdTruck.addCargo(key)

# Use nearest neighbor algorithm to sort packages on trucks and add them in effect manner
# Sets the capacity of the truck to 16 packages max
# space-time complexity O(n^2)
for trck in truckList:
    sortlocations(trck)
    while 0 < trck.loadedCargo < 16:
        tmp = 999
        minIndex = -1
        for i in range(1, get_hash_size() + 1):
            if get_hash_table().getValue(str(i))[8] == "available":
                if getDistance(getlocationIndex(trck.locations[len(trck.locations) - 1]),
                               getlocationIndex(get_hash_table().getValue(str(i))[0])) < tmp:
                    tmp = getDistance(getlocationIndex(trck.locations[len(trck.locations) - 1]),
                                      getlocationIndex(get_hash_table().getValue(str(i))[0]))
                    minIndex = get_hash_table().getKey(get_hash_table().getValue(str(i)))
        if minIndex != -1:
            trck.addCargo(minIndex)
        else:
            break

firstTruck.shouldTurn = True
firstTruck.leavingTime = '8:00 AM'
secondTruck.leavingTime = '9:05 AM'


# returns the created lists of trucks
# space-time complexity O(1)

def getTrucks():
    return truckList


# returns the total distance that the trucks traveled
# space-time complexity O(n)
def getTotalDistance():
    totalDistance = 0
    for trck in truckList:
        totalDistance += trck.lengthOfRoute()
    return totalDistance
