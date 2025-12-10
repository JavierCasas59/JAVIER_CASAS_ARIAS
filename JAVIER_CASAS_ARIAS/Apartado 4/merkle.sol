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
