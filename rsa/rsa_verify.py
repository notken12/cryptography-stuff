import math
from pathlib import Path
from sys import argv

from rsa import PubKey, load_key_from_file, verify_signed_msg


if __name__ == "__main__":
    pubkey_path = Path(argv[1])
    msg = bytes(argv[2], encoding="utf-8")
    signature = bytes.fromhex(argv[3])
    pubkey: PubKey = load_key_from_file(pubkey_path)
    print(verify_signed_msg(msg, signature, pubkey))
