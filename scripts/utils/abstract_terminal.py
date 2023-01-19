from brownie.project import *
from web3 import Web3
from utils import abis
#import contextlib
import numpy as np
from .setup.config import get_project
w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
#@contextmanager
def deploy_contracts():
    
    accounts = w3.eth.accounts
    #print(accounts)
    # Connect to the Academic contract
    academic_contract_address = accounts[0]
    academic_contract = w3.eth.contract(address=academic_contract_address, abi=abis.academic_contract_abi)

    # Connect to the Aluno contract
    aluno_contract_address = w3.eth.accounts[1]
    aluno_contract = w3.eth.contract(address=aluno_contract_address, abi=abis.aluno_contract_abi)

    # Connect to the Disciplina contract
    disciplina_contract_address = accounts[2]
    disciplina_contract = w3.eth.contract(address=disciplina_contract_address, abi=abis.disciplina_contract_abi)

    # Connect to the Professor contract
    professor_contract_address = accounts[3]
    professor_contract = w3.eth.contract(address=professor_contract_address, abi=abis.professor_contract_abi)

    return academic_contract, aluno_contract, disciplina_contract, professor_contract

academic_contract, aluno_contract, disciplina_contract, professor_contract = deploy_contracts()

# print(professor_contract.functions.inserirNota().call())

def emitir_pgto():
    with get_project() as myproject:
        pgto_token = myproject.AcademicToken.\
                     deploy({"from":aluno_contract.address,
                             "to":  academic_contract.address})#brownie.accounts[0]})
        #print(f"Sent from {aluno_contract_address} to {academic_contract_address}")
        return pgto_token


def emitir_certificado():
    with get_project() as myproject:
        certificado_token = myproject.AcademicCertificate.\
                            deploy({"from":academic_contract.address,
                                    "to":aluno_contract.address})

        return certificado_token


def cadastrar_disciplina(aluno_name, disciplina_name):
    aluno_id = int(hash(aluno_name))
    disciplina_id = int(hash(disciplina_name))
    print()
    print()
    print(type(aluno_id), 
          type(disciplina_id))

    hash_disciplina = aluno_contract.functions.\
                       setDisciplinaContractAddress(disciplina_contract.address).call()
    receipt_disciplina = w3.eth.wait_for_transaction_receipt(hash_disciplina)
    disciplina_token = aluno_contract.functions.\
                       inscreverDisciplina(aluno_id, disciplina_id).call()


    if disciplina_token:
        print(disciplina_token )
        print(f"Disciplina {disciplina_name} cadastrada com sucesso")



def lancar_nota(aluno_name, disciplina_name, nota):
    aluno_id = int(hash(aluno_name))
    disciplina_id = int(hash(disciplina_name))
    nota = int(nota)
    print()
    print()
    #print(type(aluno_id), type(disciplina_id), type(nota))
    #nota_hash = professor_contract.functions.inserirNota(aluno_id, disciplina_id, nota).transact()
    #nota_receipt = w3.eth.waitForTransactionReceipt(nota_hash)
    nota_token = professor_contract.functions.\
                 inserirNota(aluno_id, disciplina_id, nota).call()
        
    print(professor_contract.functions.inserirNota().call())
    print(nota_token)
    if nota_token:
        print(f"Nota {nota } lançada para o aluno {aluno_name} na disciplina {disciplina_name}")
    return nota_token





# def cadastrar_disciplina(disciplina_name):
#     disciplina_id = hash(disciplina_name)
#     with get_project() as myproject:
#         disciplina_token = myproject.AlunoContract.\
#                            deploy(disciplina_contract.address,
#                                   {"from":disciplina_contract.address,
#                                    "to":academic_contract.address})
#         if disciplina_token:
#             print(disciplina_token )
#             print(f"Disciplina {disciplina_name} cadastrada com sucesso")



def inscrever_aluno(aluno_name, disciplina_name):
    ...
#     aluno_id = hash(aluno_name)
#     disciplina_id = hash(disciplina_name)
#     with get_project() as myproject:
#         aluno_token = myproject.AlunoContract.\
#                       deploy(#"alunoId":aluno_id,
#                               #"disciplinaId":disciplina_id,
#                              # "from":aluno_contract_address,
#                               #"to":academic_contract_address})

#                        aluno_contract_address,
#                     #    academic_contract_address,
#                        {"from":aluno_contract_address})

#         if aluno_token:
#             print(f"Aluno {aluno_name} inscrito na disciplina {disciplina_name}")

#         return aluno_token 



# def deploy_contracts2():
#     w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
#     accounts = w3.eth.accounts
#     #print(accounts)
#     w3.eth.default_account = w3.eth.accounts[0]

#     academic_contract = w3.eth.contract(abi=abis.academic_contract_abi)
#     aluno_contract = w3.eth.contract(abi=abis.aluno_contract_abi)
    
#     disciplina_contract = w3.eth.contract(abi=abis.disciplina_contract_abi)
#     professor_contract = w3.eth.contract(abi=abis.professor_contract_abi)
    
#     hash_aluno  = professor_contract.functions.constructor().transact()
#     receipt_aluno = w3.eth.wait_for_transaction_receipt(hash_aluno)
#     aluno = w3.eth.contract(address=receipt_aluno.contractAddress,
#                             abi=abis.aluno_contract_abi)
#     hash_disc = disciplina_contract.functions.constructor().transact()
#     receipt_disc = w3.eth.wait_for_transaction_receipt(hash_disc)
#     prof = w3.eth.contract(address=receipt_disc.contractAddress,
#                             abi=abis.disciplina_contract_abi)

    
#     return aluno, prof


# academic_contract, aluno_contract, disciplina_contract, professor_contract = deploy_contracts2()
