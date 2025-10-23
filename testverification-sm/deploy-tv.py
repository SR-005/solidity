from web3 import Web3
from solcx import compile_standard,install_solc
import json
from dotenv import load_dotenv
import os
install_solc("0.8.00")

load_dotenv()
MYADDRESS = Web3.to_checksum_address(os.getenv("METAMASK"))
SECRETCODE = os.getenv("METAMASK_SECRETKEY")

#Read the Smart Contract
with open("./testverification-sm/test-verification.sol","r") as file:
    testverificationfile=file.read()

#complie the smart contract - default lines
compiledsol = compile_standard(
    {
        "language":"Solidity",
        "sources":{"test-verification.sol":{"content":testverificationfile}},
        "settings":{
            "outputSelection":  {
                "*":{"*": ["abi","metadata","evm.bytecode","evm.sourceMap"]}
            }
        }
    },solc_version="0.8.17"
)

#move the compiled code into a new file 'compiledcode.json'
with open("./testverification-sm/compiledtvcode.json","w") as file:
    json.dump(compiledsol,file)

#fetching bytecode from the compiled Smart Contract
bytecode=compiledsol["contracts"]["test-verification.sol"]["TestVerification"]["evm"]["bytecode"]["object"]

#get abi from the compiled Smart Contract
abi=compiledsol["contracts"]["test-verification.sol"]["TestVerification"]["abi"]


w3 = Web3(Web3.HTTPProvider("https://rpc.api.moonbase.moonbeam.network"))
chainid=1287

#creating the contract
TestVerification=w3.eth.contract(abi=abi,bytecode=bytecode)
print("Contract Created")

balance = w3.eth.get_balance(MYADDRESS)
print("Balance:", w3.from_wei(balance, "ether"), "DEV")

#fetching nonce(latest transaction) of our wallet
nonce=w3.eth.get_transaction_count(MYADDRESS,"pending")

transaction = TestVerification.constructor().build_transaction({
    "chainId": chainid,
    "from": MYADDRESS,
    "nonce": nonce,
    "gas": 7000000,
    "gasPrice": w3.to_wei("20", "gwei")
})

#Signing a transaction
signedtransaction=w3.eth.account.sign_transaction(transaction,private_key=SECRETCODE)

#Sending a Transaction
transactionhash=w3.eth.send_raw_transaction(signedtransaction.raw_transaction)
print(transactionhash)
transactionreceipt=w3.eth.wait_for_transaction_receipt(transactionhash)
print("Contract Deployed")

#Fetching Smart Contract Address
print(transactionreceipt.contractAddress)