from web3 import Web3: This line imports the Web3 library, which is used to interact with the Ethereum blockchain.
w3 = Web3(Web3.HTTPProvider("http://localhost:8545")): This line creates an instance of the Web3 library, connecting to an Ethereum node running on the local machine at port 8545. This is the default port for a Geth node running in a dev environment.
sender_address = w3.eth.accounts[0]: This line sets the first account in the connected Ethereum node as the sender of transactions.
academic_contract_address = ...: This line sets the address of the deployed "Academic" contract on the Ethereum blockchain.
academic_contract = w3.eth.contract(address=academic_contract_address, abi=...): This line creates an instance of the "Academic" contract using its address and ABI (Application Binary Interface).
aluno_contract_address = ...: This line sets the address of the deployed "Aluno" contract on the Ethereum blockchain.
aluno_contract = w3.eth.contract(address=aluno_contract_address, abi=...): This line creates an instance of the "Aluno" contract using its address and ABI.
disciplina_contract_address = ...: This line sets the address of the deployed "Disciplina" contract on the Ethereum blockchain.
disciplina_contract = w3.eth.contract(address=disciplina_contract_address, abi=...): This line creates an instance of the "Disciplina" contract using its address and ABI.
professor_contract_address = ...: This line sets the address of the deployed "Professor" contract on the Ethereum blockchain.
professor_contract = w3.eth.contract(address=professor_contract_address, abi=...): This line creates an instance of the "Professor" contract using its address and ABI.
tx_hash = academic_contract.functions.deploy().transact({'from': sender_address}): This line sends a transaction to deploy the "Academic" contract on the Ethereum blockchain.
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash): This line waits for the deployment of the "Academic" contract to be confirmed on the Ethereum blockchain and returns a receipt of the transaction.
tx_hash = aluno_contract.functions.deploy(academic_contract_address).transact({'from': sender_address}): This line sends a transaction to deploy the "Aluno" contract on the Ethereum blockchain and passing the address of the deployed "Academic" contract.
tx_hash = disciplina_contract.functions.deploy(academic_contract_address).transact({'from': sender_address}): This line sends a transaction to deploy the "Disciplina" contract on the Ethereum blockchain and passing the address of the deployed "Academic" contract.
tx_hash = professor_contract.functions.deploy(academic_contract_address).transact({'from': sender_address}): This line sends a transaction to deploy the "Professor" contract on the Ethereum blockchain and passing the address
