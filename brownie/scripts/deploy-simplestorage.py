from brownie import accounts

def deploysimplestorage():
    '''account=accounts[0]'''
    account=accounts.load("metamask")
    print(account)

def main():
    print("hello sm")
    deploysimplestorage()