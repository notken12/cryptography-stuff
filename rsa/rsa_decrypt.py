from pathlib import Path
from sys import argv

from rsa import PrivKey, decrypt_msg, load_key_from_file


if __name__ == "__main__":
    privkey_path = Path(argv[1])
    encrypted_msg = argv[2]
    privkey: PrivKey = load_key_from_file(privkey_path)
    print(decrypt_msg(bytes.fromhex(encrypted_msg), privkey))
    print(decrypt_msg(bytes.fromhex(encrypted_msg), privkey).decode("utf-8"))
