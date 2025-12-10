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
