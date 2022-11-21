def pow_mod(base, pow, mod):
    product = 1
    for idx in range(pow):
        product = product * base % mod
        print(product,pow)
    return product


print(pow_mod(11,3,28))