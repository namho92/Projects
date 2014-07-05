import random
import warnings


def pow_mod(x,k,m):
    """Recursively computes x**k mod m. k,m need to be positive integers."""
    if k==1:
        return x%m
    if k%2==0:
        return ( (pow_mod(x,k/2,m)%m)**2 ) % m
    else:
        return ( (x%m) * ( ( (pow_mod(x,(k-1)/2,m)%m)**2 ) % m) )%m


#should implement deterministic primality test for n > 34155007172832
def miller_test(n):
    """Uses MIller-Rabin primality test on input. Output 'False' if n fails, and n is composite.
       Outputs 'True' if n passes the test. If n < 34155007172832, 'True' means that n is
       definitely prime. Otherwise, we deduce that there's at least a (1-4^{-20})
       chance that n is prime."""
    if (n%2==0)and(n>2):
        return False

    #setting up the bases to check
    if n < 34155007172832:
        A = [2,3,5,7,11,13,17]
        if (n in A)==True:
            return True
    else:
        A = [0]*20
        for i in range(len(A)):
            c = random.randint(2,n-2)
            while (c in A[:i]):
               c = random.randint(2,n-2)
            A[i] = c
        #n too large to use xrange and sample here
        #A = random.sample(xrange(2,n-2),20)
        warnings.warn("If 'True', n is a prime with probability > 1-4^(-20).")

    #write n = 1 + (2**s)*t
    s = 0
    while ((n-1)/2**s)%2==0:
        s = s + 1
    t = (n-1)/2**s

    #checking if n is strong pseudoprime base a, for all a in A
    for a in A:
        pseudocheck = False
        b = pow_mod(a,t,n)
        if (b==1)or(b==n-1):
            pseudocheck = True
        for j in range(1,s):
            b = (b**2)%n
            if b==n-1:
                pseudocheck = True
        if pseudocheck==False:
            return False
        
    return True
