# Put your code here
first = input("enter the first file: ")
second = input("enter the second file: ")


f = open(first, 'w')

f.close()
g = open(second, 'w')

f.close()

f = open(first, 'r')
g = open(second, 'r')

for i in f:
    for j in g:
        if (i == j):
            print('Yes\n', i, '\n', j)
        else: 
            print('No')
            
