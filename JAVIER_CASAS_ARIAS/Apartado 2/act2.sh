  GNU nano 7.2                                             act2.sh
#!/bin/bash
#Identificar dirección MAC
mac=$(ip addr | awk '/ether/ {print $2}')

#Identificar sistema operativo
os=$(lsb_release -d | awk '{print $2,$3,$4}')

#Identificar nombre del equipo
equipo=$(hostname)

#Identificar nombre de usuario
user=$(whoami)

#Imprimir los datos en un mensaje único
echo "A continuación, se muestran datos del equipo:

La dirección MAC del equipos es: $mac
El sistema operativo del equipo es: $os
El nombre del equipo es: $equipo
El usuario con el que se ha ejecutado el script es: $user

"