import random


def is_prime(p: int, k: int, debug: bool = False) -> bool:
    for _ in range(k):
        if not miller_rabin_test(p, debug):
            return False
    return True


def miller_rabin_test(p: int, debug: bool = False) -> bool:
    witness = random.randrange(1, min(p, 1000000))
    if debug:
        print(f"Witness: {witness}")
    exp = p - 1
    mod = pow(witness, exp, p)
    if mod != 1:
        if debug:
            print(f"Exp: {exp}, Mod: {mod}")
        return False
    while exp % 2 == 0:
        exp = exp // 2
        mod = pow(witness, exp, p)
        if debug:
            print(f"Exp: {exp}, Mod: {mod}")
        if mod != 1:
            return mod == p - 1
    return True


def generate_prime(bits: int, k: int):
    num = random.getrandbits(bits)
    while not is_prime(num, k):
        num = random.getrandbits(bits)
        if num % 2 == 0:
            num += 1
    return num
