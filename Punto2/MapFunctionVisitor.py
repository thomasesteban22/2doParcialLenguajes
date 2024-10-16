# Generated from MapFunction.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MapFunctionParser import MapFunctionParser
else:
    from MapFunctionParser import MapFunctionParser

# This class defines a complete generic visitor for a parse tree produced by MapFunctionParser.

class MapFunctionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MapFunctionParser#prog.
    def visitProg(self, ctx:MapFunctionParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFunctionParser#stat.
    def visitStat(self, ctx:MapFunctionParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFunctionParser#mapFunction.
    def visitMapFunction(self, ctx:MapFunctionParser.MapFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFunctionParser#filterFunction.
    def visitFilterFunction(self, ctx:MapFunctionParser.FilterFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFunctionParser#iterable.
    def visitIterable(self, ctx:MapFunctionParser.IterableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFunctionParser#list.
    def visitList(self, ctx:MapFunctionParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFunctionParser#tuple.
    def visitTuple(self, ctx:MapFunctionParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFunctionParser#function.
    def visitFunction(self, ctx:MapFunctionParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFunctionParser#elements.
    def visitElements(self, ctx:MapFunctionParser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFunctionParser#lambdaExpr.
    def visitLambdaExpr(self, ctx:MapFunctionParser.LambdaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFunctionParser#op.
    def visitOp(self, ctx:MapFunctionParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFunctionParser#var.
    def visitVar(self, ctx:MapFunctionParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFunctionParser#expr.
    def visitExpr(self, ctx:MapFunctionParser.ExprContext):
        return self.visitChildren(ctx)



del MapFunctionParser