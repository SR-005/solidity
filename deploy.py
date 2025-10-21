import json
import os
from dotenv import load_dotenv
from solcx import compile_standard,install_solc
from web3 import Web3
install_solc("0.8.30")

load_dotenv()
MYADDRESS = os.getenv("MYADDRESS")
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
    },solc_version="0.8.30"
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
chainid=5777

#creating the contract
SimpleStorage=w3.eth.contract(abi=abi,bytecode=bytecode)
print(SimpleStorage)
