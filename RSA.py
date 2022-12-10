import unittest
import math
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

    # return gcd d and y,x
    return d, y, x - (a // b) * y

def fastexp(b, p, d):
    product = 1
    for idx in range(p):
        product = product * b % d
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
    return int(ans)

def modInverse(a,m):
    for i in range(1, m):
        if (((a % m) * (i % m)) % m == 1):
            return i
    return -1

def pollardRho(n):
    x = 2
    y = x ** x + 1
    g = 1

    while g == 1:
        x = (x * x + 1) % n
        y = (pow(y*y + 1,2) + 1) % n
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

    #print(b)
    #print(d_num)
    return d_num

#print(bbs(977))
# get decimal number 182096120426651

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

def pick_e(fn):
    # random pick e, let 1<e<fn and gcd(e,x) = 1
    while True:
        e = random.randint(0,fn)
        if gcd(e,fn) == 1:
            return e

def pick_d(e,fn):
    d = modInverse(e,fn)
    return d

def encryption(M,e,n):
    # M is plaintext of the message
    return fastexp(M,e,n)

def decryption(C,d,n):
    # C is the ciphertext of the message
    return fastexp(C,d,n)

def rsa_process():
    # M is plaintext, C is ciphertext
    # public key(n,e), private key(n,d)
    M = 79
    print("your plaintext is:", M)

    p = 173
    q = 271

    while p != q:
        n = p*q
        fn = euler_phi(n)
        e = pick_e(fn)
        d = pick_d(e, fn)
        print("the n is:",n, " and φ(n) is:",fn)
        # n is 46883 fn is 46440
        print("the e is:",e, " and d is:",d)

        c = encryption(M, e, n)
        print("encrypt message is:",c)
        print("decrypt message is:",decryption(c,d,n))
        break

rsa_process()


# How to break RSA with known n and e:
# (1) ed≡1 (mod φ(n)). Only knowing e and φ(n) can d be calculated
# (2) φ(n)=(p-1)(q-1). Only knowing p and q can we calculate φ(n)
# (3) n=pq. Only by decomposing n into factors can p and q be calculated
# We will use the factorization of large integers in this project to break RSA

class TestRSA(unittest.TestCase):
    def test_gcd(self):
        # bbs random s and n are 977 and 46883
        self.assertEqual(gcd(977,46883), 1)

    def test_exgcd(self):
        self.assertEqual(exgcd(63,57),(3,-9,10))

    def test_pollardRho(self):
        self.assertEqual(pollardRho(646184512626547),5057989)

    def test_fastexp(self):
        self.assertEqual(fastexp(2,5,7),4)

    def test_phi(self):
        self.assertEqual(euler_phi(46883),46440)

    def test_modinverse(self):
        self.assertEqual(modInverse(17,3120),2753)

    def test_miller_rabin(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(100))

        # test p,q in example
        self.assertTrue(is_prime(173))
        self.assertTrue(is_prime(271))

        # pollardRho factorization large number 646184512626547 get 5057989 and try prime test
        self.assertTrue(is_prime(5057989))
        self.assertTrue(is_prime(127755223))

        # 182096120426651 is the decimal number converted by Blum-Blum-Shub Pseudorandom Number Generator
        self.assertTrue(is_prime(182096120426651))


    def test_bbs(self):
        self.assertTrue(bbs(977),182096120426651)

    def test_e(self):
        self.assertTrue(gcd(pick_e(46440),46440),1)

    def test_d(self):
        self.assertTrue(modInverse(pick_e(46440),46440),1)

if __name__ == '__main__':
    unittest.main()


