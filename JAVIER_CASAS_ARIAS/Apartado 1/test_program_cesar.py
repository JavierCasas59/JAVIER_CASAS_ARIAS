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
        self.assertEqual(program_cesar.encriptar("Javier Casas!", 5), "Ofanjw Hfxfx!")          #Comprobar como no varia el resultado al añadir un símbolo en el mensaje que será cifrado.

if __name__ == "__main__":
    unittest.main()























































