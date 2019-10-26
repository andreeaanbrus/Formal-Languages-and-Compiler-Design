class HashTable:
    def __init__(self, size):
        self.size = size
        self.hashTable = [[] for x in range(self.size)]

    def add(self, value):
        index = self.hash(value)
        if self.checkExistance(value) is False:
            self.hashTable[index].append(value)
        return index

    def getPosition(self, value):
        index = self.hash(value)
        return index

    def __str__(self):
        return str(self.hashTable)

    def hash(self, token):
        sum = 0
        for letter in token:
            print(letter)
            sum += ord(letter)
        index = sum % self.size
        return index


    def checkExistance(self, value):
        # check if the value is already in the hashtable
        index = self.hash(value)
        for element in self.hashTable[index]:
            if element == value:
                print(value)
                return True
        return False
