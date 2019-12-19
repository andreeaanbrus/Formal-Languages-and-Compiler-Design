import re


class Grammar:
    @staticmethod
    def parseLine(line):
        return [element.strip() for element in line.strip().split('=')[1].strip()[1:-1].split(',')]

    @staticmethod
    def parseConsole(line):
        return [element.strip() for element in line.strip().split(',')]

    @staticmethod
    def parseProductions(productions):
        result = []
        for rule in productions:
            [lhs, rhs] = rule.strip().split('->')
            results = rhs.strip().split('|')
            for res in results:
                result.append((lhs.strip(), res.strip()))
        return result

    @staticmethod
    def readFromFile(filename):
        with open(filename) as file:
            N = Grammar.parseLine(file.readline())
            E = Grammar.parseLine(file.readline())
            S = Grammar.parseLine(file.readline())
            P = Grammar.parseProductions(Grammar.parseLine(''.join([line for line in file])))
        return Grammar(N, E, P, S)

    @staticmethod
    def readFromConsole():
        N = Grammar.parseConsole(input("N = "))
        E = Grammar.parseConsole(input("E = "))
        S = Grammar.parseConsole(input("S = "))
        P = Grammar.parseProductions(Grammar.parseConsole(input("P = ")))
        return Grammar(N, E, P, S)

    def __init__(self, N, E, P, S):
        self.N = N
        self.E = E
        self.P = P
        self.S = S

    def getProductions(self, symbol):
        result = []
        for production in self.P:
            if production[0] == symbol:
                result.append(production[1])
        return result

    def checkForStartingSymbolOnRHS(self):
        for (lhs, rhs) in self.P:
            if re.findall(self.S[0], rhs):
                return False
        return True

    def checkRegular(self):
        # A -> a, A-> ab (1)
        # if S -> epsilon then S does not appear on the rhs of any production (2)
        # epsilon = e
        startingSymbol = self.S[0]
        for rule in self.P:
            lhs, rhs = rule
            print(lhs, rhs)
            # A -> a or a -> ab
            if len(rhs) > 2:
                print("The length of rhs should be at most 2 (a or aB)")
                return False
            for elem in self.getProductions(rhs):
                if re.match(r'^[a-z]{1}[A-Z]{1}$|^[a-z]{1}$', elem) is None:
                    print("The production should be of form A -> a or A -> aB")
                    return False
            if lhs == startingSymbol and rhs == 'e':
                if self.checkForStartingSymbolOnRHS() is False:
                    print("S should not be in rhs ")
                    return False
        return True

    @staticmethod
    def fromFA(fa):
        N = fa.Q
        E = fa.E
        S = fa.q0
        P = []
        if fa.q0[0] in fa.F:
            P.append((fa.q0[0], 'e'))
        for transition in fa.D:
            lhs, state = transition[0]
            rhs = transition[1].strip()
            if rhs in fa.F:
                P.append((lhs, state))
                P.append((lhs, state.strip() + rhs))
            if rhs not in fa.F:
                P.append((lhs, state.strip() + rhs))
        return Grammar(N, E, P, S)
