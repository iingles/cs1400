"""
    Isaac Ingles
    CS1400
    Fall 2019

    Project 7 - Random Walk
"""
import statistics as stat
from random import seed, choice
from math import hypot
from turtle import *

#Turtle objects:
pa = Turtle()
mima = Turtle()
reg = Turtle()

pa.color('red')
mima.color('blue')
reg.color('green')


def set_seed(value):
    """ This function is used to set the seed for testing.
    When testing, this function needs to be called BEFORE main is called
    or any of function that uses random numbers.
    """
    seed(value)


def main():
    numSteps = int(input("enter the number of steps: "))
    numTrials = int(input("enter the number of trials: "))

    paDist = []
    mimaDist = []
    regDist = []

    for i in range(numTrials):

        paWalk = walk(numSteps,'pa')
        mimaWalk = walk(numSteps,'mima')
        regWalk = walk(numSteps,'reg')

        paDist.append(abs(paWalk[0]) + abs(paWalk[1]))
        mimaDist.append(abs(mimaWalk[0]) + abs(mimaWalk[1]))
        regDist.append(abs(regWalk[0]) + abs(regWalk[1]))

        pa.up()
        mima.up()
        reg.up()

        pa.goto(walk(100, 'pa'))
        mima.goto(walk(100, 'mima'))
        reg.goto(walk(100, 'reg'))

        pa.dot()
        mima.dot()
        reg.dot()

    #Once again, there is probably a more efficeint way to handle this output
    #CV is the ratio of the average and the standard deviation
    print("Pa random walk of ", numSteps)
    print("Mean: ", avg(paDist))
    print("Max: ", max(paDist))
    print("Min: ", min(paDist))
    print("CV: ", ( avg(paDist)/stat.stdev(paDist) ) )

    print("Mima random walk of ", numSteps)
    print("Mean: ", avg(mimaDist))
    print("Max: ", max(mimaDist))
    print("Min: ", min(mimaDist))
    print("CV: ", ( avg(paDist)/stat.stdev(paDist) ) )

    print("Reg random walk of ", numSteps)
    print("Mean: ", avg(regDist))
    print("Max: ", max(regDist))
    print("Min: ", min(regDist))
    print("CV: ", ( avg(paDist)/stat.stdev(paDist) ) )


def walk(num_steps, walker):
    x = 0
    y = 0
    direction = ''

    #Pick a random direction and step that way "number" times
    for i in range(num_steps):
        direction = choice(['north','south','east','west'])
        if direction == 'north':
            y += 1
        elif direction == 'south':
            y -= 1
        elif direction == 'east':
            x += 1
        else: #West is all that's left
            x -= 1
        #Conditions for each walk type besides pa (default)
        if walker == 'mima':
            if direction == 'south':
                y -= 1
        if walker == 'reg':
            if direction == 'north' or direction == 'south':
                #go east or west the same number instead of n or s; set y back to 0
                x += y
                y = 0

    #return the x,y coordinates
    # pass
    return (x,y)

def avg(inValues):
    
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

if __name__ == "__main__":
    set_seed(20190101)
    main()

input("press any key to continue...")