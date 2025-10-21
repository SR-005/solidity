import json
import os
from dotenv import load_dotenv
from solcx import compile_standard,install_solc
from web3 import Web3
install_solc("0.8.17")

load_dotenv()
MYADDRESS = Web3.to_checksum_address(os.getenv("MYADDRESS"))
SECRETCODE = os.getenv("SECRETKEY")

#Read the Smart Contract
with open("./simple-storage.sol","r") as file:
    simplestoragefile=file.read()

#complie the smart contract - default lines
compiledsol = compile_standard(
    {
        "language":"Solidity",
        "sources":{"simple-storage.sol":{"content":simplestoragefile}},
        "settings":{
            "outputSelection":  {
                "*":{"*": ["abi","metadata","evm.bytecode","evm.sourceMap"]}
            }
        }
    },solc_version="0.8.17"
)

#move the compiled code into a new file 'compiledcode.json'
with open("compiledcode.json","w") as file:
    json.dump(compiledsol,file)

#fetching bytecode from the compiled Smart Contract
bytecode=compiledsol["contracts"]["simple-storage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

#get abi from the compiled Smart Contract
abi=compiledsol["contracts"]["simple-storage.sol"]["SimpleStorage"]["abi"]

#connecting to Ganache Blockchain
w3=Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chainid=1337

#creating the contract
SimpleStorage=w3.eth.contract(abi=abi,bytecode=bytecode)
print("Contract Created")

#fetching nonce(latest transaction) of our wallet
nonce=w3.eth.get_transaction_count(MYADDRESS)

#To make a transcation you need to: 
    # 1. Build a Transaction 
    # 2. Sign a Transaction
    # 3. Send a Transaction 
#Building a Transaction 
transaction = SimpleStorage.constructor().build_transaction({
    "chainId": chainid,
    "from": MYADDRESS,
    "nonce": nonce,
    "gas": 3000000,
    "gasPrice": w3.to_wei("20", "gwei")
})

#Signing a transaction
signedtransaction=w3.eth.account.sign_transaction(transaction,private_key=SECRETCODE)

#Sending a Transaction
transactionhash=w3.eth.send_raw_transaction(signedtransaction.raw_transaction)  
transactionreceipt=w3.eth.wait_for_transaction_receipt(transactionhash)
print("Contract Deployed")

#Fetching Smart Contract Address
simplestorage=w3.eth.contract(address=transactionreceipt.contractAddress, abi=abi)

#Call- Simulates making a call and getting return value [No State Change]
#Transact- Actually makes a state change

#for a call function
print(simplestorage.functions.retrieve().call())


#for a transact function
storetransaction=simplestorage.functions.store(15).build_transaction(       #call function by building a transaction
    {"chainId":chainid, "from": MYADDRESS, "nonce":nonce+1}
)
signedstoretransaction=w3.eth.account.sign_transaction(storetransaction,private_key=SECRETCODE)  #sign that transaction
storetransactionhash=w3.eth.send_raw_transaction(signedstoretransaction.raw_transaction)    #generate transcation hash
storetransactionreceipt=w3.eth.wait_for_transaction_receipt(storetransactionhash)   #fetch the transaction receipt
