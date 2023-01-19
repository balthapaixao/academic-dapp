// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

import "./AcademicTypes.sol";

interface IProfessorContract{

    function inserirProfessor(uint id, string memory nome, address professorAddress) external;

    function getProfessorById(uint id) external view returns (Professor memory);

    function listarNotasDisciplina(uint disciplinaId) external view returns(Aluno[] memory, uint8[] memory);

    function inserirNota(uint alunoId, uint disciplinaId, uint8 nota) external;

}