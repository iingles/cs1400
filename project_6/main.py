"""
    Isaac Ingles
    CS 1400
    Fall 2019

    Project 6: Farmer John's Field

"""
import math

def main():
    #loop until a valid input is entered, or exit on empty string/enter
    while True:
        print("Enter the distance AB in feet or nothing (enter to exit): ")
        # Distance from A to B in feet
        distAB = input() 
        if(distAB == '' or distAB == 'exit'):
            print("Exit")
            exit()
        elif(distAB.isdigit()):
            distAB = float(distAB)
            break
        else:
            print("Please enter a number.")
            continue

    #Square feet in square
    sqFeet = squareArea(distAB)

    #Calculate the radius of a circle from the center of the square
    rad = circRadius(distAB)

    #Circle area (circle, in square feet)
    cArea = circArea(rad)

    #Shaded area - square area - area of the circle (in square feet)
    shArea = sqFeet - cArea
    
    #Number of bushels equal to 65 bushels per acre, times 4 for each circle
    numBush = sqFtToAcres(cArea * 4) * 65

    #Amount of water used (in inches) - 9 inches per acre * acres in circle area * 27,000 gallons in an acre-inch
    amtWater = 9 * sqFtToAcres(cArea * 4) * 27000

    #Price of water ( $1.50 per 1000 gallons )
    prWater =  (amtWater/1000) * 1.5

    #Income - price per bushel ($8.87) * number of bushels
    income = numBush * 8.87

    #Profit - income - price of water - price of new system ($35,000)
    profit = income - prWater - 35000

    # x4 because there are 4 circles
    print("Acres Watered: {0:.2f}".format( sqFtToAcres(cArea * 4) ) )
    print("Bushels produced: {0:.2f}".format( numBush ) )
    print("Area of shaded region: {0:.2f}".format( sqFtToAcres(shArea) ) )
    print("Net Profit: ${0:.2f}".format( profit,2 ))
 
    #Call main again
    main()

#return the area of a square (length * width)
def squareArea(abLength):
    area = float(abLength**2)

    return area

#radius of a circle inside of a square = 1/2 length of a side
def circRadius(AB):
    radius = AB/2 

    return radius

#return the area of a circle (pi * radius^2)
def circArea(rad):
    area = float( math.pi * (rad**2) )

    return area

#divide square feet by 43,560 to get acres
def sqFtToAcres(sqFeet):    
    acres = sqFeet/43650

    return acres

if __name__ == "__main__":
    main()
