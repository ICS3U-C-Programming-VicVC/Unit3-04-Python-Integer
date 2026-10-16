#!/usr/bin/env python3
# Created By: Victor Victor-Calixte
# Date: 09/16/26
# This program identifies  whether the input integer is positive, negative, or zero.


def main():

    # Get the inter from the user
    Input_number = int(input("Please enter an integer: "))

    # First check if the number is a positive
    if Input_number > 0:

    # If it's positive, then tell the user that their number is positive

        print("The number: ({}) is positive!".format(Input_number))

    # If it's positive, then tell the user that their number is positive

    elif Input_number < 0:
        print("The number: ({}) is negative!".format(Input_number))

    else:

        print("The number: ({}) is zero!".format(Input_number))
        


if __name__ == "__main__":
    main()
