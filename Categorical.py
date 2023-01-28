#Generating a categorical distribution file
#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np

# import our Random class from python/Random.py file
sys.path.append(".")

# main function for our coin toss Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number], please manually change the probabilities in the Cate definition if needed" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 8888

    # default single coin-toss probability for each side
    prob1 = 0.2
    prob2 = 0.4
    prob3 = 0.6
    prob4 = 0.8

    # default number of coin tosses (per experiment)
    Ntoss = 100000

    # default number of experiments
    Nexp = 1

    # output file defaults
    doOutputFile = True

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-prob' in sys.argv:
        p = sys.argv.index('-prob')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            prob = ptemp
    if '-Ntoss' in sys.argv:
        p = sys.argv.index('-Ntoss')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Ntoss = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True
    OutputFileName = 'H0.txt'
    # class instance of our Random class using seed
    random = Random(seed)

    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        for e in range(0,Nexp):
            for t in range(0,Ntoss):
                outfile.write(str(random.Cate())+" ")
            outfile.write(" \n")
        outfile.close()
    else:
        for e in range(0,Nexp):
            for t in range(0,Ntoss):
                print(random.Cate(prob1,prob2,prob3,prob4,prob5), end=' ')
            print(" ")
