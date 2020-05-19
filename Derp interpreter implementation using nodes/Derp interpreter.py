"""
141 Tree Lab - Derp the Interpreter

Derp is a simple interpreter that parses and evaluates prefix expressions
containing basic arithmetic operators (*,//,-,+).  It performs arithmetic with
integer only operands that are either literals or variables (read from a
symbol table).  It dumps the symbol table, produces the expression infix with
parentheses to denote order of operation, and evaluates/produces the result of
the expression.

Author: Scott C Johnson (scj@cs.rit.edu)

Author: Sanchit Monga
"""

from dataclasses import dataclass
from typing import Union


@dataclass
class LiteralNode:
    """Represents an operand node"""

    val: int


@dataclass
class VariableNode:
    """Represents a variable node"""
    name: str


@dataclass
class MathNode:
    """Represents a mathematical operation"""
    left: Union['MathNode', LiteralNode, VariableNode]
    op: str
    right: Union['MathNode', LiteralNode, VariableNode]


##############################################################################
# parse
##############################################################################

def parse(tokens):
    """parse: list(String) -> Node
    From a prefix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    """
    a=tokens.pop(0)#npopping the first element
    if a in ['+','-','//','*']:# checking whether the element is a mathmatical operator or not
        return MathNode(parse(tokens), a, parse(tokens))
    elif a.isidentifier():# chekcing whether the element is a character
        return VariableNode(a)
    elif a.isdigit():# checking whether the element is a digit
        return LiteralNode(a)
    else:# checking whether the user input is other than the required
        raise ValueError(a,"invalid")
##############################################################################
# infix
##############################################################################

def infix(node):
    """infix: Node -> String | TypeError
    Perform an inorder traversal of the node and return a string that
    represents the infix expression."""
    if node is None:# base case
        return ''
    else:
        if isinstance(node,MathNode)==True:# checking wherhter the element is a math node or not
            return '('+infix(node.left)+str(node.op)+infix(node.right)+')'
        elif isinstance(node,VariableNode)==True:# checking wherhter the element is a variable node or not
            return infix(None)+str(node.name)+infix(None)
        elif isinstance(node,LiteralNode)==True:# checking wherhter the element is a literal node or not
            return infix(None)+str(node.val)+infix(None)

##############################################################################
# evaluate
#############################################################################

def evaluate(node, symTbl):
    """evaluate: Node * dict(key=Sring, value=int) -> int | TypeError
    Given the expression at the node, return the integer result of evaluating
    the node.
    Precondition: all variable names must exist in symTbl"""
    if node is None:# base case for recursion
        return ''
    else:
        if isinstance(node,MathNode)==True:# if the value is a mathnode or not
            if(str(node.op)=='+'):# checking whether the node.op ois ewual to different operators and perfomring the operations according to that
                return evaluate(node.left, symTbl)+evaluate(node.right, symTbl)
            elif(str(node.op)=='-'):
                return evaluate(node.left, symTbl)-evaluate(node.right, symTbl)
            elif(str(node.op)=='*'):
                return evaluate(node.left, symTbl)*evaluate(node.right, symTbl)
            elif (str(node.op) == '//'):
                return evaluate(node.left, symTbl)//evaluate(node.right, symTbl)
        elif isinstance(node,VariableNode)==True:# checking wherhter the element is a variable node or not
            return int(symTbl[str(node.name)])
        elif isinstance(node,LiteralNode)==True:# checking whether the elements belong to a literal node
            return int(node.val)
##############################################################################
# main
##############################################################################

def main():
    """main: None -> None
    The main program prompts for the symbol table file, and a prefix
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression"""
    print("Hello Herp, welcome to Derp v1.0 :)")
    inFile = input("Herp, enter symbol table file: ")
    a={}# creating a new dictionary
    for line in open(inFile):# for every line in the file
        a1=line.strip()
        b=a1.split() #storing the elements of each line in a list
        a[b[0]]=b[1]# entering all the elements in the dictionary along with the key
    print("Herp, enter prefix expressions, e.g.: + 10 20 (ENTER to quit)...")
    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefixExp = input("derp> ")
        if prefixExp == "":
            break
        l=prefixExp.split()# splitting all the elements in the prefix and storing it in a list
        s=parse(l)# invoking the parse function by passing a list inside it
        inf=infix(s)# storing the infix value by passing the node value in the parse function
        print("Derping the infix expression:"+inf)# printing the infix expression
        eval=evaluate(s,a)# invoking the evaluate function and storing its value
        print("Derping the evaluation:", eval)# printing the value after evaluation
    print("Goodbye Herp :(")

if __name__ == "__main__":
    main()


