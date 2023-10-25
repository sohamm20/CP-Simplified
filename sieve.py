#!/usr/bin/python
# -*- coding: utf-8 -*-


class Primes:

    def __init__(self, n):

        self.prime = [True for i in range(n + 1)]
        p = 2
        while p * p <= n:
            if self.prime[p]:
                for i in range(p * p, n + 1, p):
                    self.prime[i] = False
            p += 1

    def getPrimes(self):

        ans = []

        for i in range(1, len(self.prime)):
            if self.prime[i]:
                ans.append(i)

        return ans

    def isPrime(self, x):
        return self.prime[x]


S = Primes(100)
print S.getPrimes()
print S.isPrime(97)
