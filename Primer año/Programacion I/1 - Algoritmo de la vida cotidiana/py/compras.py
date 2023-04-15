# faltantesComida = [
#     "jamon",
#     "queso",
#     "pascualina",
# ]
    
# faltantesOtros = [
#     "bujía", 
#     "tornillos"
# ]

def definirFaltantes(param): 
    print("Revisa que hace falta en la casa")
    
    print(f"Hacen falta {param}? 1. Si 2.No?")
    confirmComida = int(input()) 
    if confirmComida == 1: 
        print("Escribe los alimentos que deberás conseguir")
        faltantesComida = input()
    
    print("Hace falta algun otro artículo del hogar? 1.Si 2.No")
    confirmOtros = int(input()) 
    if confirmOtros == 1:
        print("Escribe los artículos que deberás conseguir")
        faltantesOtros = input() 
        
    print(f"Deberas conseguir lo siguiente: 1. Comida: {faltantesComida} 2. Otros: {faltantesOtros}")
    return faltantesComida, faltantesOtros
    
definirFaltantes("alimentos")
definirFaltantes("artículo del hogar")

def mediosDeTransporte(): 
    print("Cual sera tu medio de transporte? 1. Auto 2.Caminando 3.Bici ")
    solitude = int(input())
    
    if solitude == 1 : 
        print("Acordate de las llaves! Y revisa el agua")
    elif solitude == 2: 
        print("Bien, te toca hacer ejercicio asi que ponete ropa comoda")
    elif solitude == 3:
        print("La cleta, buen ejercicio. Deberás llevar una mochila o algo para cargar los elementos de manera comoda. Las bolsas pueden meterse entre las ruedas.")
    else: 
        print("Disculpa, ese medio de transporte no esta disponible")

def establecimientos(): 
    if len(faltantesComida) >= 0 & len(faltantesOtros) >= 0:
        print(f"Debes ir a diversos establecimientos porque tienes los siguientes elementos: 1. {faltantesComida} 2.{faltantesOtros}")
        
    mediosDeTransporte()
    
