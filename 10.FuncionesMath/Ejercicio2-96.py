#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%

def total():
    monto = float(input('Ingresa el valor del producto que estás pagando: '))
    iva = int(input('Ingresa la cantidad de IVA a aplicar: '))

    if iva != 0:
        if iva > 0:
            totalPagar = ((monto * iva)/ 100) + monto
            return(totalPagar)
        else:
            return('El monto de IVA es negativo. No podemos avanzar')
    else:
        totalPagar = (monto * .21) + monto
        return(totalPagar)
print('El total de su monto es:', total())

