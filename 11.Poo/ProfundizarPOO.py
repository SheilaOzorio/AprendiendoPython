class FabricaTelefonos():
    def __init__(this, marca, *colores, **modelos):
        this.marca = marca
        this.colores = colores
        this.modelos = modelos

telefono = FabricaTelefonos('Alcatel' 'Negro', 'Azul', m2 = 500, m3 = 700 )
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
telefono.memoria = 512
print(telefono.memoria)

#el init nos sirve para crear objetos, aunque debemos siempre igualarlos con el mismo objeto a como se muestra en las líneas 3-5. Debemos también agregarles un valor.
# el * nos sirve para decirle a nustro sistema que queremos una tupla, los dos ** nos sirven para crear un diccionario al agregarle el valor debemos poner = a como se muestra en la línea 7. 
#En la línea 11 se muestra el ejemplo de un atributo temporal. Este no es necesario colocarlo en la clase ni en algún objeto, si queremos mandarlo a llamar en otro objeto, no aparecerá ya que sólo está en el espacio para el primer objeto que fue al que se le asignó.