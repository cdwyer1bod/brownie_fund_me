from brownie import FundMe
from scripts.helpful_scripts import get_account, get_entrance_fee


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    print(fund_me.getPrice())
    entrance_fee = get_entrance_fee()
    print(entrance_fee)
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
