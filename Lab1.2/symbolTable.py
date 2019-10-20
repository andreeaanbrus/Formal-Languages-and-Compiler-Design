from hashTable import HashTable


class SymbolTable:
    def __init__(self):
        self.symTableIdentifiers = HashTable()
        self.symTableConstants = HashTable()
        self.lastIdIdentifiers = 0
        self.lastIdConstants = 0

    def getIdentifiers(self):
        return self.symTableIdentifiers

    def getConstants(self):
        return self.symTableConstants

    def addIdentifier(self, key):
        self.lastIdIdentifiers += 1
        self.symTableIdentifiers.add(key, self.lastIdIdentifiers)
        return self.lastIdIdentifiers

    def addConstant(self, key):
        self.lastIdConstants += 1
        self.symTableConstants.add(key, self.lastIdConstants)
        return self.lastIdConstants

    def getPositionIdentifier(self, token):
        return self.symTableIdentifiers.get(token)

    def getPositionConstant(self, token):
        return self.symTableConstants.get(token)


