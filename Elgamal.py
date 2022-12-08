import random
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def pow_mod(base, pow, mod):
    product = 1
    for idx in range(pow):
        product = product * base % mod
        #print(product,pow)
    return product

def euler_phi(a):
    ans = a
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            ans = ans // i * (i - 1)
            while a % i == 0:
                a = a / i
    if a > 1:
        ans = ans // a * (a - 1)
    return ans

def order(a, n, b):
    p = 1
    while p <= n and b ** p % a != 1:
        p += 1
    if p <= n:
        return p
    else:
        return -1

def primitive_root(a):
    n = euler_phi(a)
    for b in range(2, a):
        if order(a, n, b) == n:
            return b


def modInverse(a,m):
    for i in range(1, m):
        if (((a % m) * (i % m)) % m == 1):
            return i
    return -1

def bbs(s):
    # s is relatively prime to n
    # two large prime p and q where n = p * q
    # p and q are secretly kept, n is public and reusable
    p = 173
    q = 271
    n = p * q

    x = []
    x.append(s ** 2 % n)
    b = []

    # set 50 digit
    for i in range(1, 50):
        num = x[i - 1] ** 2 % n
        x.append(num)
        b.append(x[i] % 2)

    # convert list b binary number to decimal
    d_num = int(''.join(str(x) for x in b), 2)

def baby_step_giant_step(g, y, p):
    # Compute m = floor(sqrt(p))
    m = int(p ** 0.5)

    # Compute the powers of g mod p
    powers = {g ** i % p: i for i in range(m)}

    # Compute the inverse of g^m mod p
    g_inv_m = pow(g, p-1-m, p)

    for j in range(m):
        # Compute y * (g^m)^j modulo p
        y_j = y * pow(g_inv_m, j, p) % p

        # Check if y * (g^m)^j is in the powers dictionary
        if y_j in powers:
            # If y * (g^m)^j is in the powers dictionary, return the corresponding exponent
            return powers[y_j] + j * m

    # If the exponent is not found, return None
    return None


def elgamal(m,p,g):
    # x is private key
    x = random.randint(1,p-2)

    # y is public key
    y = pow_mod(g,x,p)

    # random pick k
    k = random.randint(1,p-2)

    # Encryption alice send y1 y2 to bob
    y1 = pow_mod(g,k,p)
    y2 = m * y % p

    print(y1,y2)

    # Decryption
    d_message = y2 * modInverse(pow(y1,x,p),p) % p














