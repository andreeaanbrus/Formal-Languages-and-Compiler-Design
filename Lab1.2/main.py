import myLanguageSpecs
from programInternalForm import ProgramInternalForm
from symbolTable import SymbolTable
import re

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
        print(line)
        for token in line:
            if token is not '':
                print(token)
                if token is ' ':
                    pass
                elif isReserved(token) or isOperator(token) or isSeparator(token):
                    print("operator or separator or reserved")
                    pif.add(getCodeOfToken(token), -1)
                elif isIdentifier(token):
                    print("identifier")
                    pos = st.addIdentifier(token)
                    pif.add(getCodeOfToken('identifier'), pos)
                elif isConstant(token):
                    print("constant")
                    pos = st.addConstant(token)
                    pif.add(getCodeOfToken('constant'), pos)
                else:
                    raise Exception("Lexical error at line", ''.join(line))
algo()
print(myLanguageSpecs.codification)
print("Pif", pif)
print("Symbol Table Constants: ", st.symTableConstants)
print("Symbol Table Identifiers: ", st.symTableIdentifiers)
