import math
from pathlib import Path
from sys import argv

from rsa import PubKey, encrypt_msg, load_key_from_file


if __name__ == "__main__":
    pubkey_path = Path(argv[1])
    msg = bytes(argv[2], encoding="utf-8")
    pubkey: PubKey = load_key_from_file(pubkey_path)
    print(encrypt_msg(msg, pubkey).hex())
