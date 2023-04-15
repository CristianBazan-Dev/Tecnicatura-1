const faltantesComida = [
    "jamon",
    "queso",
    "pascualina",
]
const faltantesOtros = [
    "bujía", 
    "tornillos"
]
    
const mediosDeTransporte = () =>{
    const solitude = prompt("Cuál será tu medio de transporte? 1. Auto 2. Caminando 3. Bici")
    if(solitude == 1){
        alert("Acordate de las llaves! Y revisa el agua")
    }else if(solitude == 2 ){
        alert("Bien, te toca hacer ejercicio asi que ponete ropa comoda")
    }else if(solitude == 3){
        alert("La cleta, buen ejercicio. Deberás llevar una mochila o algo para cargar los elementos de manera comoda. Las bolsas pueden meterse entre las ruedas.")
    }
    
    const trazadoDeViaje = () =>{
        const viaje = prompt("Introduce el viaje que realizarás")
    }

    
} 

const establecimientos = () =>{
    if(faltantesComida.length > 0 && faltantesOtros.length > 0){
        alert(`Debes ir a diversos establecimientos porque tienes los siguientes elementos: 
        1: ${faltantesComida}. 2:${faltantesOtros}`)
    }
    mediosDeTransporte()
}

establecimientos()

