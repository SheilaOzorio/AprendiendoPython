'''En el siguiente diccionario se encuentran capitales de los países
en el mundo, debes realizar un programa que pida un país al usuario, y
muestre la capital de ese país, en dado caso que el país no este en el diccionario, sebe
mostrar un msj diciendo 'País no encontrado'''
'''{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras",
"Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", 
"Argentina": "Buenos Aires", "Colombia": "Bogota", 
"Venezuela": "Caracas", "España": "Madrid"}'''

diccionario = {'Guatemala' : 'Ciudad de Guatemala', 'El salvador' : 'San Salvador','Colombia' : 'Bogota' ,  'Honduras' : 'Honduras,', 'México' : 'CDMX', 'Italia' : 'Roma' }

pais = input('Ingresa un país para conocer su capital: ')
letra = pais.capitalize() in diccionario
# in es un metodo que se asegura que un elemento esté dentro de otro

if letra == True: 
    print(diccionario[pais.capitalize()])
else: 
    print('El país no se encuentra en el diccionario')

