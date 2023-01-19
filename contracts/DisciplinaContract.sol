// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

import "./AcademicTypes.sol";
import "./Academic.sol";
import "./IDisciplinaContract.sol";
import "./ProfessorContract.sol";

contract DisciplinaContract is IDisciplinaContract {
    mapping(uint256 => Disciplina) disciplinaById;
    mapping(uint256 => uint256[]) public alunosByDisciplina;

    address public owner;

    address _academicContractAddr;
    address _alunoContractAddr;
    address _professorContractAddr;

    modifier onlyAdmin() {
        require(
            address(msg.sender) == address(owner),
            "Nao autorizado. Apenas o Admin pode realizar concluir essa operacao. Transacao revertida."
        );
        _;
    }

    constructor(address academicContractAddr) {
        _academicContractAddr = academicContractAddr;
        owner = msg.sender;
    }

    function getDisciplinaById(uint256 id)
        public
        view
        override
        returns (Disciplina memory)
    {
        return disciplinaById[id];
    }

    function inserirDisciplina(
        uint256 id,
        string memory nome,
        address professor,
        uint256 idProfessor
    ) public override onlyAdmin {
        require(
            Academic(_academicContractAddr).etapa() ==
                Periodo.INSCRICAO_ALUNOS_E_PROFESSORES,
            "Fora do periodo de inscricao de aluno"
        );
        require(
            bytes(
                IProfessorContract(_professorContractAddr)
                    .getProfessorById(idProfessor)
                    .nome
            ).length != 0,
            "Professor nao existente"
        );
        require(
            address(
                IProfessorContract(_professorContractAddr)
                    .getProfessorById(idProfessor)
                    .professorAddr
            ) == address(professor),
            "O endereco do professor vinculado ao id de professor fornecido nao bate. Transacao revertida"
        );

        disciplinaById[id] = Disciplina(id, nome, professor, idProfessor);
    }

    function pushAlunoToDisciplina(uint256 idAluno, uint256 idDisciplina)
        public
        override
    {
        require(
            bytes(IAlunoContract(_alunoContractAddr).getAlunoById(idAluno).nome)
                .length != 0,
            "Aluno nao existente!"
        );
        require(
            bytes(getDisciplinaById(idDisciplina).nome).length != 0,
            "Disciplina nao existente!"
        );
        alunosByDisciplina[idDisciplina].push(idAluno);
    }

    function getAlunosByDisciplina(uint256 idDisciplina)
        external
        view
        override
        returns (uint256[] memory)
    {
        return alunosByDisciplina[idDisciplina];
    }

    function setAlunoContractAddress(address alunoContractAddr)
        public
        onlyAdmin
    {
        _alunoContractAddr = alunoContractAddr;
    }

    function setProfessorContractAddress(address professorContractAddr)
        public
        onlyAdmin
    {
        _professorContractAddr = professorContractAddr;
    }
}
