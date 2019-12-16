# Put your code here
fName = input('Enter the name of the first file: ')
sName = input('Enter the name of the second file: ')

f = open(fName + '.txt', 'w')

f.write(" To be, or not to be: that is the question:"+"\n"
" Whether 'tis nobler in the mind to suffer"+"\n"
" The slings and arrows of outrageous fortune,"+"\n"
" Or to take arms against a sea of troubles,"+"\n"
" And by opposing end them? To die: to sleep;")

f.close()

f = open(fName + '.txt', 'r')
g = open(sName + '.txt', 'w')

count = 1

for line in f:
    g.write("\t" + str(count) + '>' + line)
    count +=1

g.close()


    
