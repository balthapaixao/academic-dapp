// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

import "./IProfessorContract.sol";
import "./IAlunoContract.sol";
import "./IDisciplinaContract.sol";
import "./AcademicTypes.sol";
import "./Academic.sol";

// import "hardhat/console.sol";

contract ProfessorContract is IProfessorContract {
    mapping(uint256 => Professor) professorById;
    mapping(uint256 => mapping(uint256 => uint8)) alunoIdToDisciplinaIdToNota;
    mapping(uint256 => Disciplina) disciplinaById;

    address public owner;

    address private _academicContractAddr;
    address private _alunoContractAddr;
    address private _disciplinaContractAddr;

    modifier onlyAdmin() {
        require(
            address(msg.sender) == address(owner),
            "Apenas o admin pode realizar essa operacao. Transacao revertida"
        );
        _;
    }

    modifier onlyProfessor(uint256 disciplinaId) {
        require(
            address(
                IDisciplinaContract(_disciplinaContractAddr)
                    .getDisciplinaById(disciplinaId)
                    .professor
            ) == address(msg.sender),
            "Apenas o professor da disciplina pode realizar essa operacao. Transacao revertida"
        );
        _;
    }

    constructor(address academicContractAddr) {
        _academicContractAddr = academicContractAddr;
        owner = msg.sender;
    }

    function inserirProfessor(
        uint256 id,
        string memory nome,
        address professorAddress
    ) public override onlyAdmin {
        require(
            Academic(_academicContractAddr).etapa() ==
                Periodo.INSCRICAO_ALUNOS_E_PROFESSORES,
            "Fora do periodo de inscricao de alunos/professores!"
        );
        professorById[id] = Professor(id, nome, professorAddress);
    }

    function getProfessorById(uint256 id)
        public
        view
        override
        returns (Professor memory)
    {
        return professorById[id];
    }

    function inserirNota(
        uint256 alunoId,
        uint256 disciplinaId,
        uint8 nota
    ) public override onlyProfessor(disciplinaId) {
        require(
            bytes(IAlunoContract(_alunoContractAddr).getAlunoById(alunoId).nome)
                .length != 0,
            "Aluno nao existente!"
        );
        require(
            Academic(_academicContractAddr).etapa() == Periodo.LANCAMENTO_NOTAS,
            "Fora do periodo de lancamento de notas!"
        );

        alunoIdToDisciplinaIdToNota[alunoId][disciplinaId] = nota;
    }

    function listarNotasDisciplina(uint256 disciplinaId)
        public
        view
        override
        onlyProfessor(disciplinaId)
        returns (Aluno[] memory, uint8[] memory)
    {
        uint256 numAlunos = IDisciplinaContract(_disciplinaContractAddr)
            .getAlunosByDisciplina(disciplinaId)
            .length;

        Aluno[] memory alunos = new Aluno[](numAlunos);
        uint8[] memory notas = new uint8[](numAlunos);

        for (uint256 i = 0; i < numAlunos; i++) {
            uint256 alunoId = IDisciplinaContract(_disciplinaContractAddr)
                .getAlunosByDisciplina(disciplinaId)[i];

            alunos[i] = IAlunoContract(_alunoContractAddr).getAlunoById(
                alunoId
            );
            notas[i] = alunoIdToDisciplinaIdToNota[alunoId][disciplinaId];
        }
        return (alunos, notas);
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
}
