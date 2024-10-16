__author__ = 'jszheng'

from LabeledExprVisitor import LabeledExprVisitor
from LabeledExprParser import LabeledExprParser

class MyVisitor(LabeledExprVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = complex(self.visit(ctx.expr()))
        self.memory[name] = value
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitComplex(self, ctx):
        return ctx.COMPLEX().getText()

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name]
        return 0

    def visitMulDiv(self, ctx):
        left = complex(self.visit(ctx.expr(0)))
        right = complex(self.visit(ctx.expr(1)))
        if ctx.op.type == LabeledExprParser.MUL:
            return left * right
        return left / right

    def visitAddSub(self, ctx):
        left = complex(self.visit(ctx.expr(0)))
        right = complex(self.visit(ctx.expr(1)))
        if ctx.op.type == LabeledExprParser.ADD:
            return left + right
        return left - right
    def visitParens(self, ctx):
        return self.visit(ctx.expr())
