# Generated from ListGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ListGrammarParser import ListGrammarParser
else:
    from ListGrammarParser import ListGrammarParser

# This class defines a complete listener for a parse tree produced by ListGrammarParser.
class ListGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by ListGrammarParser#prog.
    def enterProg(self, ctx:ListGrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by ListGrammarParser#prog.
    def exitProg(self, ctx:ListGrammarParser.ProgContext):
        pass


    # Enter a parse tree produced by ListGrammarParser#list.
    def enterList(self, ctx:ListGrammarParser.ListContext):
        pass

    # Exit a parse tree produced by ListGrammarParser#list.
    def exitList(self, ctx:ListGrammarParser.ListContext):
        pass


    # Enter a parse tree produced by ListGrammarParser#element.
    def enterElement(self, ctx:ListGrammarParser.ElementContext):
        pass

    # Exit a parse tree produced by ListGrammarParser#element.
    def exitElement(self, ctx:ListGrammarParser.ElementContext):
        pass



del ListGrammarParser