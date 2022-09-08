from brownie_tokens import MintableForkToken
from brownie import * # Brownie not best contract name

def main():
    dai_addr = config["networks"][network.show_active()]["dai_token"]
    whale = accounts[0]

    Fund_amount = 2_000_000 * 10 ** 18
    Borrow_amount = 1_000_000 * 10 ** 18

    dai = mint(dai_addr, whale, Fund_amount)
    Contract = TestUniswapFlashSwap.deploy({"from": whale})

    dai.approve(Contract.address, Fund_amount, {"from": whale})
    dai.transfer(Contract.address, Fund_amount, {"from": whale})

    tx = Contract.testFlashSwap(dai.address, Borrow_amount, {"from": whale})

    print('Flash Swap with UniSwap...\n')
    for x in tx.events['Log']:
        msg, val = x.values()
        print('\t{}:, ${:,.2f}'.format(msg,val/10**18))



def mint(coin_address, account, amount):
    # dai = MintableForkToken.from_explorer("0x6b175474e89094c44da98b954eedeac495271d0f")
    coin = MintableForkToken.from_explorer(coin_address)
    #dai._mint_for_testing(whale, amount)
    coin._mint_for_testing(account, amount)
    return coin



