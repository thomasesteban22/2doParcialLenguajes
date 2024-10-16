# Generated from MapFunction.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,144,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,1,1,1,1,1,1,1,1,1,1,1,3,1,38,8,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,3,4,56,8,4,
        1,5,1,5,3,5,60,8,5,1,5,1,5,1,6,1,6,3,6,66,8,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,86,8,7,
        1,7,1,7,1,7,1,7,1,7,1,7,3,7,94,8,7,1,7,3,7,97,8,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,3,7,106,8,7,3,7,108,8,7,1,8,1,8,1,8,5,8,113,8,8,10,
        8,12,8,116,9,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,138,8,10,1,11,
        1,11,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,3,
        1,0,12,13,1,0,26,28,2,0,26,26,28,29,158,0,27,1,0,0,0,2,37,1,0,0,
        0,4,39,1,0,0,0,6,46,1,0,0,0,8,55,1,0,0,0,10,57,1,0,0,0,12,63,1,0,
        0,0,14,107,1,0,0,0,16,109,1,0,0,0,18,117,1,0,0,0,20,137,1,0,0,0,
        22,139,1,0,0,0,24,141,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,29,
        1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,1,1,0,0,0,31,32,3,4,2,0,32,
        33,5,34,0,0,33,38,1,0,0,0,34,35,3,6,3,0,35,36,5,34,0,0,36,38,1,0,
        0,0,37,31,1,0,0,0,37,34,1,0,0,0,38,3,1,0,0,0,39,40,5,1,0,0,40,41,
        5,2,0,0,41,42,3,18,9,0,42,43,5,3,0,0,43,44,3,8,4,0,44,45,5,4,0,0,
        45,5,1,0,0,0,46,47,5,5,0,0,47,48,5,2,0,0,48,49,3,18,9,0,49,50,5,
        3,0,0,50,51,3,8,4,0,51,52,5,4,0,0,52,7,1,0,0,0,53,56,3,10,5,0,54,
        56,3,12,6,0,55,53,1,0,0,0,55,54,1,0,0,0,56,9,1,0,0,0,57,59,5,6,0,
        0,58,60,3,16,8,0,59,58,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,62,
        5,7,0,0,62,11,1,0,0,0,63,65,5,2,0,0,64,66,3,16,8,0,65,64,1,0,0,0,
        65,66,1,0,0,0,66,67,1,0,0,0,67,68,5,4,0,0,68,13,1,0,0,0,69,70,5,
        27,0,0,70,71,3,20,10,0,71,72,3,22,11,0,72,108,1,0,0,0,73,74,5,27,
        0,0,74,108,5,8,0,0,75,76,5,27,0,0,76,108,5,9,0,0,77,78,5,27,0,0,
        78,108,5,10,0,0,79,80,5,11,0,0,80,81,5,27,0,0,81,85,5,4,0,0,82,83,
        3,20,10,0,83,84,3,22,11,0,84,86,1,0,0,0,85,82,1,0,0,0,85,86,1,0,
        0,0,86,108,1,0,0,0,87,88,5,27,0,0,88,89,3,20,10,0,89,90,3,22,11,
        0,90,91,3,20,10,0,91,93,3,22,11,0,92,94,7,0,0,0,93,92,1,0,0,0,93,
        94,1,0,0,0,94,96,1,0,0,0,95,97,3,14,7,0,96,95,1,0,0,0,96,97,1,0,
        0,0,97,108,1,0,0,0,98,99,5,27,0,0,99,100,5,6,0,0,100,101,5,26,0,
        0,101,105,5,7,0,0,102,103,3,20,10,0,103,104,3,22,11,0,104,106,1,
        0,0,0,105,102,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,69,1,0,
        0,0,107,73,1,0,0,0,107,75,1,0,0,0,107,77,1,0,0,0,107,79,1,0,0,0,
        107,87,1,0,0,0,107,98,1,0,0,0,108,15,1,0,0,0,109,114,3,24,12,0,110,
        111,5,3,0,0,111,113,3,24,12,0,112,110,1,0,0,0,113,116,1,0,0,0,114,
        112,1,0,0,0,114,115,1,0,0,0,115,17,1,0,0,0,116,114,1,0,0,0,117,118,
        5,14,0,0,118,119,5,27,0,0,119,120,5,15,0,0,120,121,3,14,7,0,121,
        19,1,0,0,0,122,138,5,32,0,0,123,138,5,33,0,0,124,138,5,30,0,0,125,
        138,5,31,0,0,126,138,5,16,0,0,127,138,5,17,0,0,128,129,5,18,0,0,
        129,130,5,27,0,0,130,138,5,19,0,0,131,138,5,20,0,0,132,138,5,21,
        0,0,133,138,5,22,0,0,134,138,5,23,0,0,135,138,5,24,0,0,136,138,5,
        25,0,0,137,122,1,0,0,0,137,123,1,0,0,0,137,124,1,0,0,0,137,125,1,
        0,0,0,137,126,1,0,0,0,137,127,1,0,0,0,137,128,1,0,0,0,137,131,1,
        0,0,0,137,132,1,0,0,0,137,133,1,0,0,0,137,134,1,0,0,0,137,135,1,
        0,0,0,137,136,1,0,0,0,138,21,1,0,0,0,139,140,7,1,0,0,140,23,1,0,
        0,0,141,142,7,2,0,0,142,25,1,0,0,0,12,29,37,55,59,65,85,93,96,105,
        107,114,137
    ]

class MapFunctionParser ( Parser ):

    grammarFileName = "MapFunction.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'map'", "'('", "','", "')'", "'filter'", 
                     "'['", "']'", "'.upper()'", "'.lower()'", "'.capitalize()'", 
                     "'len('", "' and '", "' or '", "'lambda'", "':'", "'%'", 
                     "'**'", "'.'", "'()'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "ID", "FLOAT", "STRING", 
                      "MUL", "DIV", "ADD", "SUB", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_mapFunction = 2
    RULE_filterFunction = 3
    RULE_iterable = 4
    RULE_list = 5
    RULE_tuple = 6
    RULE_function = 7
    RULE_elements = 8
    RULE_lambdaExpr = 9
    RULE_op = 10
    RULE_var = 11
    RULE_expr = 12

    ruleNames =  [ "prog", "stat", "mapFunction", "filterFunction", "iterable", 
                   "list", "tuple", "function", "elements", "lambdaExpr", 
                   "op", "var", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    INT=26
    ID=27
    FLOAT=28
    STRING=29
    MUL=30
    DIV=31
    ADD=32
    SUB=33
    NEWLINE=34
    WS=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapFunctionParser.StatContext)
            else:
                return self.getTypedRuleContext(MapFunctionParser.StatContext,i)


        def getRuleIndex(self):
            return MapFunctionParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MapFunctionParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.stat()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==5):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mapFunction(self):
            return self.getTypedRuleContext(MapFunctionParser.MapFunctionContext,0)


        def NEWLINE(self):
            return self.getToken(MapFunctionParser.NEWLINE, 0)

        def filterFunction(self):
            return self.getTypedRuleContext(MapFunctionParser.FilterFunctionContext,0)


        def getRuleIndex(self):
            return MapFunctionParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = MapFunctionParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.mapFunction()
                self.state = 32
                self.match(MapFunctionParser.NEWLINE)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.filterFunction()
                self.state = 35
                self.match(MapFunctionParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaExpr(self):
            return self.getTypedRuleContext(MapFunctionParser.LambdaExprContext,0)


        def iterable(self):
            return self.getTypedRuleContext(MapFunctionParser.IterableContext,0)


        def getRuleIndex(self):
            return MapFunctionParser.RULE_mapFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapFunction" ):
                listener.enterMapFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapFunction" ):
                listener.exitMapFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapFunction" ):
                return visitor.visitMapFunction(self)
            else:
                return visitor.visitChildren(self)




    def mapFunction(self):

        localctx = MapFunctionParser.MapFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mapFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(MapFunctionParser.T__0)
            self.state = 40
            self.match(MapFunctionParser.T__1)
            self.state = 41
            self.lambdaExpr()
            self.state = 42
            self.match(MapFunctionParser.T__2)
            self.state = 43
            self.iterable()
            self.state = 44
            self.match(MapFunctionParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaExpr(self):
            return self.getTypedRuleContext(MapFunctionParser.LambdaExprContext,0)


        def iterable(self):
            return self.getTypedRuleContext(MapFunctionParser.IterableContext,0)


        def getRuleIndex(self):
            return MapFunctionParser.RULE_filterFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterFunction" ):
                listener.enterFilterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterFunction" ):
                listener.exitFilterFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterFunction" ):
                return visitor.visitFilterFunction(self)
            else:
                return visitor.visitChildren(self)




    def filterFunction(self):

        localctx = MapFunctionParser.FilterFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(MapFunctionParser.T__4)
            self.state = 47
            self.match(MapFunctionParser.T__1)
            self.state = 48
            self.lambdaExpr()
            self.state = 49
            self.match(MapFunctionParser.T__2)
            self.state = 50
            self.iterable()
            self.state = 51
            self.match(MapFunctionParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(MapFunctionParser.ListContext,0)


        def tuple_(self):
            return self.getTypedRuleContext(MapFunctionParser.TupleContext,0)


        def getRuleIndex(self):
            return MapFunctionParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterable" ):
                return visitor.visitIterable(self)
            else:
                return visitor.visitChildren(self)




    def iterable(self):

        localctx = MapFunctionParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_iterable)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.list_()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.tuple_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self):
            return self.getTypedRuleContext(MapFunctionParser.ElementsContext,0)


        def getRuleIndex(self):
            return MapFunctionParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = MapFunctionParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(MapFunctionParser.T__5)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 872415232) != 0):
                self.state = 58
                self.elements()


            self.state = 61
            self.match(MapFunctionParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self):
            return self.getTypedRuleContext(MapFunctionParser.ElementsContext,0)


        def getRuleIndex(self):
            return MapFunctionParser.RULE_tuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple" ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple" ):
                listener.exitTuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple" ):
                return visitor.visitTuple(self)
            else:
                return visitor.visitChildren(self)




    def tuple_(self):

        localctx = MapFunctionParser.TupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(MapFunctionParser.T__1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 872415232) != 0):
                self.state = 64
                self.elements()


            self.state = 67
            self.match(MapFunctionParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MapFunctionParser.ID, 0)

        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapFunctionParser.OpContext)
            else:
                return self.getTypedRuleContext(MapFunctionParser.OpContext,i)


        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapFunctionParser.VarContext)
            else:
                return self.getTypedRuleContext(MapFunctionParser.VarContext,i)


        def function(self):
            return self.getTypedRuleContext(MapFunctionParser.FunctionContext,0)


        def INT(self):
            return self.getToken(MapFunctionParser.INT, 0)

        def getRuleIndex(self):
            return MapFunctionParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = MapFunctionParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.match(MapFunctionParser.ID)
                self.state = 70
                self.op()
                self.state = 71
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(MapFunctionParser.ID)
                self.state = 74
                self.match(MapFunctionParser.T__7)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.match(MapFunctionParser.ID)
                self.state = 76
                self.match(MapFunctionParser.T__8)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.match(MapFunctionParser.ID)
                self.state = 78
                self.match(MapFunctionParser.T__9)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 79
                self.match(MapFunctionParser.T__10)
                self.state = 80
                self.match(MapFunctionParser.ID)
                self.state = 81
                self.match(MapFunctionParser.T__3)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16172646400) != 0):
                    self.state = 82
                    self.op()
                    self.state = 83
                    self.var()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 87
                self.match(MapFunctionParser.ID)
                self.state = 88
                self.op()
                self.state = 89
                self.var()
                self.state = 90
                self.op()
                self.state = 91
                self.var()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12 or _la==13:
                    self.state = 92
                    _la = self._input.LA(1)
                    if not(_la==12 or _la==13):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11 or _la==27:
                    self.state = 95
                    self.function()


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 98
                self.match(MapFunctionParser.ID)
                self.state = 99
                self.match(MapFunctionParser.T__5)
                self.state = 100
                self.match(MapFunctionParser.INT)
                self.state = 101
                self.match(MapFunctionParser.T__6)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16172646400) != 0):
                    self.state = 102
                    self.op()
                    self.state = 103
                    self.var()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapFunctionParser.ExprContext)
            else:
                return self.getTypedRuleContext(MapFunctionParser.ExprContext,i)


        def getRuleIndex(self):
            return MapFunctionParser.RULE_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElements" ):
                listener.enterElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElements" ):
                listener.exitElements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = MapFunctionParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.expr()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 110
                self.match(MapFunctionParser.T__2)
                self.state = 111
                self.expr()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MapFunctionParser.ID, 0)

        def function(self):
            return self.getTypedRuleContext(MapFunctionParser.FunctionContext,0)


        def getRuleIndex(self):
            return MapFunctionParser.RULE_lambdaExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaExpr" ):
                listener.enterLambdaExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaExpr" ):
                listener.exitLambdaExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaExpr" ):
                return visitor.visitLambdaExpr(self)
            else:
                return visitor.visitChildren(self)




    def lambdaExpr(self):

        localctx = MapFunctionParser.LambdaExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_lambdaExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(MapFunctionParser.T__13)
            self.state = 118
            self.match(MapFunctionParser.ID)
            self.state = 119
            self.match(MapFunctionParser.T__14)
            self.state = 120
            self.function()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(MapFunctionParser.ADD, 0)

        def SUB(self):
            return self.getToken(MapFunctionParser.SUB, 0)

        def MUL(self):
            return self.getToken(MapFunctionParser.MUL, 0)

        def DIV(self):
            return self.getToken(MapFunctionParser.DIV, 0)

        def ID(self):
            return self.getToken(MapFunctionParser.ID, 0)

        def getRuleIndex(self):
            return MapFunctionParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = MapFunctionParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_op)
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.match(MapFunctionParser.ADD)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(MapFunctionParser.SUB)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.match(MapFunctionParser.MUL)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 125
                self.match(MapFunctionParser.DIV)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 126
                self.match(MapFunctionParser.T__15)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 127
                self.match(MapFunctionParser.T__16)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 7)
                self.state = 128
                self.match(MapFunctionParser.T__17)
                self.state = 129
                self.match(MapFunctionParser.ID)
                self.state = 130
                self.match(MapFunctionParser.T__18)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 8)
                self.state = 131
                self.match(MapFunctionParser.T__19)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 9)
                self.state = 132
                self.match(MapFunctionParser.T__20)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 10)
                self.state = 133
                self.match(MapFunctionParser.T__21)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 11)
                self.state = 134
                self.match(MapFunctionParser.T__22)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 12)
                self.state = 135
                self.match(MapFunctionParser.T__23)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 13)
                self.state = 136
                self.match(MapFunctionParser.T__24)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MapFunctionParser.ID, 0)

        def INT(self):
            return self.getToken(MapFunctionParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MapFunctionParser.FLOAT, 0)

        def getRuleIndex(self):
            return MapFunctionParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = MapFunctionParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MapFunctionParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MapFunctionParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MapFunctionParser.STRING, 0)

        def getRuleIndex(self):
            return MapFunctionParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MapFunctionParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 872415232) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





