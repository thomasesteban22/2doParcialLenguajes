from MapFunctionVisitor import MapFunctionVisitor
from MapFunctionParser import MapFunctionParser

class MyVisitor(MapFunctionVisitor):
    def __init__(self):
        self.functions = {
            'Upper': lambda x: x.upper(),
            'Lower': lambda x: x.lower(),
            'Squared': lambda x: x ** 2,
            'Cube': lambda x: x ** 3,
            'Module2': lambda x: x % 2,
        }

    def visitMapFunction(self, ctx):
        function_name = ctx.lambdaExpr().getText()
        iterable_elements = ctx.iterable().getText()
        iterable_elements=list(iterable_elements[1:-1].split(','))
        if iterable_elements[0].isdigit():
            iterable_elements=list(map(int,iterable_elements))
        function_name=function_name.replace('lambda','lambda ')
        result=list(map(eval(function_name),iterable_elements))
        print(result)
        return result

    def visitFilterFunction(self, ctx):
        function_name = ctx.lambdaExpr().getText()
        iterable_elements = ctx.iterable().getText()
        iterable_elements=list(iterable_elements[1:-1].split(','))
        if iterable_elements[0].isdigit():
            iterable_elements=list(map(int,iterable_elements))
        function_name=function_name.replace('lambda','lambda ')
        result=list(filter(eval(function_name),iterable_elements))
        print(result)
        return result

    def visitElements(self, ctx):
        return [self.visit(expr) for expr in ctx.expr()]

    def visitINT(self, ctx):
        return int(ctx.getText())

    def visitFLOAT(self, ctx):
        return float(ctx.getText())

    def visitSTRING(self, ctx):
        return ctx.getText()[1:-1]  # Remove surrounding quotes

    def visitID(self, ctx):
        return ctx.getText()
