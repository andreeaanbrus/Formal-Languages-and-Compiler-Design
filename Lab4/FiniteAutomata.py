class FiniteAutomata:
    @staticmethod
    def parseLine(line):
        return [element.strip() for element in line.strip().split('=')[1].strip()[1:-1].split(',')]

    @staticmethod
    def parseConsole(line):
        return [element.strip() for element in line.strip().split(',')]

    @staticmethod
    def readFromFile(filename):
        with open(filename) as file:
            Q = FiniteAutomata.parseLine(file.readline())
            E = FiniteAutomata.parseLine(file.readline())
            q0 = FiniteAutomata.parseLine(file.readline())
            F = FiniteAutomata.parseLine(file.readline())
            D = FiniteAutomata.readD(FiniteAutomata.parseLine(''.join([line for line in file])))
        return FiniteAutomata(Q, E, D, q0, F)

    @staticmethod
    def readFromConsole():
        Q = FiniteAutomata.parseConsole(input("Q = "))
        E = FiniteAutomata.parseConsole(input("E = "))
        q0 = FiniteAutomata.parseConsole(input("q0 = "))
        F = FiniteAutomata.parseConsole(input("F = "))
        D = FiniteAutomata.readD(FiniteAutomata.parseConsole(input("D = ")))
        return FiniteAutomata(Q, E, D, q0, F)

    @staticmethod
    def readD(text):
        result = []
        for rule in text:
            [lhs, rhs] = rule.strip().split('-')
            [i, j] = lhs.strip()[1:-1].split(' ')
            result.append(((i, j), rhs.strip()))
        return result

    def __init__(self, Q, E, D, q0, F):
        self.Q = Q
        self.E = E
        self.D = D
        self.q0 = q0
        self.F = F

    @staticmethod
    def fromRegularGrammar(RG):
        Q = RG.N + ['K']
        E = RG.E
        q0 = [RG.S[0]]
        D = []
        F = ['K']
        for rule in RG.P:
            lhs, rhs = rule
            print(lhs, rhs)
            if lhs == q0[0] and rhs == 'e':
                F.append(lhs)
                continue
            if len(rhs) == 2:
                D.append(((lhs, rhs[0]), rhs[1]))
            else:
                D.append(((lhs, rhs[0]), 'K'))
        return FiniteAutomata(Q, E, D, q0, F)


