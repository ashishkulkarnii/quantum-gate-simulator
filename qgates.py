import numpy as np
from math import *
import cmath as c
from random import random
from os import system, name 


def clear(): 
    if name == 'nt': 
        _ = system('cls') 


def report(q):
    print("The vector representation of q1 is: {}\nThe chances of |0> are {}% and the chances of |1> are {}%.\n".format(*q))


def ket(n):
    if n == 0:
        chanceket1 = 0
        chanceket0 = 100
        return [[[1], [0]], chanceket0, chanceket1]
    elif n == 1:
        chanceket0 = 0
        chanceket1 = 100
        return [[[0], [1]], chanceket0, chanceket1]


#all arguments are lists of the form [<vetor representation of qubit>, <chance of ket(0)>, <chance of ket(1)>]


def hadamart(k):
    h = [[1/sqrt(2), 1/sqrt(2)], [1/sqrt(2), -1/sqrt(2)]]
    output = np.dot(h, k[0]).tolist()
    chanceket0 = output[0][0] * output[0][0] * 100
    chanceket1 = output[1][0] * output[1][0] * 100
    return [output, chanceket0, chanceket1]


def pauliX(k):
    k[0][0], k[0][1] = k[0][1], k[0][0]
    k[1], k[2] = k[2], k[1]
    return k

def pauliY(k):
    output = np.dot([[0, complex(0,-1)],[complex(0,1), 0]], k[0]).tolist()
    print(output)
    chanceket0 = abs(output[0][0] * output[0][0] * 100)
    chanceket1 = abs(output[1][0] * output[1][0] * 100)
    return [output, chanceket0.real, chanceket1.real]


def pauliZ(k):
    z = [[1, 0], [0, -1]]
    output = np.dot(z, k[0]).tolist()
    print(output)   
    chanceket0 = abs(output[0][0] * output[0][0] * 100)
    chanceket1 = abs(output[1][0] * output[1][0] * 100)
    return [output, chanceket0.real, chanceket1.real]


def cx(control, target):
    if control[2] != 0:
        print("{}% chance of {}".format(control[1], target))
        print("{}% chance of {}".format(control[2], pauliX(target)))
    else:
        output = target
        return output


def cy(control, target):
    if control[2] != 0:
        print("{}% chance of {}".format(control[1], target))
        print("{}% chance of {}".format(control[2], pauliY(target)))
    else:
        output = target
        return output


def cz(control, target):
    if control[2] != 0:
        print("{}% chance of {}".format(control[1], target))
        print("{}% chance of {}".format(control[2], pauliZ(target)))
    else:
        output = target
        return output


def measureQubit(k):
    m = 100 * random()
    p0 = k[1]
    if m < p0:
        return "|0>"
    else:
        return "|1>"
