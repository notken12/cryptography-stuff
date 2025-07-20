from typing import Literal, Tuple
import math

Point = Tuple[int, int] | Literal[0]


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


def add(p: Point, q: Point, mod: int) -> Point:
    if p == 0:
        return q
    if q == 0:
        return p
    if p[0] == q[0]:
        return 0
    slope = ((q[1] - p[1]) * mod_multiplicative_inverse(q[0] - p[0], mod)) % mod
    x = (slope * slope - p[0] - q[0]) % mod
    y = (slope * (p[0] - x) - p[1]) % mod
    return (x, y)


def double(p: Point, a: int, mod: int) -> Point:
    if p == 0:
        return 0
    slope = ((3 * p[0] * p[0] + a) * mod_multiplicative_inverse(2 * p[1], mod)) % mod
    q = p
    x = (slope * slope - p[0] - q[0]) % mod
    y = (slope * (p[0] - x) - p[1]) % mod
    return (x, y)


def get_bit(n: int, pos: int):
    return (n >> pos) & 1


def multiply(p: Point, k: int, a: int, mod: int) -> Point:
    n = k.bit_length()
    r0 = p
    r1 = double(p, a, mod)
    for i in range(n - 2, 0, -1):
        if get_bit(k, i) == 1:
            r0 = add(r0, r1, mod)
            r1 = double(r1, a, mod)
        else:
            r1 = add(r0, r1, mod)
            r0 = double(r0, a, mod)
    return r0
