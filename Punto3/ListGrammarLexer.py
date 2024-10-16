# Generated from ListGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,49,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        1,1,1,1,2,1,2,1,3,3,3,19,8,3,1,3,4,3,22,8,3,11,3,12,3,23,1,3,1,3,
        4,3,28,8,3,11,3,12,3,29,3,3,32,8,3,1,3,1,3,1,3,4,3,37,8,3,11,3,12,
        3,38,3,3,41,8,3,1,4,4,4,44,8,4,11,4,12,4,45,1,4,1,4,0,0,5,1,1,3,
        2,5,3,7,4,9,5,1,0,2,2,0,43,43,45,45,3,0,9,10,13,13,32,32,55,0,1,
        1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,
        0,0,3,13,1,0,0,0,5,15,1,0,0,0,7,18,1,0,0,0,9,43,1,0,0,0,11,12,5,
        91,0,0,12,2,1,0,0,0,13,14,5,44,0,0,14,4,1,0,0,0,15,16,5,93,0,0,16,
        6,1,0,0,0,17,19,5,45,0,0,18,17,1,0,0,0,18,19,1,0,0,0,19,21,1,0,0,
        0,20,22,2,48,57,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,
        1,0,0,0,24,31,1,0,0,0,25,27,5,46,0,0,26,28,2,48,57,0,27,26,1,0,0,
        0,28,29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,25,
        1,0,0,0,31,32,1,0,0,0,32,40,1,0,0,0,33,34,5,101,0,0,34,36,7,0,0,
        0,35,37,2,48,57,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,
        1,0,0,0,39,41,1,0,0,0,40,33,1,0,0,0,40,41,1,0,0,0,41,8,1,0,0,0,42,
        44,7,1,0,0,43,42,1,0,0,0,44,45,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,
        0,46,47,1,0,0,0,47,48,6,4,0,0,48,10,1,0,0,0,8,0,18,23,29,31,38,40,
        45,1,6,0,0
    ]

class ListGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    NUMBER = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "','", "']'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "NUMBER", "WS" ]

    grammarFileName = "ListGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


