// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

import "./AcademicTypes.sol";
import "./IAlunoContract.sol";
import "./IDisciplinaContract.sol";

// import "hardhat/console.sol";

/**
 * @title Academic
 * @dev Academic system contract
 */
contract Academic {
    Periodo public etapa;

    address public owner;
    address _alunoContractAddr;
    address _disciplinaContractAddr;
    address _professorContractAddr;

    constructor() {
        etapa = Periodo.INSCRICAO_ALUNOS_E_PROFESSORES;
        owner = msg.sender;
    }

    modifier onlyAdmin() {
        require(
            address(msg.sender) == address(owner),
            "Somente o admin pode concluir essa operacao. Transacao revertida."
        );
        _;
    }

    function setAlunoContractAddress(address alunoContractAddr)
        public
        onlyAdmin
    {
        _alunoContractAddr = alunoContractAddr;
    }

    function setDisciplinaContractAddress(address disciplinaContractAddr)
        public
        onlyAdmin
    {
        _disciplinaContractAddr = disciplinaContractAddr;
    }

    function setProfessorContractAddress(address professorContractAddr)
        public
        onlyAdmin
    {
        _professorContractAddr = professorContractAddr;
    }

    function abrirLancamentoNota() public onlyAdmin {
        etapa = Periodo.LANCAMENTO_NOTAS;
    }

    function fecharPeriodo() public onlyAdmin {
        etapa = Periodo.FIM_PERIODO;
    }

    function abrirInscricoes() public onlyAdmin {
        etapa = Periodo.INSCRICAO_ALUNOS_E_PROFESSORES;
    }
}
