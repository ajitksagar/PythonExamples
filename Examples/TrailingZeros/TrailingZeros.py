import math

#Traditional loop method
def zeros_loop(n):
        n_fact = math.factorial(n)
        lth = len(str(n_fact))
        count = 0
        i=0
        while i <= lth:
           if n_fact%10!= 0:
             break
           else:
            n_fact = n_fact / 10
            count = count + 1
        i+=1
        return count

def zeros(n):
    i = 1
    count = 0
    factor = 0
    while (5 ** i) <= n:
        factor = n / (5 ** i)
        count = count + factor
        i += 1
    return count

def zeros_recursion(n):
    x = n/5
    return x+zeros_recursion(x) if x else 0