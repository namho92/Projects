import math
import fractions
import random
import numpy as np
import numpy.polynomial.polynomial as P


def factor_pollard(n):
    """Finds a factor of the input if it is composite. This uses
    Pollard's rho algorithm, so it won't work if the input is prime."""
    a = random.randint(1,n-3)
    s = random.randint(0,n-1)
    x = s
    y = s
    d = 1
    count = 0
    while d==1:
        x = (x**2 + a) % n
        y = ( ((y**2 + a)%n)**2 + a ) % n
        d = fractions.gcd(abs(x-y),n)
        count = count + 1
    if d==n or count>1000:
        #return find_factor_pollard(n)
        print count
        return 0
    else:
        return d


#for some reason the fancy multipoint eval doesn't work well, so here's a naive method
#(btw, I think the problem is using np's polyval, it won't let me take mods at each stage.
#possible improvement: use alg9.6.1 for poly-mult and fix alg9.6.5 for poly-eval
def factor_strassen(n):
    """Uses the Pollard-Strassen method for finding factors.
       Returns a non-trivial factor if it exists, or 0 if n is prime."""
    B = int(math.floor(n**0.25)+1)
    f = np.ones(B,dtype='int64')
    print B
    #this for loop evaluates B-sized chunks of (B**2)!.
    #Below is a naive way, the proper way uses product trees and multipoint eval here.
    for i in range(B):
        jmin = 1 + i*B
        jmax = jmin + B - 1
        #making f[i] = (iB+1)(iB+2)...((i+1)B).
        for j in range(jmin, jmax+1):
            f[i] = (f[i]*j) % n

    for i in range(B):
        factor = fractions.gcd(f[i],n)
        if factor!=1:
            return factor

    return 0


###TO DO: add defaulting m to 0
###possible improvements: do that preassebling of the polynomial remainder tree
###challenge: implement your own poly class instead of using numpy
##def multi_eval_poly(coeff,points,m):
##    """Evaluates an array of points for given polynomial. Optional argument m is
##       for evaluation modulo m. Set m=0 for no modulo evaluation.""" 
##    threshold = 4
##    #d = len(coeff)
##    coeff = np.array(coeff,dtype='int64')%m
##
##    if len(points)<=threshold:
##        if m==0:
##            return P.polyval(points,coeff)
##        else:
##            return P.polyval(points,coeff)%m
##    else:
##        if len(points)%2==0:
##            lower = points[:len(points)/2]
##            upper = points[len(points)/2:]
##        else:
##            lower = points[:(len(points)+1)/2]
##            upper = points[(len(points)+1)/2:]
##
##        if m!=0:
##            w = P.polyfromroots(lower)%m
##            z = P.polyfromroots(upper)%m
##        else:
##            w = P.polyfromroots(lower)
##            z = P.polyfromroots(upper)
##
##        if m!=0:
##            a = P.polydiv(coeff,w)[-1]%m
##            b = P.polydiv(coeff,z)[-1]%m
##        else:
##            a = P.polydiv(coeff,w)[-1]
##            b = P.polydiv(coeff,z)[-1]
##
##        return np.concatenate([multi_eval_poly(a,lower,m),multi_eval_poly(b,upper,m)])
##
##
##def find_factor_strassen(n):
##    B = int(math.floor(n**0.25)+1)
##    f = P.polyfromroots(range(B))
##    print B,f
##    points = (np.arange(B)+1)*B
##
##    eval = multi_eval_poly(f,points,n)
##    
##    for j in (np.arange(len(eval))+1):
##        if abs(fractions.gcd(eval[j-1],n))>1:
##            if (abs(fractions.gcd(eval[j-1],n))>(j-1)*B)and(abs(fractions.gcd(eval[j-1],n))<=j*B):
##                return int(fractions.gcd(eval[j-1],n))
##            else:
##                for k in (range(B)+(j-1)*B+1):
##                    if abs(fractions.gcd(k,n))>1:
##                        return int(abs(fractions.gcd(k,n)))
##    
##    return 0
