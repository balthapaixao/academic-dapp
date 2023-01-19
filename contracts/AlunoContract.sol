// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

import "./AcademicTypes.sol";
import "./Academic.sol";
import "./IAlunoContract.sol";


contract AlunoContract is IAlunoContract{

    mapping(uint => Aluno) alunoById;

    address owner;
    address private _academicContractAddr;
    address private _disciplinaContractAddr;

    modifier onlyAdmin(){
       require(address(msg.sender) == address(owner), "Nao autorizado. Apenas o Admin pode realizar concluir essa operacao. Transacao revertida.");
       _;
    }

     modifier onlyAluno(uint256 id) {
        require(
            address(
                alunoById[id].aluno
            ) == address(msg.sender),
            "Apenas o proprio aluno pode realizar essa operacao. Transacao revertida"
        );
        _;
    }

    constructor(address academicContractAddr){
       _academicContractAddr = academicContractAddr;
       owner = msg.sender;
    }

    function getAlunoById(uint id) public view override returns (Aluno memory){
        return alunoById[id];
    }

    function inserirAluno(uint id, string memory nome, address alunoAddr) onlyAdmin public override {
       require(Academic(_academicContractAddr).etapa() == Periodo.INSCRICAO_ALUNOS_E_PROFESSORES, "Fora do periodo de inscricao de aluno/professores. Transacao revertida");
       require(id != 0, "Necessario um id de aluno");
       alunoById[id] = Aluno(id, nome, alunoAddr);
    }

    function inscreverDisciplina(uint alunoId, uint disciplinaId) onlyAluno(alunoId) public override{
      require(bytes(IDisciplinaContract(_disciplinaContractAddr).getDisciplinaById(disciplinaId).nome).length != 0, "Disciplina inexistente. Transacao revertida.");
      require(bytes(getAlunoById(alunoId).nome).length != 0, "Aluno nao existente. Transacao revertida.");
      IDisciplinaContract(_disciplinaContractAddr).pushAlunoToDisciplina(alunoId, disciplinaId);
    }
    
    function setDisciplinaContractAddress(address disciplinaContractAddr)
        public
        onlyAdmin
    {
        _disciplinaContractAddr = disciplinaContractAddr;
    }
}

