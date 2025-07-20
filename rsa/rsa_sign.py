from pathlib import Path
from sys import argv

from rsa import PrivKey, load_key_from_file, sign_msg


if __name__ == "__main__":
    privkey_path = Path(argv[1])
    msg = bytes(argv[2], "utf-8")
    privkey: PrivKey = load_key_from_file(privkey_path)
    print(sign_msg(msg, privkey).hex())
