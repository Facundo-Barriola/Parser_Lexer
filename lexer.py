from automatas import Estado_Final
from automatas import Estado_No_Final
from automatas import afd_aceptar
from automatas import afd_cte
from automatas import afd_desde
from automatas import afd_entonces
from automatas import afd_hasta
from automatas import afd_id
from automatas import afd_para
from automatas import afd_si
from automatas import afd_mostrar
from automatas import afd_sino
from automatas import afd_suma
from automatas import afd_multiplicacion 
from automatas import afd_llave_izquierda
from automatas import afd_llave_derecha
from automatas import afd_igual
from automatas import afd_parentesis_izq
from automatas import afd_parentesis_derecho
from automatas import afd_punto_y_coma

tokens_posibles=[("aceptar", afd_aceptar),("desde",afd_desde),("entonces",afd_entonces),
("hasta", afd_hasta),("para", afd_para),("mostrar",afd_mostrar),("sino",afd_sino),("si",afd_si),("suma",afd_suma),
("multiplicacion", afd_multiplicacion),("parentesisIzquierdo", afd_parentesis_izq),("parentesisDerecho", afd_parentesis_derecho),
("llaveIzquierda", afd_llave_izquierda),("llaveDerecha", afd_llave_derecha),("igual", afd_igual),
("puntoYComa", afd_punto_y_coma),("id", afd_id),("cte", afd_cte)]

def lexer(codigo_fuente):
    tokens=[]
    index=0
    while index < len(codigo_fuente):

        while  index < len(codigo_fuente) and codigo_fuente[index].isspace():
            index += 1
        
        comienzo_lexema=index
        posibles_tokens=[]
        posibles_tokens_con_un_caracter_mas=[]
        lexema=""
        all_trapped= False

        while not all_trapped and index<len(codigo_fuente)+1:
            all_trapped=True
            lexema=codigo_fuente[comienzo_lexema:index +1]
            # print(comienzo_lexema,index+1,lexema)
            posibles_tokens=posibles_tokens_con_un_caracter_mas
            posibles_tokens_con_un_caracter_mas=[]
            
            for (algun_token, afd) in tokens_posibles:
                simulacion_afd= afd(lexema)
                if simulacion_afd == Estado_Final:
                    posibles_tokens_con_un_caracter_mas.append(algun_token)
                    all_trapped= False
                elif simulacion_afd == Estado_No_Final:
                    all_trapped= False
            
            index = index +1
        
        if len(posibles_tokens) == 0:
            print("ERROR: TOKEN DESCONOCIDO" + lexema)
        
        index=index-1
        algun_token=posibles_tokens[0]
        token=(algun_token, codigo_fuente[comienzo_lexema:index])
        tokens.append(token)
    
    end_token_Posible="EOF"
    end_lexeme="EOF"
    end_token=(end_token_Posible,end_lexeme)
    tokens.append(end_token)
        
    return tokens

# print(lexer("hola *"))
# print(lexer("2 + 2"))
# print(lexer("para aceptar"))
# print(lexer("( { mostrar } )"))
# print(lexer("entonces"))