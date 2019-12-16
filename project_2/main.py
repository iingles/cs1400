"""
    Isaac Ingles
    CS 1400
    Project 2 -- Earthquake Energy Calculator

"""

richterInput = float(input('Enter the Richter Scale number: '))

# Apply the logorithmic formula to calculate the equivalent
# energy released in Joules: E = 10^(1.5 x R + 4.8) -- 'E' for 
# energy in Joules and 'R' for the richterInput
# rounded to 4 decimal places

eqJoules = round(float( (10) ** (1.5 * richterInput + 4.8) ), 4)

# 1 ton of TNT releases 4.184 x 10^9 Joules (4.184 gigajoules); 
# so 1 joule is approximately
# ( 1 / (4.184 x 10^9 ) )
# the strength of 1 ton of TNT, or 0.00000000024 tons of TNT
# rounded to 4 decimal places     

eqTNT = round(float( eqJoules / (4.184 * 10**9) ), 4)

print("Richter Scale Value: ", richterInput)
print("Equivalent Joules: ", eqJoules)
print("Equivalent tons of TNT: ", eqTNT)