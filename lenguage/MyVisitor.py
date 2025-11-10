from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    def__init__(self):
        delf.memory={ }

    #Definimos la asignacion 
    def visitAssing(self,ctx):
        name=ctx.ID().getText()
        value=self.visit(ctx.expr())
        self.memory[name]=value
    #Definimos asignacion
    def visitPrint(self,ctx):
        vlaue=self.visit(ctx,ctx())
        print(value)