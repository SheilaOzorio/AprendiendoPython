'''Debo crear un programa que pida al usuario una letra y si es vocal, muestre el 
mensaje "Es vocal" si no decirle al usuario que no es vocal'''

#usuamos 'input' cuando querenos que haya entra de datos


letra = input('Ingresa una letra: ')
if letra.lower() == 'a':
    print('Esta es una vocal')
elif letra.lower() == 'e':
    print('Esta es una vocal')
elif letra.lower() == 'i':
    print('Esta es una vocal')
elif letra.lower() == 'o':
    print('Esta es una vocal')
elif letra.lower() == 'u':
    print('Esta es una vocal')
else:
    print('Esta NO es una vocal')

#Aqui estamos reduciendo el codigo, ya que se esta realizando exactamente lo mimso pero sin tanto codigo.
# in nos sirve para sintetizar.

if letra.lower() in 'aeiou':
    print('Es una vocal')
else:
    print('Esta NO es una vocal')

