#!/usr/bin/python3

def upc(upc):

    while len(upc) != 11: # If the upc code is incomplete append zeros to the start to make it 11 digits
        upc = "0" + upc

    step1 = int(upc[0]) + int(upc[2]) + int(upc[4]) + int(upc[6]) + int(upc[8]) + int(upc[10])# Summing the numbers at odd positions, starting at 0 because python is the big gay

    step2 = int(step1) * 3 # Multiplying by 3

    step3a = int(upc[1]) + int(upc[3]) + int(upc[5]) + int(upc[7]) + int(upc[9]) # Summing the numbers at even positions

    step3b = int(step2) + int(step3a) # Adding step3a to step2

    M = int(step3b) % 10 # Obtaining the remainder of step3b / 10

    if M == 0:
        return upc + str(M) # If the remainder is 0 that is our check digit
    
    checkDigit = 10 - M # If not then the check digit is 10 minus the remainder

    return upc + str(checkDigit) # Return the full upc