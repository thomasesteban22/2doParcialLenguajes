# Generated from ListGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ListGrammarParser import ListGrammarParser
else:
    from ListGrammarParser import ListGrammarParser

# This class defines a complete generic visitor for a parse tree produced by ListGrammarParser.

class ListGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ListGrammarParser#prog.
    def visitProg(self, ctx:ListGrammarParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListGrammarParser#list.
    def visitList(self, ctx:ListGrammarParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListGrammarParser#element.
    def visitElement(self, ctx:ListGrammarParser.ElementContext):
        return self.visitChildren(ctx)



del ListGrammarParser