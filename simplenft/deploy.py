from solcx import compile_standard, install_solc
import json

install_solc("0.8.20")

# Load Solidity file
with open("./simplenft/simplenft.sol", "r") as f:
    source = f.read()

compiledsol = compile_standard(
    {
        "language": "Solidity",
        "sources": {
            # IMPORTANT: Use the REAL VIRTUAL FILE PATH
            "contracts/simplenft.sol": {"content": source}
        },
        "settings": {
            "remappings": [
                "@openzeppelin/=node_modules/@openzeppelin/"
            ],
            "outputSelection": {
                "*": {
                    "*": ["abi", "evm.bytecode"]
                }
            }
        }
    },
    solc_version="0.8.20"
)

with open("compiled.json", "w") as file:
    json.dump(compiledsol, file, indent=2)

print("Compiled successfully!")
