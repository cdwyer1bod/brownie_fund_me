from brownie import network, config, accounts, MockV3Aggregator, FundMe
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 2000000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


def get_entrance_fee():
    min_usd = 50 * 10**18
    price = FundMe[-1].getPrice()
    precision = 1 * 10**18 * 10**18
    return (min_usd * precision) / price


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks")
    # V3 Aggregator is just a list of all the V3 Aggregators we've deployed
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, Web3.toWei(
            STARTING_PRICE, "ether"), {"from": get_account()})
