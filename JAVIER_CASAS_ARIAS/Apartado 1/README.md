Apartado 1:

1. En el apartado número 1 se piden los siguientes puntos:
    1. Crear una aplicación sencilla en Python relacionada con la ciberseguridad (por ejemplo criptografía).
    2. Crear 4 tests unitarios para comprobar que la aplicación funciona correctamente.

El programa en Python que he creado, ha sido un cifrado César, ya que es uno de los métodos de criptografía más básica y antigua. Para este práctica, es cifrado César ha permitido comprender el funcionamiento de su cifrado y ejecutar una aplicación de forma sencilla.


2. El cifrado César consiste en reemplazar cada letra del alfabeto por otra letra que se encuentre más adelante según el número de posición que se le ha indicado.
Un simple ejemplo sería utilizar un desplazamiento de 3 posiciones. De esta forma, la conversión sería la siguiente:
A => D
E => H
C => F

En esta práctica se han creado 2 ficheros principales. El fichero program_cesar.py es el que contiene el programa escrito en el lenguaje de programación Python. El fichero test_program_cesar.py, es el test unitario que permite realizar una evaluación para comprobar que el programa funciona correctamente.




2.1: Código fuente (program_cesar.py)
En este programa se han creado 2 funciones principales. Una función cifra un mensaje, la otra función descifra el mensaje y también se ha creado un menú de interacción para que el usuario final ingrese el mensaje que desea cifrar.


Código fuente:
    #Programa de criptofrafía: Javier Casas

    #FUNCIÓN PARA CIFRAR MENSAJE
    def encriptar(texto, desplazamiento):       
        resultado = ""      #Cadena vacía donde se irán añadiendo caracteres cifrados
        for char in texto:
            if char.isalpha():      #Comprueba si la variable "char" es una letra del alfabeto
                base = ord('A') if char.isupper() else ord('a')         #Determina la base del mensaje, dependiendo de si la letra es mayúscula o minúscula
                nueva_posicion = (ord(char) - base + desplazamiento) % 26       #La variable "nueva_posición" será la nueva posición dentro del alfabeto
                resultado += chr(base + nueva_posicion)         #Convierte el cálculo de los números en carácteres
            else:
                resultado += char  #Si existen espación, números o signos de puntuación, los deja exactamente igual.
        return resultado            #Retorna el resultado

    #FUNCIÓN PARA DESCIFRAR MENSAJE
    def desencriptar(texto, desplazamiento):
        return encriptar(texto, -desplazamiento)        #Llama a la función "encriptar" con desplazamiento negativo, permitiendo revertir el proceso y obtener el mensaje original.


    #Comprobar que el erchivo se ejecute directamente desde python3
    if __name__ == "__main__":
        mensaje = input("Escribe el mensaje que será cifrado: ")     #Solicitarle al usuario que escriba un mensaje para cifrar
        clave = int(input("Introduce el desplazamiento (número): "))        #Solicitar que defina el número de desplazamiento

        #Cifra el mensaje teniendo en cuenta el desplazamiento y luego muestra el mensaje cifrado
        cifrado = encriptar(mensaje, clave)
        print("Mensaje cifrado:", cifrado)

        #Llama a la función "desencriptar" para descifrar el mensaje.
        descifrado = desencriptar(cifrado, clave)
        print("Mensaje descifrado:", descifrado)



EL código fuente presenta una serie de comentarios que explica el funcionamiento de sus líneas de código.
A continuación, se explican las funciones principales definidas en el código.

encriptar(texto, desplazamiento)
- Recorre cada letra del mensaje introducido por el usuario final.
- Si identifica que el caracter es una letra, la desplaza según el número de desplazamiento indicado.
- En caso de un espacio, signo o carácter especial, se dejará exactamente igual sin sufrir variaciones.

desencriptar(texto, desplazamiento)
- El objetivo de esta función es descifrar el mensaje cifrado con la función (encriptar).
- Su funcionamiento es inverso, para que esto suceda se le añade el signo negativo (-) antes la variable 
desplazamiento.

Menú principal (if __name__ == "__main__":):
- Le pide al usaurio que introduzca el mensaje que desea cifrar.
- Le solicita al usuario el número de desplazamiento deseado.
- Muestra por pantalla el mensaje cifrado y el mensaje descifrado.




2.2: Test unitario (test_program_cesar.py):
El test unitario ha sido creado con el objetivo de comprobar el funcionamiento del programa principal. Para esto, se han creado 4 comprobaciones diferentes que permite evaluar el comportamiento del código según los datos añadidos y las características del mensaje que será cifrado.

Cödigo del test unitario:
        #Test unitario: Javier Casas

        import program_cesar        #Importar programa creado
        import unittest             #Importart librearía estándar de python para realizar test unitarios

        class TestCesar(unittest.TestCase):     #Define la clase de test llamada TestCesar. Permite que unittest ejecute tests definidos en esta clase.

            def test_cifrado(self):
                self.assertEqual(program_cesar.encriptar("ABC", 3), "DEF")      #Cifrar "ABC" con desplazamiento 3 y el resultado debe ser "DEF"

            def test_descifrado(self):
                self.assertEqual(program_cesar.desencriptar("DEF", 3), "ABC")       #Descifra "DEF" con desplazamiento 3 y el resultado debe ser "ABC"

            def test_desplazamiento(self):        #Comprobar un desplazamiento superior a 26. 
                self.assertEqual(program_cesar.encriptar("Hola", 30), program_cesar.encriptar("Hola", 4))       #Se obtiene lo mismo en un desplaz 30 y 4. 30 % 26 = 4

            def test_simbolo(self):
                self.assertEqual(program_cesar.encriptar("Hola mundo!", 5), "Mtqf rzsit!")          #Comprobar como no varia el resultado al añadir un símbolo en el mensaje que será cifrado.

        if __name__ == "__main__":
            unittest.main()


A continuación, se explica el funcionamiento de cada test unitario:

1. def test_cifrado(self):
        self.assertEqual(program_cesar.encriptar("ABC", 3), "DEF") 
- Cifrar "ABC" con desplazamiento 3 y el resultado debe ser "DEF"

2. def test_descifrado(self):
        self.assertEqual(program_cesar.desencriptar("DEF", 3), "ABC")
- Descifra "DEF" con desplazamiento 3 y el resultado debe ser "ABC"

3. def test_desplazamiento(self):        
        self.assertEqual(program_cesar.encriptar("Hola", 30), program_cesar.encriptar("Hola", 4))
- Con este test se prueba que el resultado del cifrado no varía aunque se defina un desplazamiento superior a 26, ya que de esta manera sobre pasa el alfabeto. 
- En este caso se ha aplicado un desplazamiento 30 y se obtiene el mismo resultado que asignar un desplazamiento 4. Esto se debe a que en la función "encriptar" se definió la ecuación: 
(base_mansaje + desplazamiento) % 26  
En la actividad sería: 30 % 26 = 4

4. def test_simbolo(self):
        self.assertEqual(program_cesar.encriptar("Javier Casas!", 5), "Ofanjw Hfxfx!")
- Este test lo que hace es verificar como al aplicar un cifrado no eliminar los espacios y los símbolos, el resultado obtenido mantiene el espacio y el símbolo.