
# Hash Table class
class HashTable:
    def __init__(self):
        self.table = []

# Inserts key and values into hash table ,
# Space-time complexity is O(1)
    def insert(self, key, values):
        self.table.append([key, values])

# looks up value and returns results if found,
# Space-time complexity O(n)
    def getValue(self, key):
        result = None
        for obj in self.table:
            if key == obj[0]:
                result = obj[1]
        if result == None:
            print("invalid key ", key)
        else:
            return result

    # looks up value for key and returns results if found,
    # Space-time complexity O(n)
    def getKey(self, value):
        result = None
        for obj in self.table:
            if value == obj[1]:
                result = obj[0]
        if result == None:
            print("invalid key")
            exit(0)
        else:
            return result
