import math
def solve(g, h, p):
    N = int(math.ceil(math.sqrt(p - 1)))
    print ("N =", N)
    t = {}
    # Baby step.
    for i in range(N):
        t[pow(g, i, p)] = i
    # Print all pairs b^j for 0<=j<m
    print ("Baby step", t)
    # Fermat’s Little Theorem
    # (b^-1)^m = c , inverse of c in Z
    c = pow(g, N * (p - 2), p)
    print(c)

    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in t:
            print(y,j,t[y])
            return j * N + t[y]

    return None

print(solve(2,3,29))

