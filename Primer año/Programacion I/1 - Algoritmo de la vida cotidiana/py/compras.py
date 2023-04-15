# faltantesComida = [
#     "jamon",
#     "queso",
#     "pascualina",
# ]
    
# faltantesOtros = [
#     "bujía", 
#     "tornillos"
# ]


import pyttsx3 


# name = input("What's your name?")
# engine.say(f"hola, {name}")



def mediosDeTransporte(): 
    engine = pyttsx3.init()
    
    engine.say("Cual sera tu medio de transporte? 1. Auto 2.Caminando 3.Bici ")
    engine.runAndWait()
    
    solitude = int(input())
    
    if solitude == 1 : 
        engine.say("Acordate de las llaves! Y revisa el agua")
        engine.runAndWait()
    elif solitude == 2: 
        engine.say("Bien, te toca hacer ejercicio asi que ponete ropa comoda")
        engine.runAndWait()
    elif solitude == 3:
        engine.say("La cleta, buen ejercicio. Deberás llevar una mochila o algo para cargar los elementos de manera comoda. Las bolsas pueden meterse entre las ruedas.")
        engine.runAndWait()
    else: 
        engine.say("Disculpa, ese medio de transporte no esta disponible")
        engine.runAndWait()



def establecimientos(faltantes1, faltantes2): 
    engine = pyttsx3.init()
    if len(faltantes1) >= 0 & len(faltantes2) >= 0:
        engine.say(f"Debes ir a diversos establecimientos porque tienes los siguientes elementos: 1. {faltantes1} 2.{faltantes1}")
        engine.runAndWait()
    
    engine.say("Debes ir a un sólo establecimiento.")
        

def lista(): 
    engine = pyttsx3.init()

    engine.say("Revisa que hace falta en la casa")
    engine.runAndWait()

    engine.say("Hacen falta alimentos? 1. Si 2.No?")
    engine.runAndWait()
    
    confirmComida = int(input()) 
    if confirmComida == 1: 
        engine.say("Escribe los alimentos que deberás conseguir")
        engine.runAndWait()
        faltantesComida = input()
    
    engine.say(f"Hace falta algun otro artículo del hogar? 1.Si 2.No")
    engine.runAndWait()
    
    confirmOtros = int(input())
    if confirmOtros == 1:
        engine.say("Escribe los artículos que deberás conseguir")
        engine.runAndWait()
        faltantesOtros = input() 
        
        engine.say(f"Deberas conseguir lo siguiente: 1. Comida: {faltantesComida} 2. Otros: {faltantesOtros}")
        engine.runAndWait()
    
    mediosDeTransporte()
    establecimientos(faltantesComida, faltantesOtros)
    recorrido()
  
    
lista()

    
