# main function for this Python code
import sys
import numpy as np
import matplotlib.pyplot as plt
if __name__ == "__main__":
    tru = []
    # create some random data
    file1 = open('H0.txt', 'r') # Opens up a text file
    trufile = file1.read().split() # Split the data into a readable format for the program
    for i in range(0,Ntoss): # Add the data from the text file to an array
        C = int(trufile[i])
        tru.append(C)
    file1.close()
    # create histogram of our data
    n, bins, patches = plt.hist(tru, 10, density=True, facecolor='g', alpha=0.75)

    # plot formating options
    plt.xlabel('x')
    plt.ylabel('Probability')
    plt.title('Categorical random distribution')
    plt.grid(True)

    # show figure (program only ends once closed
    plt.show()
