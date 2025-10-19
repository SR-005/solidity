from solcx import compile_standard,install_solc
install_solc("0.8.30")

#Read the Smart Contract
with open("./simple-storage.sol","r") as file:
    simplestoragefile=file.read()


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

print(compiledsol)