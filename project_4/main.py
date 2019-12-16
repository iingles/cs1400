"""
Isaac Ingles
Project 4 - Rabbits, rabbits, rabbits
CS 1400
Fall 2019
"""

#Set initial conditions
adults = 1
month = 1
babies = 0
total = 1
beforeAdultsChange = 0

f = open('./rabbits.csv', 'w')
"""
    The expected output is:

    1, 1, 0, 1
    2, 1, 1, 2
    3, 2, 1, 3
    4, 3, 2, 5
    ...
   
    This is the Fibbonacci sequence;
    where the next number is the sum of the previous two. 
    
    The formula for this is: 

    f˅n = (f˅n - 1) + (f˅n - 2)

    where, in this case, n is the number of months passed
    and f is the number of rabbits.
"""

f.write("Month,Adults,Babies,Total\n")

#There are 500 cages; each holding 2 rabbits -- so the total capacity is 1000 rabbits.
while total <= 1000:
    f.write(str(month) + ',' +  str(adults) + ',' + str(babies) + ',' + str(total) + '\n')
    #increment the month after each output
    month += 1
    #Keep track of the adults before I set the new value so I can set babies to it
    beforeAdultsChange = adults
    #add the babies from the previous iteration to the pool of adults  
    adults += babies
    #set babies to the prior adult value (each pair produces another baby)
    babies = beforeAdultsChange   

    total = adults + babies

f.write("The cages will be full after " + str(month - 1) + " months.")
#make sure to close the file
f.close()

#Wait for user input before ending
input("Press Enter to continue...") 