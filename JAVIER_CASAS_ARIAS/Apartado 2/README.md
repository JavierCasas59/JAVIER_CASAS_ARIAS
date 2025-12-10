Apartado 2

1. En esta actividad, se nos pide crear un script en Bash que sea capaz de obtener cierta información del equipo donde se ejecuta y luego la muestre por pantalla en un mensaje único.

La información que se debe mostrar a través del script es la siguiente:
- Dirección MAC del equipo donde se ejecuta el script.
- Sistema operativo del equipo donde se ejecuta el script.
- El nombre del equipo.
- El usuario que ejecuta el script.

2. El script creado presenta el siguiente contenido.

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

A continuación, se muestra la explicación técnica del script creado en Bash
2.1: mac=$(ip addr | awk '/ether/ {print $2}')
- Se crea la variable "mac". El contenido de esta variable es identificar la dirección MAC de equipo, localizando la línea 'ether' y luego muestra la segunda columna que corresponde a la dirección MAC.

2.2: os=$(lsb_release -d | awk '{print $2,$3,$4}')
- Se crea la variable "os". Extrae la descripción del sistema especificando las columnas 2, 3 y 4.

2.3: equipo=$(hostname)
- Se crea la variable "equipo". Haciendo uso de 'hostname', se obtiene el nombre del equipo donde se ha ejecutado el script.

2.4: user=$(whoami)
- Se crea la variable "user". Con el comando 'whoami' se obtiene el nombre del usuario con el que se ha ejecutado el script.

2.5: echo "A continuación, se muestran datos del equipo:

        La dirección MAC del equipos es: $mac
        El sistema operativo del equipo es: $os
        El nombre del equipo es: $equipo
        El usuario con el que se ha ejecutado el script es: $user

        "
- Es un mensaje único donde se muestra por pantalla al usuario los resultados obtenidos.


3. Para ejecutar el script y realizar una interacción con el, se necesita realizar los siguientes pasos:

3.1: Primero será necesario asignarle permisos de ejecución al script para que el usuario pueda ejecutarlo. Estos permisos se asignan con privilegio administrador "root".
sudo chmod +x act2.sh

3.2: Para ejecutar el script desde la terminal, será necesario realizarlo de la siguiente manera:
- ./act2.sh

3.3: Un ejemplo del resultado obtenido es el siguiente:
        A continuación, se muestran datos del equipo:

        La dirección MAC del equipos es: 00:15:5d:e7:8d:a9
        El sistema operativo del equipo es: Ubuntu 24.04.3 LTS
        El nombre del equipo es: PC-JAVI
        El usuario con el que se ha ejecutado el script es: casas