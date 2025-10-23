from web3 import Web3
from solcx import compile_standard,install_solc
import json
install_solc("0.8.00")

rpc_url = "https://rpc.api.moonbase.moonbeam.network"
w3 = Web3(Web3.HTTPProvider(rpc_url))

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
