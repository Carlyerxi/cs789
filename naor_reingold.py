import random
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def fastexp(base, pow, mod):
    product = 1
    for idx in range(pow):
        product = product * base % mod
        #print(product,pow)
    return product

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

def random_bitnumber(n):
    p = random.randint(0, 2**n - 1)
    q = random.randint(0, 2**n - 1)
    r = random.randint(0, 2**(2*n) - 1)

    while is_prime(p) is False:
        p = random.randint(0, 2**n - 1)
    while is_prime(q) is False:
        q = random.randint(0, 2**n - 1)

    while p == q:
        q = random.randint(0, 2 ** n - 1)
        while is_prime(q) is False:
            q = random.randint(0, 2 ** n - 1)

    return p,q,r


#print(random_bitnumber(6))

# p,q,r generator by random_bitnumber
def naor_reingold(n,p,q,x,r):
    N = p*q
    numbers = []
    pairs = []

    for i in range(2*n):
        num = random.randint(1,N)
        numbers.append(num)

    # generate a sequence of pairs a where lable as a1,0 a1,1 a2,0 a2,1...a6,1
    for i in range(0, len(numbers), 2):
        pairs.append((numbers[i], numbers[i + 1]))
    #print(pairs)

    g = random.randint(0,N)

    while gcd(g,N) == 1:
        g = g*g % N
        break
    #print(g)

    # convert binary x to decimal and each number stand for a sequence of x
    binary = format(x, "b")
    binary_x = list((map(int, binary)))
    #print(binary_x)


    # compute e as sum of vaule from a1,x1 + a2,x2 ... + an,xn
    pair_match = []
    e = 0
    for i in range(n):
        pair_match.append(pairs[i][binary_x[i]])
        for num in pair_match:
            e += num
    #print(pair_match)
    #print(e)

    # compute g^e mod N 2n bits binary
    nx_digit = fastexp(g,e,N)

    # convert nx into binary and padding extra zero on the left side
    nx_binary = list(bin(nx_digit).replace('0b', '').zfill(2*n))
    nx_list = [int(s) for s in nx_binary]
    #print(nx_digit)
    #print(nx_list)


    # compare nx_binary with random 2n digits binary which is r
    # convert r into 2n digits binary
    # function u * v = (u1v1 + ... + unvn)%2
    r_binary = list(bin(r).replace('0b', ''))
    r_list = [int(s) for s in r_binary]
    #print(r_list)


    bin_match = []
    for x,y in zip(nx_list, r_list):
        bin_match.append((x*y))

    bin_result = sum(bin_match) % 2
    #print(bin_match)
    return bin_result



#print(naor_reingold(6,11,7,43,3815))

def naro_reingold_generator():
    #pick random n and x
    n = 6
    x = 43
    while n == 6:
        p = int(random_bitnumber(6)[0])
        q = int(random_bitnumber(6)[1])
        r = int(random_bitnumber(6)[2])

        print("naor reingold random generator number is:", naor_reingold(6, p, q, 43, r))
        break

naro_reingold_generator()






