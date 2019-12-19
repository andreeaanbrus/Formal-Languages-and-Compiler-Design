from Grammar import Grammar
from Parser import Parser
import myLanguageSpecs
from programInternalForm import ProgramInternalForm
from symbolTable import SymbolTable
import re


def main():
    # print(parser.parse('int a = 5;'))
    # g = Grammar.readFromFile('grammar.txt')
    # g = Grammar.readFromFile('myGrammar.txt')
    g = Grammar.readFromFile('my_mini_grammar.txt')
    parser = Parser(g)
    st = SymbolTable()
    pif = ProgramInternalForm()
    filename = 'input.txt'

    # def detectToken()
    # define token -> keyword, operator, separator (addToPif(code_of_token, -1)
    #             -> identifier (pos = pos(token, symTable), addToPif(token, st))
    #             -> constant (pos + addToPif(code_of_constant, pos))

    def isSeparator(char):
        return char in myLanguageSpecs.separators

    def isOperator(char):
        return char in myLanguageSpecs.operators

    def isReserved(word):
        return word in myLanguageSpecs.reservedWords

    def isIdentifier(word):
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]){0,8}$', word) is not None

    def isConstant(token):
        return re.match(r'((\'[a-z]\'|\'[0-9]\')|(\+|-){0,1}[0-9]*\d$)', token) is not None

    def getCodeOfToken(token):
        try:
            return myLanguageSpecs.codification[token]
        except:
            raise Exception("The token is not in codification table")

    def tokenize():
        result = []
        with open(filename) as file:
            re_separator = r'('
            for separator in myLanguageSpecs.separators:
                re_separator += re.escape(separator) + '|'
            re_separator = re_separator[:-1] + ')'
            for line in file:
                line = line.strip()
                new_line = re.split(re.compile(re_separator), line)
                result.append(new_line)
        return result

    def algo():
        lines_array = tokenize()
        for line in lines_array:
            for token in line:
                if token is not '':
                    if token is ' ':
                        pass
                    elif isReserved(token) or isOperator(token) or isSeparator(token):
                        pif.add(getCodeOfToken(token), -1)
                    elif isIdentifier(token):
                        pos = st.addIdentifier(token)
                        pif.add(getCodeOfToken('identifier'), pos)
                    elif isConstant(token):
                        pos = st.addConstant(token)
                        pif.add(getCodeOfToken('constant'), pos)
                    else:
                        raise Exception("Lexical error at line", ''.join(line))

    algo()
    # print("Pif", pif)
    # print("Symbol Table Constants: ", st.symTableConstants)
    # print("Symbol Table Identifiers: ", st.symTableIdentifiers)
    # print(g.P)
    revereCodification = {}
    for key in myLanguageSpecs.codification:
        revereCodification[myLanguageSpecs.codification[key]] = key
    inputStack = ''
    for (code, id) in pif.pif:
        inputStack += str(code) + ' '
    print("Productions: ", g.P)
    print(parser.closure([('S1', '.' + g.S[0])]))
    print(parser.parse(inputStack))
    # print(parser.parse('abbc'))
    # print(parser.getCannonicalCollection())
main()
