function sleep(s) {
    return new Promise(resolve => setTimeout(resolve,s))
}

console.log('Aquí funciona el backend de la aplicación de horarios')
while(true) {
    setTimeout(1000)
}