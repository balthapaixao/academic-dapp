from web3 import Web3
from .utils import abis

def main() -> None:
    w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

    # Connect to the Academic contract
    academic_contract_address = w3.eth.accounts[0]
    academic_contract = w3.eth.contract(address=academic_contract_address, abi=abis.academic_contract_abi)

    # Connect to the Aluno contract
    aluno_contract_address = w3.eth.accounts[1]
    aluno_contract = w3.eth.contract(address=aluno_contract_address, abi=abis.aluno_contract_abi)

    # Connect to the Disciplina contract
    disciplina_contract_address = w3.eth.accounts[2]
    disciplina_contract = w3.eth.contract(address=disciplina_contract_address, abi=abis.disciplina_contract_abi)

    # Connect to the Professor contract
    professor_contract_address = w3.eth.accounts[3]
    professor_contract = w3.eth.contract(address=professor_contract_address, abi=abis.professor_contract_abi)


    print(f"Contratos deployados:\nAcademic -> {academic_contract_address},\nAluno -> {aluno_contract_address},\nDisciplina -> {disciplina_contract_address},\nProfessor -> {professor_contract_address}")

    # Set the addresses of the Aluno and Disciplina contracts in the Professor contract
    hash_aluno_disc  = professor_contract.functions.setAlunoContractAddress(aluno_contract_address).transact({'from': aluno_contract_address})
    receipt_aluno_disc = w3.eth.waitForTransactionReceipt(hash_aluno_disc)
    print(f"HASH: {hash_aluno_disc}")
    print(f"RECEIPT: {receipt_aluno_disc}")


    hash_disc_prof = disciplina_contract.functions.setProfessorContractAddress(professor_contract_address).transact({'from': professor_contract_address})
    receipt_disc_prof = w3.eth.waitForTransactionReceipt(hash_disc_prof)
    print(f"HASH: {hash_disc_prof}")
    print(f"RECEIPT: {receipt_disc_prof}")

    hash_disc_aluno = disciplina_contract.functions.setAlunoContractAddress(aluno_contract_address).transact({'from': aluno_contract_address})
    receipt_disc_aluno = w3.eth.waitForTransactionReceipt(hash_disc_aluno)
    print(f"HASH: {hash_disc_aluno}")
    print(f"RECEIPT: {receipt_disc_aluno}")

main()