from brownie import AcademicToken, accounts

def deploy_token():
    my_token = AcademicToken.deploy({"from":accounts[0]})
    return my_token
def main():
    deploy_token()

main()