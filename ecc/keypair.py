from datetime import datetime
from .curve import Curve, NIST_PRIME_384
from .point_multiplication import Point, multiply
import random


class Keypair:
    privkey: int
    pubkey: Point

    def __init__(self, curve: Curve):
        def try_gen():
            priv = random.randrange(1, curve.order)
            pub = multiply((curve.G_x, curve.G_y), priv, curve.a, curve.p)
            if pub != 0:
                self.privkey = priv
                self.pubkey = pub
            else:
                try_gen()

        try_gen()


if __name__ == "__main__":
    n = int(input("How many keypairs do you want to generate? "))
    time = datetime.now()
    for _ in range(n):
        Keypair(NIST_PRIME_384)
    print(f"Time taken to generate {n} keypairs: {datetime.now()-time}")
