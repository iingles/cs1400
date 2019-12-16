"""
Isaac Ingles
CS1400
Fall 2019
Project 5: The Stock Trader
"""

"""
NOTE:
I couldn't get stocks_data.csv to open; it kept telling me
that the file was corrupted -- but I did find stocks_data.txt
on Canvas and so I just decided to use that -- it likely has all 
of the same information.
"""

#for standard deviation
import math
import statistics

f = open('stocks_data.txt', 'r')

#Dictionary format - transaction: [company, price, date]
trades = []

for line in f:
    trades.append(line.split('\t'))    

trades.sort()
names = set()

msft = {}
aapl = {}
ibm = {}

#Grab the individual company names
#Set the dates of the trades to be the keys
for trade in trades:
    names.add(trade[0])
    
    if(trade[0] == 'MSFT'):
        msft[trade[1]] = float(trade[2][0:-2])
    if(trade[0] == 'IBM'):
        ibm[trade[1]] = float(trade[2][0:-2])
    if(trade[0] == 'AAPL'):
        aapl[trade[1]] = float(trade[2] [0:-2])


msft_max = max(msft.values())
ibm_max = max(ibm.values())
aapl_max = max(aapl.values())

msft_min = min(msft.values())
ibm_min = min(ibm.values())
aapl_min = min(aapl.values())

#Find which value corresponds to which key(the date of the trade)
def keysFromValues(theDict, theValue):
    theKey = ''

    for item in theDict.items():
        if(item[1] == theValue):
            theKey = item[0]
    return theKey

#Find the average price
def avgPrice(inValues):

    average = 0
    valuesTotal = 0

    #Looks like Python 3 doesn't support index() for dictionaries?
    valuesList = list(inValues)

    #find the index of the last value + 1 (index starts at 0)
    numValues = valuesList.index(valuesList[-1]) + 1

    #add the values
    for index, i in enumerate(inValues, 1):
        valuesTotal += i   

    average = valuesTotal/numValues

    return average


highPrices = [[msft_max,keysFromValues(msft, msft_max), "MSFT"], [aapl_max,keysFromValues(aapl, aapl_max), "AAPL" ], [ibm_max,keysFromValues(ibm, ibm_max), "IBM" ]]
lowPrices = [[msft_min,keysFromValues(msft, msft_min), "MSFT"], [aapl_min,keysFromValues(aapl, aapl_min), "AAPL" ], [ibm_min,keysFromValues(ibm, ibm_min), "IBM" ]]

high = max([ highPrices[0][0], highPrices[1][0], highPrices[2][0] ] )
low = min([ lowPrices[0][0], lowPrices[1][0], lowPrices[2][0] ] )

for j in highPrices:
    if(j[0] == high):
        highestPrice = j[2],j[0],j[1]

for k in lowPrices:
    if(k[0] == low):
       lowestPrice = k[2],k[0],k[1]


"""
    There is probably a much more elegant way of handling this output; such as "template"; but I couldn't
    get it to quite work and so I just used a hammer and did it the long way :-/

"""

output = open('stock_summary.txt', 'w')

output.write("MSFT\n-----\n")
output.write("\nMax: " + str(msft_max) + " " + str(keysFromValues(msft, msft_max)) )
output.write("\nMin: " + str(msft_min) + " " + str(keysFromValues(msft, msft_min)) )
output.write("\nAverage: " + str(avgPrice(msft.values()) ) )
output.write("\nStandard Deviation: " + str( statistics.stdev(msft.values())) )

output.write("\n\nAAPL\n-----\n")
output.write("\nMax: " + str(aapl_max) + " " + str(keysFromValues(aapl, aapl_max)) )
output.write("\nMin: " + str(aapl_min) + " " + str(keysFromValues(aapl, aapl_min)) )
output.write("\nAverage: " + str(avgPrice(aapl.values()) ) )
output.write("\nStandard Deviation: " + str( statistics.stdev(aapl.values())) )

output.write("\n\nIBM\n-----\n")
output.write("\nMax: " + str(ibm_max) + " " + str(keysFromValues(ibm, ibm_max)) )
output.write("\nMin: " + str(ibm_min) + " " + str(keysFromValues(ibm, ibm_min)) )
output.write("\nAverage: " + str(avgPrice(ibm.values()) ) )
output.write("\nStandard Deviation: " + str( statistics.stdev(ibm.values())) )
output.write("\n\nHighest Price: " + str(highestPrice[0] + " " + str(highestPrice[1]) + " " + str(highestPrice[2] )) )
output.write("\nLowest Price: " + str(lowestPrice[0]) + " " + str(lowestPrice[1]) + " " + str(lowestPrice[2]) )

output.close()