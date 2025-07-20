from ecc.point_multiplication import multiply
from .keypair import Keypair, NIST_PRIME_384


alice = Keypair(NIST_PRIME_384)
bob = Keypair(NIST_PRIME_384)

print(f"alice sends pubkey to bob: {alice.pubkey}")
print(f"bob sends pubkey to alice: {bob.pubkey}")

bob_secret = multiply(alice.pubkey, bob.privkey, NIST_PRIME_384.a, NIST_PRIME_384.p)
alice_secret = multiply(bob.pubkey, alice.privkey, NIST_PRIME_384.a, NIST_PRIME_384.p)

assert bob_secret == alice_secret

print(f"bob now has the shared secret: {bob_secret}")
print(f"alice now has the shared secret: {alice_secret}")
