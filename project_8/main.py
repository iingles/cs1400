"""
Isaac Ingles
CS1400
Fall 2019
Project 8: "Was Clinton Right?"
"""
import csv

def main():    
    #create a list of totals by the year
    totals = yearTotals(yearData('BLS_private.csv'))

    #get the job numbers
    jobNums = presJobs(totals)

    """
    Now that I have the jobs numbers, add them up according to party.
    The dictionary jobNums is structured as follows:
    <year> : [president, total jobs, party]

    I chose the year to be the key because it needs to be unique.
    """
    dems = int(0)
    reps = int(0)

    f = open('presidents.txt', 'w')
    f.write("{:<10}{:<20}{:<10}{:<20}\n".format('Year', 'President', 'Jobs', 'Party') ) 
    f.write("{:<10}{:<20}{:<10}{:<20}\n\n".format('____', '__________', '_____', '_____') ) 

    for key, value in jobNums.items():
        if(value != ''):
            if(value[2] == 'Democrat'):                
                dems += value[1]
            if(value[2] == 'Republican'):
                # print(value[0], value[2])            
                reps += value[1]
         
        f.write("{:<10}{:<20}{:<10}{:<20}\n".format(str(key), str(value[0]), str(value[1]), str(value[2]) ) )
     
    #Total at this point for the date range should be stored in dems, reps

    f.write("\nTotals:\n")
    f.write("{:<20}{:<20}\n".format('total: ', str(reps + dems)) )
    f.write("{:<20}{:<20}\n".format('Democrats: ', str(dems)) )
    f.write("{:<20}{:<20}\n".format('Republicans: ', str(reps)) )

    f.write("""
    \n\tFrom the numbers given in the CSV file, unless there is an error that I missed, 
    \nthe data given shows the opposite of what Clinton said.
    \nThe data is very confusing; with conflicting reports across various articles; 
    \neven the BLS data is difficult to interpret.  It seems as though it
    \ndepends on how 'employment' is defined and how it is used to gather the data.
    """)

    f.close()


def presJobs(totals):
    """
        #return a dictionary of presidents, years, party, and total jobs per year
    """

    #create a dictionary of the presidents, year range of their terms, and their parties since 1961
    presidents = {'John F. Kennedy':[1961,1963,'Democrat'], 'Lyndon B. Johnson': [1964,1969,'Democrat'],'Richard Nixon': [1969,1974, 'Republican'], 'Gerald Ford': [1974, 1977, 'Republican'], 'Jimmy Carter': [1977, 1981, 'Democrat'], 'Ronald Reagan': [1981, 1989, 'Republican'], 'George H.W. Bush': [1989, 1993, 'Republican'], 'Bill Clinton': [1993,2001, 'Democrat'], 'George W. Bush': [2001, 2009, 'Republican'], 'Barack Obama': [2009, 2017, 'Democrat']}
    
    #counter for the years
    year = 0

    #create an empty dictionary
    nums = {}

    for key, value in presidents.items():
        if(value != ''):
            start = value[0]
            end = value[1]
            #get a list of the years this pres was in office
            inOffice = dates(start, end)
            #compare the list vs. the pres admins
            for i in inOffice:
                #if the key exists in the totals dictionary
               
                if str(i) in totals:                    
                    nums[i] = [key, totals[str(i)], value[2] ]
    return nums
    

def dates(start, end):
    """
        Calculate the individual years in a given range of years
    """
    years = []
    count = start
    #subtract the years to get the number in between
    numyears = end - start
    #add the number of years to the start number and return
    for i in range(numyears + 1):
        years.append(count)
        count += 1
    return years

def yearData(inFile):
    """
        Separate the data in the CSV file into years, return the separated data  
    
    """

    #use Python's csv method
    with open(inFile) as theFile:
        csvReader = csv.reader(theFile, delimiter=',')

        #counter to keep track of each line
        line = 0

        #The dictionary to return     
        data = {}

        for row in csvReader:
            #I know that in this file, the desired information doesn't start until line 6
            if line <= 5:
                line += 1
            else:            
                #Make the year (element 0) the key and the rest of the row the values
                data[row[0]] = row[1:]      
                line +=1
    return data

def yearTotals(theDict):
    """
        Take in the years/values dictionary then add up and return a dictionary of the totals per year
    """    
    totals = {}
    for key,value in theDict.items():

        total = 0
        for v in value:
            #Check to make sure that there are no empty strings
            if(v != ''):
                total += int(v)            
        totals[key] = total

    return(totals)

if __name__ == "__main__":
    main()
