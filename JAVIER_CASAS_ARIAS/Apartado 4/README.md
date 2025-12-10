Apartado 4

1. En esta actividad he desarrollado un contrato inteligente en Solidity relacionado con el funcionamiento de un árbol de Merkle. El objetivo principal del programa creado es el siguiente:

- Comprender que es un árbol Merkle y como se utiliza para verificar datos de manera eficiente.
- Crear un contrato que almacene y actualice la raíz Merkle.
- Mediante un modificado de acceso, se crean mecanismos de seguridad.
- Poner en práctica los las habilidades aprendidas de Solidity en la plataforma CryptoZombies.



2. A continuación, se muestra el código fuente del contrato creado:

        // Contrato Merkle: Javier Casas
        pragma solidity >=0.5.0 <0.6.0;         // Declara versión del compilador de Solidity utilizado.

        contract InicioMerkle {              // Declarar el contrato MerkleStart

            address public propietario;     // definir propietario del contrato
            bytes32 public merkleRaiz;     // almacena la raíz Merkle actual

            constructor(bytes32 inicioRaiz) public {
                propietario = msg.sender;        // el propietario es quien despliega el contrato
                merkleRaiz = inicioRaiz;        // Se guarda el parámetro "inicioRaiz" en "merkleRaiz". 
            }

            // Solo el propietario puede modificar la raíz
            modifier soloPropietario() {
                require(msg.sender == propietario, "No estás identificado como propietario");
                _;  // Es un modificador que marca donde se ejecutará el cuerpo de la función
            }

            // Actualizar la raíz Merkle con una nueva
            function actualizarRaiz(bytes32 nuevaRaiz) public soloPropietario {
                merkleRaiz = nuevaRaiz;     // Actualiza la variable de estado con el nuevo valor. NOTA: Esta operación requiere una transacción y consumo de gas
            }
        }




3. Ahora se irá explicando el contrato creado, destacando las partes del código más significativas.

3.1: contract InicioMerkle {...}
- Con este comando se crea el contrato llamado InicioMerkle. Todo el código que se encuentra dentro de {...} pertenece a este contrato

3.2: Las principales variables del contrato son:
- propietario: Esta variable guarda la dirección que despliega el contrato y define el propietario del mismo. 
- merkleRaiz: Almacena la raíz Merkle actual.

3.3: constructor(bytes32 inicioRaiz) public {
- Esta es una función especial que se ejecuta una sola vez cuando se despliega el contrato.
- Se define un parámetro 'inicioRaiz' de tipo bytes32, el cual se utilizará para inicializar el contrato 'InicioMerkle'.
- Es obligatorio que en los constructores se declare la visibilidad como pública 'public'

3.4: propietario = msg.sender;
- Esto indica que el propietario es quien despliega el contrato.
- msg.sender: es la dirección que despliega el contrato.
- propietario: esta es la única cuenta que tiene permisos para actualizar la raíz.

3.5: modifier soloPropietario() {
        require(msg.sender == propietario, "No estás identificado como propietario");
        _;  
    }
- modifier soloPropietario: Declara un modificador llamado soloPropietario. Los modificadores son trozos de código reutilizables que se colocan en la firma de una función para ejecutar primero la comprobación y luego la función.
- require(msg.sender == propietario, "No estás identificado como propietario"); : Se verifica una condición y en caso de ser el resultado falso 'false', se revierte la transacción y se muestra el mensaje "No estás identificado como propietario".

3.6: function actualizarRaiz(bytes32 nuevaRaiz) public soloPropietario {
        merkleRaiz = nuevaRaiz;     
    }
- Permite cambiar la raíz Merkle almacenada. Al ser una operación que modifica el estado, requiere una transacción y por tanto gasto de gas.
- merkleRaiz = nuevaRaiz: Actualiza la variable de estado 'merkleRaiz' con el nuevo valor.




4. Se adjunta la imagen 'SOLIDITY.png' donde se muestra la realización de todas las actividades de Solidity en la plataforma CryptoZombies.