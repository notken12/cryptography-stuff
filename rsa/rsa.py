# bezout's identity:
# ax + by = gcd(a, b)
# x is the modular multiplicative inverse of a mod b
# => a * x = 1 (mod b)

# extended euclidean algorithm:
# gives:
# r_k: gcd(a, b)
# s_k: x
# t_k: y
# -
# s_i+1 = s_i-1 - q_i*s_i
# q_i = r_i-2 // r_i-1

# we only need to compute either s_k or t_k if we wanna make a function
# for finding modular multiplicative inverse


from hashlib import md5
import json
import math
from pathlib import Path
from typing import Tuple, TypedDict
from primes import generate_prime


def mod_multiplicative_inverse(a: int, b: int) -> int:
    """
    Returns the modular multiplicative inverse of `a` modulo `b`.
    `a` and `b` must be coprime.
    """
    old_r, r = a, b
    old_s, s = 1, 0

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s

    return old_s


def phi_n(p: int, q: int) -> int:
    """Returns `phi(n)` where `n` is the product of prime numbers `p` and `q`."""
    return (p - 1) * (q - 1)


def decryption_exponent(e: int, phin: int) -> int:
    return mod_multiplicative_inverse(e, phin)


class PubKey(TypedDict):
    e: int
    n: int


def encrypt_msg(msg: bytes, pubkey: PubKey) -> bytes:
    return int.to_bytes(
        pow(int.from_bytes(msg, "big"), pubkey["e"], pubkey["n"]),
        math.ceil(pubkey["n"].bit_length() / 8),
        "big",
    )


class PrivKey(PubKey):
    d: int


def decrypt_msg(m_e: bytes, privkey: PrivKey) -> bytes:
    return int.to_bytes(
        pow(int.from_bytes(m_e, "big"), privkey["d"], privkey["n"]), len(m_e), "big"
    )


def save_key_to_file(key: PubKey, path: Path):
    with open(path, "w") as file:
        file.write(json.dumps(key, indent=2))


def load_key_from_file(path: Path):
    with open(path) as file:
        return json.loads(file.read())


def generate_keypair(bits: int) -> Tuple[PubKey, PrivKey]:
    e = 65537
    p = generate_prime(bits // 2, 20)
    q = generate_prime(bits // 2, 20)
    phin = phi_n(p, q)
    # phin and e must be relatively prime
    if phin % e == 0:
        # we can't have that because there would be no possible
        # decryption exponent since there wouldn't be any
        # modular multiplicative inverse
        return generate_keypair(bits)
    d = decryption_exponent(e, phin)
    n = p * q
    return ({"e": e, "n": n}, {"e": e, "n": n, "d": d})


def sign_msg(msg: bytes, privkey: PrivKey) -> bytes:
    hash = md5(msg).digest()
    return int.to_bytes(
        pow(int.from_bytes(hash, "big"), privkey["d"], privkey["n"]),
        math.ceil(privkey["n"].bit_length() / 8),
        "big",
    )


def verify_signed_msg(msg: bytes, signature: bytes, pubkey: PubKey) -> bool:
    msg_hash = md5(msg).digest()
    # decode the signature using the public exponent
    # since (m^e)^d = (m^d)^e (mod n)
    signature_hash_int = pow(int.from_bytes(signature, "big"), pubkey["e"], pubkey["n"])
    # Convert back to bytes, handling the case where the result might be larger than the hash
    signature_hash = signature_hash_int.to_bytes(
        math.ceil(signature_hash_int.bit_length() / 8), "big"
    )
    return msg_hash == signature_hash
