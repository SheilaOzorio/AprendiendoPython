#Cuando tenemos más de dos clases podemos recurrir a la herencia, ya sea a la simple o una herencia Multiple que es la que se muestra aquí.

class A():
    def primera(self):
        return "Esta es la clase A"
class B():
    def segunda():
        return "Esta es la clase B"
class C( A , B):  #Aquí estamos haciendo nuestra herencia "multiple", es decir que estamos agregando dos clases en una, que serían la clase A y B en la clase C, esto vuelve a la clase C en "hija" de A y B por así decirlo. jiji. Por lo tanto nuestros dos metodos ("primera", y "segunda") ahora ya son parte de la clase C.
    pass

c = C()
print(c.primera())
print(c.segunda())