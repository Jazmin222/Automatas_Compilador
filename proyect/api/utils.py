import antlr4 import*
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
import io 
import sys
from MyVisitor import MyVisitor


def run_code(code:str):
    input stream=InputStream(code)
    lexer=GrammarLexer(input_stream)
    stream=CommonTokenStream(Lexer)
    parser=GrammarParser(stream)
    tree=parser.program()
    
    #Capturan la salida
    old_stdout=sys.stdout()
    buf = io.StringIO()
    sys.stdout = buf

    #Creamos un objeto de nuestro visitor
    visitor = MyVisitor()
    #Visitamos el arbol con nuestro visitor
    visitor.visit(tree)
    #Capturamos la salida
    output=buf.getvalue()

    return output
