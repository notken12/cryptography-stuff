from datetime import datetime


def mod_exp(base, exp, mod):
    if mod == 1:
        return 0
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result


test_cases = [
    [base, exp, mod]
    for base in range(10000, 10101)
    for exp in range(10000, 10101)
    for mod in range(10000, 10101)
]


for [base, exp, mod] in test_cases:
    assert mod_exp(base, exp, mod) == pow(base, exp, mod)

print(f"Fast modular exponentiation function passed {len(test_cases)} test cases")

start = datetime.now().timestamp()
for [base, exp, mod] in test_cases:
    mod_exp(base, exp, mod)
print(
    f"Invoked fast modular exponentiation function for {len(test_cases)} test cases in {(datetime.now().timestamp() - start)*1000}ms"
)

start = datetime.now().timestamp()
for [base, exp, mod] in test_cases:
    pow(base, exp, mod)
print(
    f"Invoked builtin fast modular exponentiation function for {len(test_cases)} test cases in {(datetime.now().timestamp() - start)*1000}ms"
)

print("Testing naive modular exponentiation... (will take a while)")

start = datetime.now().timestamp()
for [base, exp, mod] in test_cases:
    (base**exp) % mod
print(
    f"Naively evaluated modular exponentiation for {len(test_cases)} test cases in {(datetime.now().timestamp() - start)*1000}ms"
)
