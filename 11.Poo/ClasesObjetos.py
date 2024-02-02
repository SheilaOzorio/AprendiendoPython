#La forma de crear clases es por medio de palabras reservadas y sintaxis.
#Se recomienda que en las 'clases', pongamos la primera letra en mayúsculas, esto para que podamos reconocerla después como una clase

#Digamos que el class es como nuestro molde, o la casita que tiene cosas y nosotros somos los que le ponemos esas cosas (que en programación es Objetos), podemos ponerle tantos como sea necesarias
class CasaMelendezOzorio():
    pass
print(type(CasaMelendezOzorio))

celular = CasaMelendezOzorio()
print(type(CasaMelendezOzorio))

#Si le asiganamos objetos a nuestro <class> (casaMelendezOzorio), y quereamos saber qué tipo de dato es con <type>, ahora saldrá que es un dato 'main CasaMelendezOzorio'

def CasaMelendezOzorio():
    pass
print(type(CasaMelendezOzorio))

#Aquí vemos que aunque tengan el mismo nombre, un class y un def pueden ser distintos y no habría como tal un problema. aunque sería preferente no hacerlo ya que aunque no aparezca un error, el programa sí entra en 'conflicto'
