'''Break y continue, nos sirve para detener una iteracion o para saltarnos una
iteracion, break:   es como descanso o deternerse'''
'''Si queremos interrumpir nuestro bucle y que termine antes de haber completado la condicion
si es del 1 al 10 por ejemplo y queremos que termine hasta el 5, ahí es donde entra el "BREAK",
por lo general break se convina con IF, vease el ejemplo'''

for i in range(1, 10):
 #   print(i)
   # if i == 5:
    #    break

    if i == 6:
        continue
    print(i)
'''Continue nos permite omitir algún valor, en este ejemplo en cuanto
llegue a 6, omitirá ese valor y continuará desde el el 7, es decir 1,2,4,5,7 '''
