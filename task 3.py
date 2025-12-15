A = float(input("Input: "))
intpart = int(A)
fracpart = round(A - intpart, 2)
intfrac = intpart/100
fracint = fracpart*100
print(intfrac, ",", round(fracint))
print(round(fracint) + intfrac)