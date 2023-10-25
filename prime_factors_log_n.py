# Contributed by Soham Mirikar

MAX = 100000
import math as mt

class primeFactors:
        
    def __init__(self, n):
        
        self.MAXN = n + 1
        
        self.spf = [0 for i in range(self.MAXN)]
        
        self.spf[1] = 1
        
        for i in range(2, self.MAXN):
            self.spf[i] = i
        
        for i in range(4, self.MAXN, 2):
            self.spf[i] = 2
     
        for i in range(3, mt.ceil(mt.sqrt(self.MAXN))):
            if (self.spf[i] == i):
                for j in range(i * i, self.MAXN, i): 
                    if (self.spf[j] == j):
                        self.spf[j] = i
        
    def getFactorization(self, x):
        ret = dict()
        while (x != 1):
            temp = self.spf[x]
            
            if temp not in ret:
                ret[temp] = 0
            
            ret[temp] += 1
            x = x // self.spf[x]
        
        return ret

primes = primeFactors(MAX)

print(primes.getFactorization(100))
