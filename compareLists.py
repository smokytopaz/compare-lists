import os.path
import numpy as np

def compare(file1, file2):

    files = [file1, file2]

    comp1 = makeList(files[0])
    comp2 = makeList(files[1])

    '''Uses numpy to compare elements from comp1 with comp2, if an element from
    comp1 exists anywhere in comp2 the result is True'''
    result = np.in1d(comp1, comp2)

    #Prints the element from comp1 followed by a message (1102 - Matches)    
    for x, i in enumerate(result):
        if (i == True):
            print('{} - MESSAGE'.format(comp1[x]))
        else:
            print('{} - MESSAGE'.format(comp1[x]))
                                                                                                

def makeList(file):
                                                                                  
    #Reads the file lines into a list and strips off the new-line character
    with open(file) as f:
        return([x.strip() for x in f.readlines() if x.strip() != ''])


compare('/path/to/file1', '/path/to/file2')
