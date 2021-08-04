from time import sleep

sleep(1)
print("¿QUIERES SABER TU FUTURO?")
print("con este código sabrás lo que las estrellas y los procesadores tienen para ti\n")

animacion = [".", "..", "...", " "]
for i in animacion:
    print(i)
    sleep(0.5)

signo = input("Ingresa tu signo zodiacal: ")

sig_zod = { 
"Aries" : "Marzo 21 - Abril 19", 
"Tauro" : "Abril 20 - Mayo 20",
"Geminis" : "Mayo 21 - Junio 20",
"Cáncer": "Junio 21 - Julio 22", 
"Leo" : "Julio 23 - Agosto 22", 
"Virgo" : "Agosto 23 - Septiembre 22", 
"Libra" : "Septiembre 23 - Octubre 22", 
"Escorpio" : "Octubre 23 - Noviembre 21",
"Sagitario" : "Noviembre 22 - Diciembre 21",
"Capricornio" : "Diciembre 22 - Enero 19",
"Acuario" : "Enero 20 - Febrero 18",
"Picis": "Febrero 19 - Marzo 20"}

if signo in sig_zod:
    print("Excelente %s, en un ratico te diré lo que te prepara el futuro." % signo)
else:
    print("%s no es un signo del zodiaco, no me quieras ver la cara de estúpida." % signo) 

sleep(2)

print("%s: el día de hoy te va a ir de lujo porque weles bien." % signo.upper())
