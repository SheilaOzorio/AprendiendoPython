#Ejercicio 1
cadena = 'Te quiero solo como amigo'

print(cadena [0 : 2])
print((cadena[22 : 25]))
print( len(cadena))
print((cadena[-25 : 0]))
print(cadena[ : : 2])  #Imprime de dos en dos 
print(cadena[ : : -1]) #Metodo para imprimir al revez
print( cadena + cadena [ : : -1]) #Metodo para imprimir normal y al revez de forma junta : Te quiero solo como amigoogima omoc olos oreiuq eT

#Ejercicio 2

cadena2 = "este es el uso del metodo Replace"
remplazando = cadena2.replace("e" , "E")
print(remplazando)
#Esta función está remplezando todas las "e" por "E", esto con ayuda del metodo "replace"

cadena1 = "Separado"
print(cadena1)

remplazar1 = cadena1.replace ("" , ",") 
print(remplazar1)
#A esta función le estamos diciendo que remplace los lugares en blanco (entre letra y letra), con "", y que lo remplace con ",".
