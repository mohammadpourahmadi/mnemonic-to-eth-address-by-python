from bip44 import Wallet
from bip44.utils import get_eth_addr
from ecdsa.keys import PrivateKey

# Define a function to process mnemonics and write Ethereum addresses to a file
def process_mnemonics(input_file, output_file):
    with open(input_file, 'r') as input_text, open(output_file, 'w') as output_text:
        for line in input_text:
            mnemonic = line.strip()  # Assuming each line contains one mnemonic
            w = Wallet(mnemonic)
            sk, pk = w.derive_account("eth", account=0)
            sk = PrivateKey(sk)
            if sk.public_key.format() == pk:
                eth_address = get_eth_addr(pk)
                output_text.write(f"Mnemonic: {mnemonic}\n")
                output_text.write(f"Ethereum Address: {eth_address}\n\n")

# Specify your input and output file paths
input_file_path = 'input_mnemonics.txt'  # Change this to your input file path
output_file_path = 'output_addresses.txt'  # Change this to your desired output file path

# Call the function to process mnemonics and save Ethereum addresses to the output file
process_mnemonics(input_file_path, output_file_path)
