from brownie import accounts, SimpleStorage, network
import os,time

def deploysimplestorage():
    account=accounts[0]   #for default brownie ganache account

    '''account=accounts.load("metamask")'''     #one of the method for loading external account --but need to enter passwrd each time 
    '''account=accounts.add(os.getenv("METAMASK_SECRETKEY"))'''   #fetching the account from .env variable

    print(account)
    simplestorage=SimpleStorage.deploy({"from":account})  
    #simple call function- no transaction  
    value=simplestorage.retrieve()
    print("Old Value: ",value)

    #transaction function
    transaction=simplestorage.store(15, {"from":account})
    transaction.wait(1)     #wait for transaction block to confirm
    value=simplestorage.retrieve()
    print("New Value: ",value)


def main():
    print("hello sm")
    deploysimplestorage()
    time.sleep(2)
    network.disconnect()    #for a clean connection termination