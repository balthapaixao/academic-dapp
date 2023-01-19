// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;


struct Aluno{
    uint id;
    string nome;
    address aluno;
}

struct Disciplina{
    uint id;
    string nome;
    address professor;
    uint idProfessor;
}

struct Professor{
    uint id;
    string nome;
    address professorAddr;
}

enum Periodo {
    INSCRICAO_ALUNOS_E_PROFESSORES,
    LANCAMENTO_NOTAS,
    FIM_PERIODO
}


