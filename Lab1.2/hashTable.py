class HashTable:
    def __init__(self):
        self.hashTable = {}

    def add(self, key, value):
        self.hashTable[key] = value

    def get(self, key):
        return self.hashTable.get(key)

    def __str__(self):
        return str(self.hashTable)