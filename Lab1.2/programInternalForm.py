class ProgramInternalForm:
    def __init__(self):
        self.pif = []

    def add(self, code, id):
        self.pif.append((code, id))

    def __str__(self):
        return str(self.pif)

