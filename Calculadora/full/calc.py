import ply.lex as lex #libreria que ayuda a crear un an lexico
import ply.yacc as yacc #libreria que ayuda a crear un an semantico y sintactico
import sys

#creacion de una lista de tokens para el lex
tokens = [
    'INT', 'FLOAT', 'NAME', 'RESTA', 'SUMA',
    'DIVISION', 'MULTIPLICACION', 'EQUALS'
]
#formato para decirle al lexer, como luce un token de ese tipo
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'\/'
t_EQUALS = r'\='
#le dice a ply, ignorar esos caracteres al leer(espacio en blanco).
t_ignore = r' '

#creacion de funciones para los tokens numeros
def t_FLOAT(t):
    #define como se ven los floats: entero seguido de punto y entero
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    #define como se ven los enteros:un entero seguido de 1 o mas caracteres
    r'\d+'
    #convertir el valor a entero y devolvemos el entero
    t.value = int(t.value)
    return t



def t_NAME(t):
    #definicion de clases de caracteres a leer en las cadenas
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t
#creacion de error. se salta un token
def t_error(t):
    print("Caracteres ilegales!")
    t.lexer.skip(1)
    return t
print("hola")

lexer=lex.lex()

#para crear la asociacion izquierda y la preferencia de token
precedence = (
    ('left','SUMA','RESTA'),
    ('left','MULTIPLICACION','DIVISION')
)
#******ANALIZADOR LEXICO

#******PARSER
#creacion de funciones
#cada funcion crea un ARBOL
def p_calc(p):
    #definicion de no terminales
    '''
    calc : expression
         | var_assign
         | empty
    '''
    print(run(p[1]))
#una variable puede ser igual a una expresion o a otra variable
def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression
        
    '''
#creacion de tuplas para generar arbol a partir de las mismas
    p[0] = ('=', p[1], p[3])
#creacion de funciones recursivas de expresiones 1+2+3+4
def p_expression(p):
    '''
    expression : expression MULTIPLICACION expression
               | expression DIVISION expression
               | expression SUMA expression
               | expression RESTA expression
    '''
#creacion de arbol con el parser; p[0] es la expresion p[2] es el operador
#p[1 y 3] son valores que son una tupla
    p[0] = (p[2], p[1], p[3])

#creacion de funcion de expresion, puede ser int o float y le pasa el valor a p_calc
def p_expression_int_float(p):
    '''
    expression : INT
               | FLOAT
    '''
    p[0] = p[1]
#funcion para poder aceptar variables en las expresiones y poder sumarlas
def p_expression_var(p):
    '''
    expression : NAME
    '''
    p[0] = ('var', p[1])

def p_error(p):
    print('Error de sintaxis')

def p_empty(p):
    '''
    empty : 
    '''
    p[0] = None
parser = yacc.yacc()
env = {}
#funcion para correr el parser y el arbol
#analiza el operador y hace la operacion?????
def run(p):
    global env
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2]) 
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == '=':
            env[p[1]] = run(p[2])
            print(env)
        elif p[0] == 'var':
            if p[1] not in env:
                return 'Variable no definida encontrada'
            else:
                return env[p[1]]
    else:
        return p
#????????????????????
#******PARSER

#******ANALIZADOR LEXICO
#ciclo para pedir input de usuario
while True:
    try:
        s = input('Ingresa expresion>>')
#error de fin de file ctrl+d
    except EOFError: 
        break
    parser.parse(s)
#ANALIZADOR LEXICO CREADO*****************
