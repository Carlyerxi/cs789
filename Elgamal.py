import random
import math
import unittest

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

# when a^b mod n is 1, the smallest integer b is the order of a mod n
# according to euler theory phi(n) would be a solution
# when phi(n) is the order of a mod n, a is the primitive root of n
def order(a, n, b):
    p = 1
    while p <= n and b ** p % a != 1:
        p += 1
    if p <= n:
        return p
    else:
        return -1

#print(order(5,7,6))

def primitive_root(p):
    n = euler_phi(p)
    for a in range(2, p):
        if order(p, n, a) == n:
            return a

#print(primitive_root(7))

def modInverse(a,m):
    for i in range(1, m):
        if (((a % m) * (i % m)) % m == 1):
            return i
    return -1

def baby_step_giant_step(g, y, p):
    m = int(math.ceil(math.sqrt(p - 1)))
    S = {pow(g, j, p): j for j in range(m)}
    gs = pow(g, p - 1 - m, p)
    for i in range(m):
        if y in S:
            return i * m + S[y]
        y = y * gs % p
    return None

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


def elgamal(p):
    # alice choose prime p and integer g in Zp
    # encrypt message m
    m = 29
    print("the plaintext is:", m)

    g = primitive_root(p)
    print("the primitive root of p is:",g)

    # d is alice private key
    d = random.randint(1,p-1)

    beta = pow_mod(g,d,p)

    # alice's public key (p,g,beta)


    # bob random pick k
    k = random.randint(1,p-1)

    # Encryption m (1 <= m <= p-1) send y1 y2 to alice
    y1 = pow_mod(g,k,p)
    y2 = (m * pow_mod(beta,k,p)) % p

    # ciphertext y1 y2 are public
    cipher = y1,y2

    print("the alice's private d is: ",d," β is: ",beta," and bob's random k is:",k)
    print("bob send the ciphertext:",cipher)

    # Decryption based on m = y1^(-k) * y2 mod p
    d_message = y2 * modInverse(pow(y1,d,p),p) % p

    print("alice's decrypt message is:",d_message)

    # Eve intercept alice and bob's message
    # with knowing alice public key (p,g,y) and bob ciphertext y1 and y2
    # since ciphertext consists random k, we need to use bsgs to compute the discrete log of y

    # x is the alice private key d
    x = baby_step_giant_step(g, beta, p)
    print("eve decrypt alice's private d is:", x)

    # once alice private d is known, Eve can get beta pow(g,d,p)
    # then just repeat d_message
    new_beta = pow(g,x,p)
    print("eve calculate the beta value and get:",new_beta)

    if new_beta == beta:
        d_message = y2 * modInverse(pow(y1, d, p), p) % p

    print("Eve's decryption is:", d_message)

elgamal(37)

class TestRSA(unittest.TestCase):
    def test_order(self):
        # test Order that 5^6 mod 7 is 1
        self.assertEqual(order(5,7,6), 1)

    def test_primitive_root(self):
        self.assertEqual(primitive_root(37),2)
        self.assertEqual(primitive_root(7919),7)
        self.assertEqual(primitive_root(7), 3)


    def test_bsgs(self):
        self.assertEqual(baby_step_giant_step(2,16,37),4)


if __name__ == '__main__':
    unittest.main()




