import generating_Jij as gj
import numpy as np
import argparse
import time

def run_simulation(N, numSeeds, alg):
    if alg == "bm":
        nString = str(N) + "_" + str(numSeeds) + "bm.txt"
        with open(nString, "a") as f:
            start = time.time()
            f.write(str(N) + "-Dimensional System - Ground States (seed, configuration)")
            f.write("\n")
            for seed in range(0,numSeeds):
                Jij = gj.generateJij(N, seed=seed)
                bm = gj.biqMac(Jij)

                bmList = []
                for element in bm:
                    bmList.append(gj.binary_to_decimal(element))
                bmString = str(seed) + ": " + str(bmList)

                f.write(bmString)
                f.write("\n")


            end = time.time()

            f.write("Computational time: " + str(end-start) + "s")
            f.write("\n")
            f.write("\n")
    if alg == "ex":
        nString = str(N) + "_" + str(numSeeds) + "ex.txt"
        with open(nString, "a") as f:
            start = time.time()
            f.write(str(N) + "-Dimensional System - Ground States (seed, configuration)")
            f.write("\n")
            for seed in range(0,numSeeds):
                Jij = gj.generateJij(N, seed=seed)
                bm = gj.biqMac(Jij)

                bmList = []
                for element in bm:
                    bmList.append(gj.binary_to_decimal(element))
                bmString = str(seed) + ": " + str(bmList)

                f.write(bmString)
                f.write("\n")


            end = time.time()

            f.write("Computational time: " + str(end-start) + "s")
            f.write("\n")
            f.write("\n")
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Jij ground state simulation")
    parser.add_argument("-N", type=int, required=True, help="System size")
    parser.add_argument("-numSeeds", type=int, required=True, help="Number of seeds for random generation")
    parser.add_argument("-alg", type=str, required=True, help="bm: biqMac, ex: Exhaustive")
    
    args = parser.parse_args()
    
    # Call main function with arguments
    run_simulation(args.N, args.numSeeds, args.alg)

