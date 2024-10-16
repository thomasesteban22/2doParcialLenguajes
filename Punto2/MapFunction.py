import sys
from antlr4 import *
from MapFunctionLexer import MapFunctionLexer
from MapFunctionParser import MapFunctionParser


from MyVisitor import MyVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = MapFunctionLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MapFunctionParser(token_stream)
    tree = parser.prog()

    visitor = MyVisitor()
    visitor.visit(tree)
