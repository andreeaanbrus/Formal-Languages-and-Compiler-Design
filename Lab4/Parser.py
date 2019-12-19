class Parser:
    # the lr0 parser
    def __init__(self, grammar):
        self.grammar = grammar
        self.workingStack = []
        self.inputStack = []
        self.output = []

    def closure(self, productions):
        # productions: the list of productions for closure
        if not productions:
            return None
        closure = productions
        done = False
        while not done:
            done = True
            for dottedProd in closure:
                dotIndex = dottedProd[1].index('.')
                alpha = dottedProd[1][:dotIndex]
                Bbeta = dottedProd[1][dotIndex + 1:]
                if len(Bbeta) == 0:
                    continue
                B = Bbeta[0]
                if B in self.grammar.E:
                    continue
                for prod in self.grammar.getProductions(B):
                    dottedProd = (B, '.' + prod)
                    if dottedProd not in closure:
                        closure.append(dottedProd)
                        done = False
        return closure

    def goTo(self, state, symbol):
        C = []
        for production in state:
            dotIndex = production[1].index('.')
            alpha = production[1][:dotIndex]
            Xbeta = production[1][dotIndex + 1:]
            if len(Xbeta) == 0:
                continue
            X, beta = Xbeta[0], Xbeta[1:]
            if X == symbol:
                res = str(alpha) + X + '.' + str(beta)
                resultProd = (production[0], res)
                C.append(resultProd)
        return self.closure(C)

    def getCannonicalCollection(self):
        C = [self.closure([('S1', '.' + self.grammar.S[0])])]
        finished = False
        while not finished:
            finished = True
            for state in C:
                for symbol in self.grammar.N + self.grammar.E:
                    nextState = self.goTo(state, symbol)
                    if nextState is not None and nextState not in C:
                        C.append(nextState)
                        finished = False
        return C

    def generateTable(self):
        states = self.getCannonicalCollection()
        print("states", states)
        # a line for each state si
        # dictionary having keys 'action' and x form N + E for goto(si, x)
        table = [{} for _ in range(len(states))]
        # rules:
        # 1. if [A -> alpha.aBeta] is from si then action(si) = shift
        # 2. if [A -> Beta.] is from si and A != S' then action(si) = reduceI where I is the number of production A -> beta
        # 3. if [S' -> S.] is from si then action(si) = accept
        # 4. if goto(si, X) = sj (from collection) , then goto (si, X) = sj (from table)
        # 5. else error
        for index in range(len(states)):
            state = states[index]
            firstRuleCNT = 0
            secondRuleCNT = 0
            thirdRuleCNT = 0
            for prod in state:
                dotIndex = prod[1].index('.')
                alpha = prod[1][:dotIndex]
                beta = prod[1][dotIndex + 1:]
                if len(beta) != 0:
                    firstRuleCNT += 1
                else:
                    print(prod)
                    if prod[0] != 'S1':
                        secondRuleCNT += 1
                        productionIndex = self.grammar.P.index((prod[0], alpha))
                    elif alpha == self.grammar.S[0]:
                        thirdRuleCNT += 1

            if firstRuleCNT == len(state):
                table[index]['action'] = 'shift'

            elif secondRuleCNT == len(state):
                table[index]['action'] = 'reduce ' + str(productionIndex)

            elif thirdRuleCNT == len(state):
                table[index]['action'] = 'acc'
            else:
                raise (Exception('Error'))
            for symbol in self.grammar.N + self.grammar.E: #the goto part of the table
                nextState = self.goTo(state, symbol)
                if nextState in states:
                    table[index][symbol] = states.index(nextState)
        return table

    def parse(self, input):
        print(input)
        table = self.generateTable()
        self.workingStack = ['0']
        self.inputStack = [char for char in input]
        self.output = []
        print(table)
        while len(self.workingStack) != 0:
            state = int(self.workingStack[-1])  # take the state number from working stack
            if len(self.inputStack) > 0:
                char = self.inputStack.pop(0)
            else:
                char = None
            if table[state]['action'] == 'shift':
                if char not in table[state]:
                    raise (Exception('Cannot parse shift. Character: ', char))
                self.workingStack.append(char)
                self.workingStack.append(table[state][char])
            elif table[state]['action'] == 'acc':
                if len(self.inputStack) != 0:
                    raise (Exception('Cannot parse acc'))
                self.workingStack.clear()
            else:
                reduceState = int(table[state]['action'].split(' ')[1])
                reduceProduction = self.grammar.P[reduceState]
                toRemoveFromWorkingStack = [symbol for symbol in reduceProduction[1]]
                while len(toRemoveFromWorkingStack) > 0 and len(self.workingStack) > 0:
                    if self.workingStack[-1] == toRemoveFromWorkingStack[-1]:
                        toRemoveFromWorkingStack.pop()
                    self.workingStack.pop()
                if len(toRemoveFromWorkingStack) != 0:
                    raise (Exception('Cannot Parse reduce'))
                self.inputStack.insert(0, reduceProduction[0])
                self.output.insert(0, str(reduceState))

        return self.output
