import json
from solcx import compile_standard,install_solc
install_solc("0.8.30")

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

print("ABI: ",abi)