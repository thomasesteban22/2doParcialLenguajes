# Generated from MapFunction.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MapFunctionParser import MapFunctionParser
else:
    from MapFunctionParser import MapFunctionParser

# This class defines a complete listener for a parse tree produced by MapFunctionParser.
class MapFunctionListener(ParseTreeListener):

    # Enter a parse tree produced by MapFunctionParser#prog.
    def enterProg(self, ctx:MapFunctionParser.ProgContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#prog.
    def exitProg(self, ctx:MapFunctionParser.ProgContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#stat.
    def enterStat(self, ctx:MapFunctionParser.StatContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#stat.
    def exitStat(self, ctx:MapFunctionParser.StatContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#mapFunction.
    def enterMapFunction(self, ctx:MapFunctionParser.MapFunctionContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#mapFunction.
    def exitMapFunction(self, ctx:MapFunctionParser.MapFunctionContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#filterFunction.
    def enterFilterFunction(self, ctx:MapFunctionParser.FilterFunctionContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#filterFunction.
    def exitFilterFunction(self, ctx:MapFunctionParser.FilterFunctionContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#iterable.
    def enterIterable(self, ctx:MapFunctionParser.IterableContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#iterable.
    def exitIterable(self, ctx:MapFunctionParser.IterableContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#list.
    def enterList(self, ctx:MapFunctionParser.ListContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#list.
    def exitList(self, ctx:MapFunctionParser.ListContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#tuple.
    def enterTuple(self, ctx:MapFunctionParser.TupleContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#tuple.
    def exitTuple(self, ctx:MapFunctionParser.TupleContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#function.
    def enterFunction(self, ctx:MapFunctionParser.FunctionContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#function.
    def exitFunction(self, ctx:MapFunctionParser.FunctionContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#elements.
    def enterElements(self, ctx:MapFunctionParser.ElementsContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#elements.
    def exitElements(self, ctx:MapFunctionParser.ElementsContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#lambdaExpr.
    def enterLambdaExpr(self, ctx:MapFunctionParser.LambdaExprContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#lambdaExpr.
    def exitLambdaExpr(self, ctx:MapFunctionParser.LambdaExprContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#op.
    def enterOp(self, ctx:MapFunctionParser.OpContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#op.
    def exitOp(self, ctx:MapFunctionParser.OpContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#var.
    def enterVar(self, ctx:MapFunctionParser.VarContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#var.
    def exitVar(self, ctx:MapFunctionParser.VarContext):
        pass


    # Enter a parse tree produced by MapFunctionParser#expr.
    def enterExpr(self, ctx:MapFunctionParser.ExprContext):
        pass

    # Exit a parse tree produced by MapFunctionParser#expr.
    def exitExpr(self, ctx:MapFunctionParser.ExprContext):
        pass



del MapFunctionParser