# Darey Lee
# Programming Assignment 1
# CS 3210
# Mota

from enum import Enum
from tree import Tree
import sys

# Enable/Disable printing of the stack and input string in the console
DEBUG = False

##########################################################
#################### LEXICAL ANALYZER ####################
##########################################################

def parseFile():
    symbols = [':=', '>=', '<=', ':', '=', '>', '<', '*', '.', ';', '-', '+']
    input_string = []
    temp_list_of_elements = []
    final_string = []

    for line in file:
        input_string.append(line)

    # remove leading and trailing spaces
    for entry in input_string:
        input_string[input_string.index(entry)] = entry.strip()

    # seperate each word by ' ' and flatten the list
    for entry in input_string:
        new_elements = entry.split(' ')
        
        for element in new_elements:
            temp_list_of_elements.append(element)

    # check for symbols attached to words and seperate them from the word
    for entry in temp_list_of_elements:
        for symbol in symbols:
            if symbol in entry:
                final_string.append(entry.split(symbol)[0])
                final_string.append(symbol)
                final_string.append(entry.split(symbol)[1])
                break
        else:
            final_string.append(entry)
    
    # removing all empty strings
    while '' in final_string:
        final_string.remove('')

    return final_string

def lex(word):
    #1
    if word == '+':
        lexeme_and_token.append((word, Token.ADDITION))

    #2
    elif word == ':=':
        lexeme_and_token.append((word, Token.ASSIGNMENT))

    #3
    elif word == 'begin':
        lexeme_and_token.append((word, Token.BEGIN))

    #4    
    elif word == 'boolean':
        lexeme_and_token.append((word, Token.BOOLEAN_TYPE))  

    #5
    elif word == ':':
        lexeme_and_token.append((word, Token.COLON))

    #6
    elif word == 'do':
        lexeme_and_token.append((word, Token.DO))

    #7
    elif word == 'else':
        lexeme_and_token.append((word, Token.ELSE))

    #8
    elif word == 'end':
        lexeme_and_token.append((word, Token.END))

    #9
    elif word == '=':
        lexeme_and_token.append((word, Token.EQUAL))

    #10
    elif word == 'false':
        lexeme_and_token.append((word, Token.FALSE))

    #11
    elif word == '>':
        lexeme_and_token.append((word, Token.GREATER))

    #12
    elif word == '>=':
        lexeme_and_token.append((word, Token.GREATER_EQUAL))

    #14
    elif word == 'if':
        lexeme_and_token.append((word, Token.IF))

    #16
    elif word == 'integer':
        lexeme_and_token.append((word, Token.INTEGER_TYPE))

    #17
    elif word == '<':
        lexeme_and_token.append((word, Token.LESS))

    #18
    elif word == '<=':
        lexeme_and_token.append((word, Token.LESS_EQUAL))

    #19
    elif word == '*':
        lexeme_and_token.append((word, Token.MULTIPLICATION))

    #20
    elif word == '.':
        lexeme_and_token.append((word, Token.PERIOD))

    #21
    elif word == 'program':
        lexeme_and_token.append((word, Token.PROGRAM))
                      
    #22
    elif word == 'read':
        lexeme_and_token.append((word, Token.READ))

    #23
    elif word == ';':
        lexeme_and_token.append((word, Token.SEMICOLON))       

    #24
    elif word == '-':
        lexeme_and_token.append((word, Token.SUBTRACTION))

    #25
    elif word == 'then':
        lexeme_and_token.append((word, Token.THEN))

    #26
    elif word == 'true':
        lexeme_and_token.append((word, Token.TRUE))

    #27
    elif word == 'var':
        lexeme_and_token.append((word, Token.VAR))

    #28
    elif word == 'while':
        lexeme_and_token.append((word, Token.WHILE))

    #29
    elif word == 'write':
        lexeme_and_token.append((word, Token.WRITE))

    #15
    elif word[0].isdigit():
        for char in word:
            if not char.isdigit():
                print(char)
                raise Exception(errorMessage(3))
        lexeme_and_token.append((word, Token.INTEGER_LITERAL))
        integer_list.append(word)

    #13
    elif word[0].isalpha():
        for char in word:
            if not char.isalpha() and not char.isdigit():
                raise Exception(errorMessage(3))
        lexeme_and_token.append((word, Token.IDENTIFIER))
        identifier_list.append(word)
    
    else:
        raise Exception(errorMessage(3))
    
class Token(Enum):
    ADDITION        = 1
    ASSIGNMENT      = 2
    BEGIN           = 3
    BOOLEAN_TYPE    = 4
    COLON           = 5
    DO              = 6
    ELSE            = 7
    END             = 8
    EQUAL           = 9
    FALSE           = 10
    GREATER         = 11
    GREATER_EQUAL   = 12
    IDENTIFIER      = 13
    IF              = 14
    INTEGER_LITERAL = 15
    INTEGER_TYPE    = 16
    LESS            = 17
    LESS_EQUAL      = 18
    MULTIPLICATION  = 19
    PERIOD          = 20
    PROGRAM         = 21
    READ            = 22
    SEMICOLON       = 23
    SUBTRACTION     = 24
    THEN            = 25
    TRUE            = 26
    VAR             = 27
    WHILE           = 28
    WRITE           = 29

#########################################################
#################### SYNTAX ANALYZER ####################
#########################################################

def changeTokenToActualForm(entry):
    if entry == 'addition':
        return '+'
    if entry == 'assignment':
        return ':='
    if entry == 'boolean_type':
        return 'boolean'
    if entry == 'colon':
        return ':'    
    if entry == 'equal':
        return '='
    if entry == 'greater':
        return '>'
    if entry == 'greater_equal':
        return '>='
    if entry == 'integer_type':
        return 'integer'    
    if entry == 'less':
        return '<'
    if entry == 'less_equal':
        return '<='
    if entry == 'multiplication':
        return '*'
    if entry == 'period':
        return '.'   
    if entry == 'semicolon':
        return ';'         
    if entry == 'subtraction':
        return '-'
    return entry

# reads the given input and returns the grammar as a list of productions
def loadGrammar(input):
    grammar = []
    for line in input:
        grammar.append(line.strip())
    return grammar

# returns the LHS (left hand side) of a given production
def getLHS(production):
    return production.split("->")[0].strip()

# returns the RHS (right hand side) of a given production
def getRHS(production):
    return production.split("->")[1].strip().split(" ")

# prints the productions of a given grammar, one per line
def printGrammar(grammar):
    i = 0
    for production in grammar:
        print(str(i) + ". " + getLHS(production), end = " -> ")
        print(getRHS(production))
        i += 1

# reads the given input containing an SLR parsing table and returns the "actions" and "gotos" as dictionaries
def loadTable(input):
    actions = {}
    gotos = {}
    header = input.readline().strip().split(",")
    end = header.index("$")
    tokens = []
    for field in header[1:end + 1]:
        tokens.append(field)
        # tokens.append(int(field))
    variables = header[end + 1:]
    for line in input:
        row = line.strip().split(",")
        state = int(row[0])
        for i in range(len(tokens)):
            token = tokens[i]
            key = (state, token)
            value = row[i + 1]
            if len(value) == 0:
                value = None
            actions[key] = value
        for i in range(len(variables)):
            variable = variables[i]
            key = (state, variable)
            value = row[i + len(tokens) + 1]
            if len(value) == 0:
                value = None
            gotos[key] = value
    return (actions, gotos)

# prints the given actions, one per line
def printActions(actions):
    for key in actions:
        print(key, end = " -> ")
        print(actions[key])

# prints the given gotos, one per line
def printGotos(gotos):
    for key in gotos:
        print(key, end = " -> ")
        print(gotos[key])

# given an input (source program), grammar, actions, and gotos, returns true/false depending whether the input should be accepted or not
def parse(input, grammar, actions, gotos):

    # TODO #1: create a list of trees
    trees = []

    stack = []
    stack.append(0)
    while True:
        state = stack[-1]
        token = input[0]
        action = actions[(state, token)]

        if DEBUG:
            print("stack: ", end = "")
            print(stack, end = " ")
            print("input: ", end = "")
            print(input, end = " ")
            print("action: ", end = "")
            print(action)

        if action is None:
            special_words = ['program', 'var', 'begin', 'end', 'read', 'write', 'if', 'then', 'else', 'while', 'do']
            symbols = [':=', '>=', '<=', ':', '=', '>', '<', '*', '.', ';', '-', '+']

            action_category_symbols = False
            action_category_special_words = False

            for entry in actions:
                if entry[0] == state and actions[entry] != None:
                    if(entry[1] in symbols):
                        action_category_symbols = True
                    if(entry[1] in special_words):
                        action_category_special_words = True
                    
                if action_category_symbols and action_category_special_words:
                    raise Exception(errorMessage(99))

            for entry in actions:
                
                if entry[0] == state and actions[entry] != None:

                    for word in special_words:
                        if entry[1] == word:
                            raise Exception(errorMessage(8))
                    
                    if stack[-2] == 'identifier' and input[0] == 'integer':
                        raise Exception(errorMessage(99))
                    
                    for symbol in symbols:
                        if entry[1] == symbol:
                            raise Exception(errorMessage(9)) 
                    
                    if entry[1] == 'integer' or entry[1] == 'boolean':
                        raise Exception(errorMessage(10))

                    if stack[-2] in symbols and input[0] in symbols:
                        raise Exception(errorMessage(11))

                    if entry[1] == '$':
                        raise Exception(errorMessage(6))

                    raise Exception(errorMessage(7))

        # shift operation
        if action[0] == 's':
            input.pop(0)
            stack.append(token)
            state = int(action[1:])
            stack.append(state)

            # TODO #2: create a new tree, set data to token, and append it to the list of trees
            tree = Tree()

            # Append literals to their tokens
            if token == 'identifier':
                identifier_literal_tree = Tree()
                identifier_literal_tree.data = identifier_list.pop(0)
                tree.add(identifier_literal_tree)

            if token == 'integer_literal':
                integer_literal_tree = Tree()
                integer_literal_tree.data = integer_list.pop(0)
                tree.add(integer_literal_tree)

            tree.data = token
            trees.append(tree)

        # reduce operation
        elif action[0] == 'r':
            production = grammar[int(action[1:])]
            lhs = getLHS(production)
            rhs = getRHS(production)
            for i in range(len(rhs) * 2):
                stack.pop()
            state = stack[-1]
            stack.append(lhs)
            stack.append(int(gotos[(state, lhs)]))

            # TODO #3: create a new tree and set data to lhs
            newTree = Tree()
            newTree.data = lhs

            # TODO #4: get "len(rhs)" trees from the right of the list of trees and add each of them as child of the new tree you created, preserving the left-right order
            for tree in trees[-len(rhs):]:
                newTree.add(tree)

            # TODO #5: remove "len(rhs)" trees from the right of the list of trees
            trees = trees[:-len(rhs)]

            # TODO #6: append the new tree to the list of trees
            trees.append(newTree)

        # not a shift or reduce operation, must be an "accept" operation
        else:
            production = grammar[0]
            lhs = getLHS(production)
            rhs = getRHS(production)

            # TODO #7: same as reduce but using the 1st rule of the grammar
            root = Tree()
            root.data = lhs
            for tree in trees:
                root.add(tree)

            # TODO #8: return the new tree
            return root

#########################################################
###################### ERROR CODES ######################
#########################################################
def errorMessage(code):
    msg = "Error #" + str(code) + ": "
    if code == 1:
        return msg + "Source file missing"
    if code == 2:
        return msg + "Couldn't open source file"
    if code == 3:
        return msg + "Lexical error"
    if code == 4:
        return msg + "Couldn't open grammar file"
    if code == 5:
        return msg + "Couldn't open SLR table file"
    if code == 6:
        return msg + "EOF expected"
    if code == 7:
        return msg + "Identifier expected"
    if code == 8:
        return msg + "Special word missing"
    if code == 9:
        return msg + "Symbol missing"
    if code == 10:
        return msg + "Data type expected"        
    if code == 11:
        return msg + "Identifier or literal value expected"
    if code == 99:
        return msg + "Syntax error"

class Error_01(Exception):
    pass
class Error_02(Exception):
    pass
class Error_03(Exception):
    pass
class Error_04(Exception):
    pass
class Error_05(Exception):
    pass
class Error_06(Exception):
    pass
class Error_07(Exception):
    pass
class Error_08(Exception):
    pass
class Error_09(Exception):
    pass
class Error_10(Exception):
    pass
class Error_11(Exception):
    pass 
class Error_99(Exception):
    pass

# main
if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise Exception("Source file missing")

    try:
        source = open(sys.argv[1], "rt")
    except:
        raise Exception("Couldn't open source file") from None
    
    file = source.readlines()
    source.close()

########### LEXICAL ANALYZER ###########

    clean_input_string = parseFile()
    
    lexeme_and_token = []
    integer_list = []
    identifier_list = []

    for word in clean_input_string:
        lex(word)

############ SYNTAX ANALYZER ############

    try:
        input = open("grammar.txt", "rt")
    except:
        raise Exception("Couldn't open grammar file") from None
    
    grammar = loadGrammar(input)
    # printGrammar(grammar)
    input.close()

    try:
        input = open("slr_table.csv", "rt")
    except:
        raise Exception("Couldn't open SLR table file") from None
    
    actions, gotos = loadTable(input)
    # printActions(actions)
    # printGotos(gotos)
    input.close()

    input = []
    for (lexeme, token) in lexeme_and_token:
        input.append(token.name.lower())

    for entry in input:
        input[input.index(entry)] = changeTokenToActualForm(entry)

    input.insert(len(input), '$')

    # tree building update
    tree = parse(input, grammar, actions, gotos)

    # If no errors, print everything
    if tree:
        print("##############################")
        print("##### LEXEME AND TOKENS ######")
        print("##############################")
        for (lexeme, token) in lexeme_and_token:
            print(lexeme, token)

        print("##############################")
        print("######### PARSE TREE #########")
        print("##############################")
        print("Input is syntactically correct!")
        print("Parse Tree:")
        tree.print("")

    else:
        raise Exception(errorMessage(99))
