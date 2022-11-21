import math
def euler_phi(n):
    ans = n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ans = ans // i * (i - 1)
            while n % i == 0:
                n = n / i
    if n > 1:
        ans = ans // n * (n - 1)
    return ans



print(euler_phi(100))