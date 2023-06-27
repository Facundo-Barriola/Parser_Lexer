from lexer import *

no_terminales =["Programa","Asignacion","Estructura","Expresion","Expresion_Prima","Valor","ListaExpresiones",
"Termino", "Termino_Prima","Factor"]

producciones = {
    'Programa':[['Asignacion','Programa'],['Estructura','Programa'], ['Estructura'],['Asignacion']], 
    
    'Asignacion':[['id'],['igual'],['Expresion']],
    
    'Estructura':[['para','id','desde','Valor','hasta','Valor','llaveIzquierda','Programa','llaveDerecha'],
    
    ['si','Expresion','entonces','llaveIzquierda','Programa','llaveDerecha','sino','llaveIzquierda','Programa','llaveDerecha'],
    
    ['si','Expresion','entonces','llaveIzquierda','Programa','llaveDerecha'],
    
    ['mostrar','ListaExpresiones'],
    
    ['aceptar','id']],
    
    'Valor':[['id'],['cte']],
    
    'Expresion':[["Termino",'Expresion_Prima'],['Termino']], 

    'Expresion_Prima':[['suma', 'Termino', 'Expresion_Prima'],['suma','Termino']],
    
    'Termino':[["Factor",'Termino_Prima'],['Factor']], 

    'Termino_Prima':[['multiplicacion','Factor','Termino_Prima'],['multiplicacion','Factor']],
    
    'Factor':[['parentesisIzquierdo','Expresion','parentesisDerecho'],['id'],['cte']],
    
    'ListaExpresiones':[['Expresion','puntoYComa',],['Expresion']]
}

def Parser(input):
    datos_parser ={
        'tokens':input,
        'posicion_indice':0,
        'error':False,
    }

    def principal():
        pni('Programa')
        token_actual= datos_parser['tokens'][datos_parser['posicion_indice']][0]
        if token_actual != 'EOF' or datos_parser['error']:
            print('La cadena no pertenece al lenguaje')
            return False
        print('La cadena es aceptada')
        return True

    def pni(no_terminales):
        for parteDerecha in producciones[no_terminales]:
            posicion_a_retroceder = datos_parser['posicion_indice']
            procesar(parteDerecha)
            if datos_parser['error']:
                datos_parser['posicion_indice']=posicion_a_retroceder
            else:
                break
    
    def procesar(parteDerecha):
        for simbolo in parteDerecha:
            token_actual= datos_parser['tokens'][datos_parser['posicion_indice']][0]
            datos_parser['error']= False
            if simbolo in no_terminales:
                pni(simbolo)
                if(datos_parser['error']):
                    break
            else:
                if simbolo == token_actual:
                    datos_parser['posicion_indice'] += 1
                else:
                    datos_parser['error']=True
                    break
            
    return principal()

Parser(lexer("variable=123"))
Parser(lexer('var=}'))
Parser(lexer('aux=2 * 3 + ( 3 * 9 )'))
Parser(lexer("para x desde 0 hasta 10 { y = 15 }"))
Parser(lexer("si a + b = c entonces { mostrar c sino d }"))
Parser(lexer("si 2 + 2 entonces { mostrar 4 } sino { mostrar 0 }"))
