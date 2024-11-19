import tfim
import numpy as np
import string

import branchboundV13
from branchboundV13 import BB

import time
           
def generateBasis(L, D=1, PBC=True, J=1.0):
    """
    generates a basis for a given instance
    """
    lattice = tfim.Lattice([L], PBC)
    N = lattice.N
    basis = tfim.IsingBasis(lattice)
    return basis

def generateJij(N,J=1.0,seed=0):
    """
    generates a Jij matrix for a given instance
    """
    Jij = tfim.Jij_instance(N,J,dist="bimodal",seed=seed,even=True)
    return Jij

def printBasis(basis):
    for b in range(basis.M):
        state = basis.spin_state(b)
        print(state)

def printStates(basis):
    for b in range(basis.M):
        state = basis.spin_state(b)
        print(state)

def findEnergies(basis, Jij):
    """
    calculates the energy of each spin configuration
    """
    energies = -tfim.JZZ_SK_ME(basis,Jij)
    return energies

def makeJij(G,N):
    """
    Turns Jij matrix from form built in tfim.py to standard Jij where J[i][j] is the bond between spins i and j
    """
    Jij = np.zeros((N,N))
    for j in range(N//2):
        for i in range(N):
            Jij[i][(i-j+N-1) % N] = Jij[(i-j+N-1) % N][i] = G[j][i]
    return Jij

def getSpins(energy_list,basis): 
    """
    returns the spin configurations of the ground states
    """
    indexlist = []
    minimum = min(energy_list)
    stateList = []
    for i in range(len(energy_list)):
        if energy_list[i] == minimum:
            indexlist.append(i)
    for i in range(0, basis.M):
        if i in indexlist:
            state = basis.spin_state(i)
            stateList.append(state)
    return stateList

def testConvert(Jij):
    """
    converts a Jij matrix into the form read by the Spin Glass Server
    """
    N = len(Jij[0])
    print("name: "+str(N)+"-dimensional system as an SGS test\n")
    for i in range(N):
        for j in range(i+1,len(Jij[0])):
            print(str(i+1)+" "+str(j+1)+" "+str(Jij[i][j]))

def exhaustive(Jij):
    """
    exhaustively calculates the groud states of a given Jij instance
    """
    newSet = set()
    N = len(Jij[0])
    basis = generateBasis(N)
    energies = findEnergies(basis,Jij)
    spins = getSpins(energies,basis)
    for i in range(len(spins)):
        for j in range(len(spins[0])):
            if spins[i][j] == -1:
                spins[i][j] = 0
        newSet.add(str(spins[i]))
    return newSet

def biqMac(Jij):
    """
    efficiently calculates the ground states of a given Jij instance
    """
    N = len(Jij[0])
    arr = makeJij(Jij, N)
    Q2 = np.array(arr)
    P2 = np.zeros(N)
    R2 = 0
    for i in range(N):
        for j in range(N):
            P2[i] += Q2[i][j]
            R2 += Q2[i][j]
    solver = BB(-2*Q2, 2*P2, -0.5*R2)
    return solver.solve()

def binary_to_decimal(array):
    """
    Converts an array of spins to its corresponding decimal value
    """
    array = array.translate(str.maketrans('', '', string.punctuation))
    array = array.replace(" ", "")
    
    binary = int(array, 2)

    return binary