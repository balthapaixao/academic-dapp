// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

import "./AcademicTypes.sol";

interface IDisciplinaContract{

    function inserirDisciplina(uint id, string memory nome, address professor, uint idProfessor) external;

    function getDisciplinaById(uint id) external view returns (Disciplina memory);

    function getAlunosByDisciplina(uint idDisciplina) external view returns (uint256[] memory);

    function pushAlunoToDisciplina(uint idAluno, uint idDisciplina) external;
}
