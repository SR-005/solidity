from brownie import SimpleStorage, accounts

def test_deploy():
    #Arrage
    account=accounts[0]

    #Act
    simplestorage=SimpleStorage.deploy({"from":account})
    initialvalue=simplestorage.retrieve()
    expected=5  #what is the value that we expect from the above function call

    #Assert
    assert initialvalue==expected   #check if initialvalue is the same as expected value from the function call