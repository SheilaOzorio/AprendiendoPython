'''elif es cuando nosotros queremos destinar varias condiciones y a partir dre la 
condición determinar que es lo que se va a ejecutar'''
'''Un condicional anidado es aquel que v a estar dentro de otro condicional, esto nos sirve para hacer una validacion siempre y cuando lleve una secuencia logica'''

#En el sig ejemplo se va evaluar si el nombre es Juan y si Juan ya tiene la mayoria de edad, se usara entonces los condicionales anidados ya que hay dos condidiciones.

nombre = 'juan'
edad = 18

if nombre == 'Juan':
    if edad >= 18:
        print('Eres Juan y eres mayor de edad')
    else: 
        print('Eres Juan pero NO eres mayor de edad')
else:
    print('Tu No eres Juan')

    
