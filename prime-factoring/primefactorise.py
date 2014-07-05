import findfactor
import checkprime


def get_number():
    return abs(int(input("Enter a positive integer: ")))


def factorise(n):
    """Returns the non-trivial factors of n in a list with multiplicity."""
    factors = [n]
    if checkprime.miller_test(n)==True:
        return factors
    fac1 = findfactor.factor_pollard(n)
    if fac1==0:
        fac1 = findfactor.factor_strassen(n)
    fac2 = n/fac1
    assert fac1*fac2==n

    return sorted(factorise(fac1) + factorise(fac2))


#not sure what the purpose of main() is
def main():
    n = get_number()

    if checkprime.miller_test(n)==True:
        print "%d is prime." % n
    else:
        print "The prime factors of %d are %r." % (n, factorise(n))


#dunno what this is either
if __name__ == "__main__":
    main()
