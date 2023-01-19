// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

import "./AcademicTypes.sol";

interface IAlunoContract{

    function inserirAluno(uint id, string memory nome, address aluno) external;
    
    function getAlunoById(uint id) external view returns (Aluno memory);

    function inscreverDisciplina(uint alunoId, uint idDisciplina) external;
}
