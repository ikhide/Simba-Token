from scripts.helpful_scripts import get_account
from brownie import MyToken, network, config
from web3 import Web3


def deploy():
    """
    Deploys the contract and print the address
    """

    account = get_account()
    initial_supply = Web3.toWei(1000000000, 'ether')
    token = MyToken.deploy(initial_supply, {'from':account},publish_source=config['networks'][network.show_active()]['verify'])
    print(token.address)
    print(token.totalSupply())

def main():
    deploy()

