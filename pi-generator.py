#def pi_term(n):
#    "Returns the nth term in the infinite expansion of pi."
#	return 4.0 * (-1)^{n+1} / (2.0*n-1)

#obtain user input for number of digits
def get_digits():
    digits = int(input("How many digits of pi do you want? "))
	
    while (digits <= 0) or (digits > 10000):
        if digits <= 0:
    	    digits = int(input("Please enter a non-negative number. "))
    	else:
    	    digits = int(input("Please enter a number no greater than 10000. "))
    
    return digits


#not sure what the purpose of main() is
def main():
    print "You want %r digits." % get_digits()

#dunno what this is either
if __name__ == "__main__":
    main()
