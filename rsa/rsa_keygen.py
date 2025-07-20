from pathlib import Path
from sys import argv
from rsa import generate_keypair, save_key_to_file


if __name__ == "__main__":
    keyname = argv[1]
    pubkey_path = Path(keyname + ".pub")
    privkey_path = Path(keyname + ".key")
    print("Generating and saving keypair...")
    (pubkey, privkey) = generate_keypair(2048)
    save_key_to_file(pubkey, pubkey_path)
    save_key_to_file(privkey, privkey_path)
    print(f"Public and private keys saved to {pubkey_path} and {privkey_path}")
