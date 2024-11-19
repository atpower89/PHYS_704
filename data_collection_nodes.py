import generating_Jij_nodes as gj
import numpy as np
import argparse
import time

def run_simulation(N, numSeeds):
    nString = str(N) + "_" + str(numSeeds) + "nodes.txt"
    with open(nString, "a") as f:
        start = time.time()
        for seed in range(0,numSeeds):
            Jij = gj.generateJij(N, seed=seed)
            bm = gj.biqMac(Jij)

            f.write(str(seed) + " " + str(bm))
            f.write("\n")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Jij ground state simulation")
    parser.add_argument("-numSeeds", type=int, required=True, help="Number of seeds for random generation")
    
    args = parser.parse_args()
    
    # Call main function with arguments
    for N in range(8,37):
        run_simulation(N, args.numSeeds)