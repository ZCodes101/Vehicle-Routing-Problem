
import csv
from HashTable import HashTable

# reads the package data from csv and saves in the hash table
# space-time complexity O(n)
with open('./data/package_data.csv') as csv_file:
    hashTable = HashTable()
    csv_reader = csv.reader(csv_file, delimiter=',')
    counter = 0
    for row in csv_reader:
        if len(row) == 9:
            row[8] = "At Hub"
        else:
            row.append("At Hub")
        row.append("available")
        row.append("")
        hashTable.insert(row[0], row[1:])
        counter += 1
csv_file.close()

# reads the distance name data from a csv and saves it in dictionary
# space-time complexity O(n)
with open('./data/distance_name.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    locations = {}
    for row in csv_reader:
        locations[row[0]] = row[2]


    def get_location_data():
        return locations

# reads the distance data from a csv and saves it in dictionary
# space-time complexity O(n)
with open('./data/distance_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    distances = []
    for row in csv_reader:
        distances.append(row)


# returns the hash table, size, and distance data all with O(1) space-time complexity
def get_hash_table():
    return hashTable


def get_hash_size():
    return counter


def get_distance_data():
    return distances

# Resets the hash table for the GUI reset button
# space-time Complexity O(n)
def reset_hash_table():
    hashTable.table.clear()
    with open('./data/package_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        counter = 0
        for row in csv_reader:
            if len(row) == 9:
                row[8] = "At Hub"
            else:
                row.append("At Hub")
            row.append("available")
            row.append("")
            hashTable.insert(row[0], row[1:])
            counter += 1
    csv_file.close()
