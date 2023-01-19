#https://remix.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.8.7+commit.e28d00a7.js

academic_contract_abi = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "abrirInscricoes",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "abrirLancamentoNota",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "etapa",
		"outputs": [
			{
				"internalType": "enum Periodo",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "fecharPeriodo",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "alunoContractAddr",
				"type": "address"
			}
		],
		"name": "setAlunoContractAddress",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "disciplinaContractAddr",
				"type": "address"
			}
		],
		"name": "setDisciplinaContractAddress",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "professorContractAddr",
				"type": "address"
			}
		],
		"name": "setProfessorContractAddress",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]


aluno_contract_abi = [
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "academicContractAddr",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			}
		],
		"name": "getAlunoById",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "nome",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "aluno",
						"type": "address"
					}
				],
				"internalType": "struct Aluno",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "alunoId",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "disciplinaId",
				"type": "uint256"
			}
		],
		"name": "inscreverDisciplina",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "nome",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "alunoAddr",
				"type": "address"
			}
		],
		"name": "inserirAluno",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "disciplinaContractAddr",
				"type": "address"
			}
		],
		"name": "setDisciplinaContractAddress",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]

disciplina_contract_abi = [
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "academicContractAddr",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "alunosByDisciplina",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "idDisciplina",
				"type": "uint256"
			}
		],
		"name": "getAlunosByDisciplina",
		"outputs": [
			{
				"internalType": "uint256[]",
				"name": "",
				"type": "uint256[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			}
		],
		"name": "getDisciplinaById",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "nome",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "professor",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "idProfessor",
						"type": "uint256"
					}
				],
				"internalType": "struct Disciplina",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "nome",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "professor",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "idProfessor",
				"type": "uint256"
			}
		],
		"name": "inserirDisciplina",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "idAluno",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "idDisciplina",
				"type": "uint256"
			}
		],
		"name": "pushAlunoToDisciplina",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "alunoContractAddr",
				"type": "address"
			}
		],
		"name": "setAlunoContractAddress",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "professorContractAddr",
				"type": "address"
			}
		],
		"name": "setProfessorContractAddress",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]

professor_contract_abi = [
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "academicContractAddr",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			}
		],
		"name": "getProfessorById",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "nome",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "professorAddr",
						"type": "address"
					}
				],
				"internalType": "struct Professor",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "alunoId",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "disciplinaId",
				"type": "uint256"
			},
			{
				"internalType": "uint8",
				"name": "nota",
				"type": "uint8"
			}
		],
		"name": "inserirNota",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "nome",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "professorAddress",
				"type": "address"
			}
		],
		"name": "inserirProfessor",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "disciplinaId",
				"type": "uint256"
			}
		],
		"name": "listarNotasDisciplina",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "nome",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "aluno",
						"type": "address"
					}
				],
				"internalType": "struct Aluno[]",
				"name": "",
				"type": "tuple[]"
			},
			{
				"internalType": "uint8[]",
				"name": "",
				"type": "uint8[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "alunoContractAddr",
				"type": "address"
			}
		],
		"name": "setAlunoContractAddress",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "disciplinaContractAddr",
				"type": "address"
			}
		],
		"name": "setDisciplinaContractAddress",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]