import generating_Jij as gj
import numpy as np
import argparse
import time

def run_simulation(N, numSeeds):
    nString = str(N) + "_" + str(numSeeds) + "times.txt"
    with open(nString, "a") as f:
        start = time.time()
        f.write(str(N) + "-Dimensional System - Ground States (seed, degeneracy, computation time)")
        f.write("\n")
        for seed in range(0,numSeeds):
            seedStart = time.time()
            Jij = gj.generateJij(N, seed=seed)
            bm = gj.biqMac(Jij)

            bmList = []
            counter = 0
            for element in bm:
                bmList.append(gj.binary_to_decimal(element))
                counter += 1
            seedEnd = time.time()
            countString = str(seed) + " " + str(counter) + " " + str(seedEnd-seedStart)

            f.write(countString)
            f.write("\n")

        f.write("\n")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Jij ground state simulation")
    parser.add_argument("-N", type=int, required=True, help="System size")
    parser.add_argument("-numSeeds", type=int, required=True, help="Number of seeds for random generation")
    
    args = parser.parse_args()
    
    # Call main function with arguments
    run_simulation(args.N, args.numSeeds)