from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()
    # pass price feeed address
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:  # use mock address if on development chain
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        print("Mocks deployed")

    publish_source = config["networks"][network.show_active()].get("verify")
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account, },
        publish_source=publish_source
    )

    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
