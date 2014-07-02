import math
#import numpy as np


def rounding(x, base=5):
    return int(base * round(float(x)/base))


def get_cost():
    cost = float(input("How much does your item cost (dollars.cents)? $"))

    #check for sensible cost
    dec_part,int_part = math.modf(100*cost)
    while dec_part != 0:
        cost =  float(input("We only go as low as cents! Please enter a valid cost: $"))
        dec_part,int_part = math.modf(100*cost)
    if (100*cost)%5 != 0.0:
        cost = rounding(100*cost)/100.0
        print "Your cost is rounded to $%.2f." % cost

    return cost


def get_payment():
    pay = float(input("How much money do you give? $"))

    #check for sensible pay
    dec_part,int_part = math.modf(100*pay)
    while (dec_part != 0) or ((100*pay)%5 != 0.0):
        if (dec_part != 0):
            pay =  float(input("We only go as low as cents! Please give a valid amount: $"))
            dec_part,int_part = math.modf(100*pay)
        if (100*pay)%5 != 0.0:
            pay =  float(input("We can only accept 5c denominations! Please give a valid amount: $"))
            dec_part,int_part = math.modf(100*pay)

    return pay


#TO DO: make the user input currencies, return sorted array of the user's inputs
#TO DO: add - allow the user to modify the default AUD settings
def get_denoms():
    choice = str(raw_input("Do you want to make your own denominations (y/n)? "))

    while (choice != "y") and (choice != "n"):
        choice = str(raw_input("Please enter 'y' or 'n': do you want to make your own denominations? "))

    if choice == "y":
        #for now
        return [50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05]
    elif choice == "n":
        return [50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05]


def calculate_change(amount,denoms):
    """Calculate denominations needed to give for the amount.

       amount = the amount of money needed
       denoms = vector of denominations for currency."""
    
    changes = [0]*len(denoms)
    for k in range(len(denoms)):
        least_denom = denoms[-1]

        #this line to avoid floating point errors: round to nearest least denom
        amount = least_denom * round(amount/least_denom)

        changes[k] = amount//denoms[k]
        amount = amount - denoms[k]*changes[k]

    return changes

     
#not sure what the purpose of main() is
def main():
    denom_vector = get_denoms()
    due = get_cost()
    paid = get_payment()

    while due > paid:
        print "You still owe $%.2f. Please give more money." % (due - paid)
        more_paid = get_payment()
        paid += more_paid

    change = paid - due

    print "Total due: $%.2f." % due
    print "Total paid: $%.2f." % paid
    print "Change due: $%.2f." % change

    change_vector = calculate_change(change, denom_vector)

    print "Change given:"
    for k in range(len(denom_vector)):
        if int(change_vector[k]) != 0:
            print "$%.2f's due: %d" % (denom_vector[k], int(change_vector[k]))


#dunno what this is either
if __name__ == "__main__":
    main()
