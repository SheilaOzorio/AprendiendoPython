class casaMelendezOzorio():
    def __init__(self , marca , color):
        self.marca = marca
        self.color = color
        print('El objeto {} ha sido creado'.format(self.marca))
  
    def __str__(self):
        return('El objeto es {}'.format(self.marca))
    def __del__(self):
         print('El objeto {} ha sido destruido'.format(self.marca))

estufa = casaMelendezOzorio('Samsumg', 'LG')
print(estufa.marca)
print(estufa)
# El self sirve para inciarlizar los valores
#Primero se crea el objeto y yo puedo acceder a sus atributos, que previamente ya tendrán los valores que yo le asigne.
#Es importante que cuando trabajemos ocn atributos dentro de la clase tengamos que ponerlos SIEMPRE con self. Ejemplo: (self.marca). Pero si es fuera de la clase, ya no será necesario el self.
#Así como existe un 'constructor' que es el INIT, también existe un "destructor", que es el DEL, se le dice constructor porque el init crea atributos/valores, mientras que el DEL elimina todos los objetos una vez finalizada la ejecuciónse ejecuta al finalizar la ejecución de un programa que tiene clases y que tiene objetos y
#el metodo init funcionará cuando tengamos minimo un objeto, nos sirve para que se ejecute con sólo iniciar el objeto.se recomienda siempre colocar los nombres de los atributos que un objeto va a tener. Ejemplo: def __init__(self, marca, color): seguido de esto colocar lo valores que la respectiva "marca" y "color" tendrán. Cuando se jecute ese init se le va a pedir al usuario unas marca, un color y un parametro. 