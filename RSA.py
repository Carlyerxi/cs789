import unittest
import random

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Extended Euclidean Algorithm
def exgcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = exgcd(b, a % b)
    return d, y, x - (a // b) * y

def fastexp(base, pow, mod):
    product = 1
    for idx in range(pow):
        product = product * base % mod
        #print(product,pow)
    return product

def pollardRho(n):
    x = 2
    y = x ** x + 1
    g = 1

    while g == 1:
        x = (x * x + 1) % n
        y = (y * y + 1) % n
        y = (y * y + 1) % n
        g = gcd(abs(x - y), n)

    if g == n:
        return None
    else:
        return g


#print(pollardRho(646184512626547))

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

    print(b)
    print(d_num)

#print(bbs(977))

def is_prime(n, k=10):
    # Handle small numbers
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0:
        return False

    # Find r and d such that n - 1 = 2^r * d
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Test the number against k witnesses
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def createkeys(p,q):
    # randomly choose two unequal prime numbers p and q
    # computes the product n of p and q
    n = p * q

    # fn is the euler function of n
    fn = (p-1) * (q-1)

def pick_e(fn):
    # random pick e, let 1<e<fn and gcd(e,fn) = 1
    while True:
        e = random.randint(0,fn)
        if gcd(e,fn) == 1:
            return e

def pick_d(e,fn):
    # computes the modulo inverse element d of e using Extended Euclidean Algorithm
    x,y,r = exgcd(e,fn)

    if y < 0:
        return fn + y
    return y

def encryption(M,e,n):
    # M is plaintext of the message
    return fastexp(M,e,n)

def decrypttion(C,d,m):
    # C is the ciphertext of the message
    return fastexp(C,d,m)

# How to break RSA with known n and e:
# (1) ed≡1 (mod φ(n)). Only knowing e and φ(n) can d be calculated
# (2) φ(n)=(p-1)(q-1). Only knowing p and q can we calculate φ(n)
# (3) n=pq. Only by decomposing n into factors can p and q be calculated
# We will use the factorization of large integers in this project to break RSA

class TestRSA(unittest.TestCase):
    def test_gcd(self):
        # bbs random s and n are 977 and 46883
        self.assertEqual(gcd(977,46883), 1)

    def test_pollardRho(self):
        self.assertEquals(pollardRho(3),None)

    def test_miller_rabin(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(100))

        # pollardRho factorization large number 646184512626547 get 5057989 and try prime test
        self.assertTrue(is_prime(5057989))

        # 182096120426651 is the decimal number converted by Blum-Blum-Shub Pseudorandom Number Generator
        self.assertTrue(is_prime(182096120426651))



if __name__ == '__main__':
    unittest.main()


