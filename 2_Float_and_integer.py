Three, pi = 3, 3.14

#Checking the Type of Three
print("Type of {} is {}.".format(Three, type(Three)))

print("Type of {} is {}.".format(pi, type(pi)))

pi_Numerator, pi_Denominator = 22, 7

# // operation gives the decimal value of float eg: 2.14 to 2.
pi_Floor_Value = pi_Numerator//pi_Denominator

print(pi_Floor_Value)

Number, Power = 2, 10
Twotothepowerten = Number**Power

print(Twotothepowerten)

Negitive_Number = -4
"""abs function represents or returns the positive value of negitive
number"""
print("Absolute value of {} is {}.".format(Negitive_Number,
                                           abs(Negitive_Number)))

numberOfTypeString_1, numberOfTypeString_2 = "3", "7"

#Integer conversion.
stringToNumber_1, stringToNumber_2 = int(numberOfTypeString_1), int(numberOfTypeString_2)

print("Addition of {} and {} is {}."
      .format(stringToNumber_1,
              stringToNumber_2,
              stringToNumber_1 + stringToNumber_2))

floatString_1, floatString_2 = "1.21", "2.31"

#Float conversion.
stringToFloat_1 = float(floatString_1)
stringToFloat_2 = float(floatString_2)

print("Addition of {} and {} is {}".format(stringToFloat_1,
                                           stringToFloat_2,
                                           stringToFloat_1 +
                                           stringToFloat_2))
