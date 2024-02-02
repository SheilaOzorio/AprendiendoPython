#Siempre agregar el while al pricipio para el bucle
#except ZeroDivisionError esto en caso de que haya un error cuando se realice una división, ejemplo que el usuario coloque el 0, ningún número se puede dividir en 0 aparecerá la  nota que pongas después del print. 
# except valueError: también se puede utilizar cuando hay un dato mal, seguido de esto colocamos el print junto que el mensaje de error y aparecerá cuando algo que se agregue no esté bien. 
# except kayboardInterrrupt: seguido de print y '\n'(esta \n sólo para un salto de línea)y le agregamos la nota de error. 
#Siempre debemos también de usar el break para que el bucle no sea eterno. La sintaxis es así.

while True:
    try:
        edad = int(input('Agrega tu edad: '))
        print('Tu edad es: ', edad)
        break
    except ValueError:
        print('Los datos ingresados son incorrectos')


