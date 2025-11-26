from brownie import accounts, SimpleStorage, network
import os,time

def deploysimplestorage(account):

    '''account=accounts[0]'''   #for default brownie ganache account
    '''account=accounts.load("metamask")'''     #one of the method for loading external account --but need to enter passwrd each time 
    '''account=accounts.add(os.getenv("METAMASK_SECRETKEY"))'''  #fetching the account from .env variable

    print("Wallet Address: ",account)

    #deploying smart contract
    simplestorage=SimpleStorage.deploy({"from":account})
    

def simplestorageinteract(account):
    simplestorage=SimpleStorage[-1]     #retrieve address of latest deployed contract

    #simple call function- no transaction  
    value=simplestorage.retrieve()
    print("Old Value: ",value)

    #transaction function
    transaction=simplestorage.store(20, {"from":account})
    transaction.wait(1)     #wait for transaction block to confirm
    value=simplestorage.retrieve()
    print("New Value: ",value)


def main():
    if network.show_active()=="development":
        account=accounts[0]
    else:
        account=accounts.add(os.getenv("METAMASK_SECRETKEY"))

    #run once to deploy smart contract
    '''deploysimplestorage(account)'''

    #function to interact with deployed smart contract
    simplestorageinteract(account)

    #for a clean connection termination
    time.sleep(2)
    network.disconnect()    