from hashTable import HashTable


class SymbolTable:
    def __init__(self):
        self.symTableIdentifiers = HashTable(17)
        self.symTableConstants = HashTable(17)

    def getIdentifiers(self):
        return self.symTableIdentifiers

    def getConstants(self):
        return self.symTableConstants

    def addIdentifier(self, key):
        position = self.symTableIdentifiers.add(key)
        return position

    def addConstant(self, key):
        position = self.symTableConstants.add(key)
        return position

    def getPositionIdentifier(self, token):
        return self.symTableIdentifiers.getPosition(token)

    def getPositionConstant(self, token):
        return self.symTableConstants.getPosition(token)


