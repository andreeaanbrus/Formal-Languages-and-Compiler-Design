from Grammar import Grammar
from FiniteAutomata import FiniteAutomata


def printCommand():
    print("1 -> Grammar")
    print("2 -> Finite Automaton")
    print("0 -> Exit")


def printCommandGrammar():
    print("1 -> Set of non-terminals")
    print("2 -> Set of terminals")
    print("3 -> Set of productions of a non-terminal")
    print("4 -> Productions of a given terminal")
    print("5 -> Check if regular")
    print("6 -> Transform in finite automata")
    print("0 -> Back")


def printCommandFA():
    print("1 -> Set of states")
    print("2 -> Alphabet")
    print("3 -> Transitions")
    print("4 -> Final States")
    print("5 -> Transform to regular grammar")
    print("0 -> Back")


def main():
    mainCMD = -1
    while mainCMD != 0:
        printCommand()
        mainCMD = int(input("command: "))
        cmd = -1
        if mainCMD == 1:
            print("1 -> Read grammar from file")
            print("2 -> Read grammar from console")
            readCmd = int(input())
            if readCmd == 1:
                grammar = Grammar.readFromFile('grammar.txt')
            else:
                grammar = Grammar.readFromConsole()
            while cmd != 0:
                printCommandGrammar()
                cmd = int(input("command: "))
                if cmd == 1:
                    print("The set of non-terminals (N): ", grammar.N)
                elif cmd == 2:
                    print("The set of terminals (E): ", grammar.E)
                elif cmd == 3:
                    print("The set of productions (P): ", grammar.P)
                elif cmd == 4:
                    symbol = input("The symbol: ")
                    print(grammar.getProductions(symbol))
                elif cmd == 5:
                    print(grammar.checkRegular())
                elif cmd == 6:
                    convertedFA = FiniteAutomata.fromRegularGrammar(grammar)
                    print("Q -> ", convertedFA.Q)
                    print("E -> ", convertedFA.E)
                    print("q0 -> ", convertedFA.q0)
                    print("F ->", convertedFA.F)
                    print("D -> ", convertedFA.D)
        elif mainCMD == 2:
            print("1 -> Read FA from file")
            print("2 -> Read FA from console")
            readCmd = int(input())
            if readCmd == 1:
                fa = FiniteAutomata.readFromFile('fa.txt')
            else:
                fa = FiniteAutomata.readFromConsole()
            while cmd != 0:
                printCommandFA()
                cmd = int(input("command: "))
                if cmd == 1:
                    print("The set of states (Q): ", fa.Q)
                elif cmd == 2:
                    print("Alphabet: ", fa.E)
                elif cmd == 3:
                    print("The transitions (D): ", fa.D)
                elif cmd == 4:
                    print("The set of final states (F):", fa.F)
                elif cmd == 5:
                    convertedRG = Grammar.fromFA(fa)
                    print("N -> ", convertedRG.N)
                    print("E -> ", convertedRG.E)
                    print("S -> ", convertedRG.S)
                    print("P ->", convertedRG.P)
main()
