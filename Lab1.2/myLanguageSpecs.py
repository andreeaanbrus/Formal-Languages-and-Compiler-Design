operators = ['+', '-', '*', '/', '=', '<', '>', '<=', '==', '>=', '!=', '&&', '||']
separators = [';', '{', '}', '(', ')', ' ', '\n', '[', ']', ',']
reservedWords = ['int', 'char', 'double', 'if', 'else', 'while', 'read', 'print', 'list', 'int_main']
all = operators + separators + reservedWords
codification = {all[i]: i + 2 for i in range(0, len(all))}
codification['identifier'] = 0
codification['constant'] = 1
print(codification)