import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from antlr4 import *
from ListGrammarLexer import ListGrammarLexer
from ListGrammarParser import ListGrammarParser
import sys
class ListVisitor(ParseTreeVisitor):
    def visitList(self, ctx:ListGrammarParser.ListContext):
        elements = [self.visit(element) for element in ctx.element()]
        return np.array(elements)

    def visitElement(self, ctx:ListGrammarParser.ElementContext):
        return float(ctx.NUMBER().getText())

def main():
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())
    lexer = ListGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ListGrammarParser(token_stream)
    tree = parser.prog()
    
    visitor = ListVisitor()
    array = visitor.visit(tree)
    
    time = np.arange(0, len(array)/10, 0.1)
    
    plt.figure(figsize=(10, 4))
    plt.subplot(2, 1, 1)
    plt.plot(time, array)
    plt.title('Original Time series')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    
    fourier_transform = np.fft.fft(array)
    frequencies = np.fft.fftfreq(len(array), 0.01)
    
    plt.figure(figsize=(10, 4))
    plt.subplot(2, 1, 1)
    plt.plot(frequencies, np.abs(fourier_transform))
    plt.title('Fourier Transform')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')

    plt.show()

if __name__ == '__main__':
    main()

