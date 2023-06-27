Estado_Final="Estado Final"
Estado_No_Final="Estado no final"
Estado_Trampa="Estado Trampa"

def afd_para(cadena):
    estado_actual=0
    estados_finales=[4]
    for c in cadena:
        if (c=="p" and estado_actual==0):
            estado_actual=1
        elif (c=="a" and estado_actual==1):
            estado_actual=2
        elif (c=="r" and estado_actual==2):
            estado_actual=3
        elif (c=="a" and estado_actual==3):
            estado_actual=4
        else:
            estado_actual=-1
            break
    if estado_actual == -1:
        return (Estado_Trampa)
    elif estado_actual in estados_finales:
        return (Estado_Final)
    else:
        return (Estado_No_Final)


def afd_entonces(cadena):
    estado_actual=0
    estados_finales=[8]
    for c in cadena:
        if (c=="e" and estado_actual==0):
            estado_actual=1
        elif (c=="n" and estado_actual==1):
            estado_actual=2
        elif (c=="t" and estado_actual==2):
            estado_actual=3
        elif (c=="o" and estado_actual==3):
            estado_actual=4
        elif (c=="n" and estado_actual==4):
            estado_actual=5
        elif(c=="c" and estado_actual==5):
            estado_actual=6
        elif(c=="e" and estado_actual==6):
            estado_actual=7
        elif(c=="s" and estado_actual==7):
            estado_actual=8
        else:
            estado_actual=-1
            break
    if estado_actual == -1:
        return (Estado_Trampa)
    elif estado_actual in estados_finales:
        return (Estado_Final)
    else:
        return (Estado_No_Final)

def afd_aceptar(cadena):
    estado_actual=0
    estados_finales=[7]
    for c in cadena:
        if (c=="a" and estado_actual==0):
            estado_actual=1
        elif (c=="c" and estado_actual==1):
            estado_actual=2
        elif (c=="e" and estado_actual==2):
            estado_actual=3
        elif (c=="p" and estado_actual==3):
            estado_actual=4
        elif (c=="t" and estado_actual==4):
            estado_actual=5
        elif(c=="a" and estado_actual==5):
            estado_actual=6
        elif(c=="r" and estado_actual==6):
            estado_actual=7
        else:
            estado_actual=-1
            break
    if estado_actual == -1:
        return (Estado_Trampa)
    elif estado_actual in estados_finales:
        return (Estado_Final)
    else:
        return (Estado_No_Final)

def afd_mostrar(cadena):
    estado_actual=0
    estados_finales=[7]
    for c in cadena:
        if (c=="m" and estado_actual==0):
            estado_actual=1
        elif (c=="o" and estado_actual==1):
            estado_actual=2
        elif (c=="s" and estado_actual==2):
            estado_actual=3
        elif (c=="t" and estado_actual==3):
            estado_actual=4
        elif (c=="r" and estado_actual==4):
            estado_actual=5
        elif(c=="a" and estado_actual==5):
            estado_actual=6
        elif(c=="r" and estado_actual==6):
            estado_actual=7
        else:
            estado_actual=-1
            break
    if estado_actual == -1:
        return (Estado_Trampa)
    elif estado_actual in estados_finales:
        return (Estado_Final)
    else:
        return (Estado_No_Final)

def afd_desde(cadena):
    estado_actual=0
    estados_finales=[5]
    for c in cadena:
        if (c=="d" and estado_actual==0):
            estado_actual=1
        elif (c=="e" and estado_actual==1):
            estado_actual=2
        elif (c=="s" and estado_actual==2):
            estado_actual=3
        elif (c=="d" and estado_actual==3):
            estado_actual=4
        elif (c=="e" and estado_actual==4):
            estado_actual=5
        else:
            estado_actual=-1
            break
    if estado_actual == -1:
        return (Estado_Trampa)
    elif estado_actual in estados_finales:
        return (Estado_Final)
    else:
        return (Estado_No_Final)

def afd_hasta(cadena):
    estado_actual=0
    estados_finales=[5]
    for c in cadena:
        if (c=="h" and estado_actual==0):
            estado_actual=1
        elif (c=="a" and estado_actual==1):
            estado_actual=2
        elif (c=="s" and estado_actual==2):
            estado_actual=3
        elif (c=="t" and estado_actual==3):
            estado_actual=4
        elif (c=="a" and estado_actual==4):
            estado_actual=5
        else:
            estado_actual=-1
            break
    if estado_actual == -1:
        return (Estado_Trampa)
    elif estado_actual in estados_finales:
        return (Estado_Final)
    else:
        return (Estado_No_Final)

def afd_sino(cadena):
    estado_actual=0
    estados_finales=[4]
    for c in cadena:
        if (c=="s" and estado_actual==0):
            estado_actual=1
        elif (c=="i" and estado_actual==1):
            estado_actual=2
        elif (c=="n" and estado_actual==2):
            estado_actual=3
        elif (c=="o" and estado_actual==3):
            estado_actual=4
        else:
            estado_actual=-1
            break
    if estado_actual == -1:
        return (Estado_Trampa)
    elif estado_actual in estados_finales:
        return (Estado_Final)
    else:
        return (Estado_No_Final)

def afd_si(cadena):
    estado_actual=0
    estados_finales=[2]
    for c in cadena:
        if (c=="s" and estado_actual==0):
            estado_actual=1
        elif (c=="i" and estado_actual==1):
            estado_actual=2
        else:
            estado_actual=-1
            break
    if estado_actual == -1:
        return (Estado_Trampa)
    elif estado_actual in estados_finales:
        return (Estado_Final)
    else:
        return (Estado_No_Final)

def afd_igual(cadena):
    estado_actual=0
    estados_finales=[1]
    for c in cadena:
        if (c=="=" and estado_actual==0):
            estado_actual=1
        else:
            estado_actual=-1
            break
    if estado_actual == -1:
        return (Estado_Trampa)
    elif estado_actual in estados_finales:
        return (Estado_Final)
    else:
        return (Estado_No_Final)

def afd_suma(cadena):
    estado_actual=0
    estados_finales=[1]
    for c in cadena:
        if (c=="+" and estado_actual==0):
            estado_actual=1
        else:
            estado_actual=-1
            break
    if estado_actual == -1:
        return (Estado_Trampa)
    elif estado_actual in estados_finales:
        return (Estado_Final)
    else:
        return (Estado_No_Final)

def afd_multiplicacion(cadena):
    estado_actual=0
    estados_finales=[1]
    for c in cadena:
        if (c=="*" and estado_actual==0):
            estado_actual=1
        else:
            estado_actual=-1
            break
    if estado_actual == -1:
        return (Estado_Trampa)
    elif estado_actual in estados_finales:
        return (Estado_Final)
    else:
        return (Estado_No_Final)

def afd_punto_y_coma(cadena):
    estado_actual=0
    estados_finales=[1]
    for c in cadena:
        if (c==";" and estado_actual==0):
            estado_actual=1
        else:
            estado_actual=-1
            break
    if estado_actual == -1:
        return (Estado_Trampa)
    elif estado_actual in estados_finales:
        return (Estado_Final)
    else:
        return (Estado_No_Final)

def afd_parentesis_izq(cadena):
    estado_actual=0
    estados_finales=[1]
    for c in cadena:
        if (c=="(" and estado_actual==0):
            estado_actual=1
        else:
            estado_actual=-1
            break
    if estado_actual == -1:
        return (Estado_Trampa)
    elif estado_actual in estados_finales:
        return (Estado_Final)
    else:
        return (Estado_No_Final)

def afd_parentesis_derecho(cadena):
    estado_actual=0
    estados_finales=[1]
    for c in cadena:
        if (c==")" and estado_actual==0):
            estado_actual=1
        else:
            estado_actual=-1
            break
    if estado_actual == -1:
        return (Estado_Trampa)
    elif estado_actual in estados_finales:
        return (Estado_Final)
    else:
        return (Estado_No_Final)


def afd_llave_izquierda(cadena):
    estado_actual=0
    estados_finales=[1]
    for c in cadena:
        if (c=="{" and estado_actual==0):
            estado_actual=1
        else:
            estado_actual=-1
            break
    if estado_actual == -1:
        return (Estado_Trampa)
    elif estado_actual in estados_finales:
        return (Estado_Final)
    else:
        return (Estado_No_Final)

def afd_llave_derecha(cadena):
    estado_actual=0
    estados_finales=[1]
    for c in cadena:
        if (c=="}" and estado_actual==0):
            estado_actual=1
        else:
            estado_actual=-1
            break
    if estado_actual == -1:
        return (Estado_Trampa)
    elif estado_actual in estados_finales:
        return (Estado_Final)
    else:
        return (Estado_No_Final)

def afd_id(cadena):
    estado_Actual = 0

    for caracter in cadena:
        if caracter.isalpha():
            estado_Actual = 1
        elif(caracter.isnumeric() and estado_Actual==1):
            estado_Actual = 1
        else:
            estado_Actual=-1
            break

    if estado_Actual == -1:
        return(Estado_Trampa)
    elif estado_Actual == 1: 
        return(Estado_Final)
    else:
        return(Estado_No_Final)

def afd_cte(cadena):
    estado_actual=0
    estados_finales=[1]
    for c in cadena:
        if c.isnumeric():
            estado_actual=1
        else:
            estado_actual=-1
    if estado_actual in estados_finales:
        return(Estado_Final)
    else:
        return(Estado_Trampa)

