balance = 3926
annualInterestRate = 0.2

month = 12

a = (1 + annualInterestRate / 12)
Uo = balance

lowestPayment = (1 - a) * ( ( a ** month) * Uo) / (1 - a ** month)


t = -lowestPayment / (1 - a)
Un = (a ** 12) * (Uo - t) + t

print(lowestPayment)
print(Un)
print()

roundLowestPayment = round(lowestPayment, -1)

t = -roundLowestPayment / (1 - a)
Un = (a ** 12) * (Uo - t) + t
print(roundLowestPayment)
print(Un)
print()

if Un > 0:
    roundLowestPayment += 10

print("Lowest Payment: " + str(roundLowestPayment))
