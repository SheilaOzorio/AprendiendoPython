'''class FabricaTelefonos():
    marca = 'Samsumg'

    def ElaborarHuawei(self):
        self.marca = 'Huawei'
telefono = FabricaTelefonos()
telefono.ElaborarHuawei()
print(telefono.marca)'''

#self sirve para englobar un atributo a toda una clase, es decir que si quiero mandar a llamar a algún atributo desde fuera del metodo, self antes de nuestro atributo nos será útil para lograrlo. NOTA: Debemos haber llamado a nuestra función en la cual se encuentra el atributo que queremos que se imprima; de esta forma primero accedemos al metodo. Ejemplo:  telefono.ElaborarHuawei() - self.marca = 'Huawei'

class CasitaMelendezOzorio():
    def __init__(self):
        print('Estoy ejecutando un metodo INIT, porque se ha creado un nuevo objeto')
Cama  = CasitaMelendezOzorio()

#El metodo INIT  nos va a servir para ser el constructor de una clase, que es el primer metodo que se ejecuta al crearse un obejeto. En vez de crear nuestros atributos podemos utilizar el metodo INIT para iniciar esto. Funcionará siempre y cuando tenga al menos un objeto. que por cierto nada más necesitaremos un objeto para que se ejecute.
#El init nos ahorra colocar los atribus, crear el objeto. colocarle los atributos al obhjeto y luego mandar a llamar a los atributos.
# init se le puede llamar ta,bién como 'metodo constructor'



