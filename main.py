from qgates import *
import pdb
from time import sleep


clear()


print("There are two qubits: q1 and q2.\nThe probability amplitude of each qubit, upon measurement, collapses into one of the probable outcomes:\n|0> or |1>.\nSo, upon completion of program, or upon usage of gates that require measurement, the probabilities will collapse and the output will be displayed.\n")

q1 = input("Enter the quantum state of q1: (0 for |0>, and 1 for |1>) ")
q1 = ket(int(q1))

q2 = input("Enter the quantum state of q2: (0 for |0>, and 1 for |1>) ")
q2 = ket(int(q2))


def main(q1, q2):
    
    clear()
    
    reportq1(q1)
    reportq2(q2)
    
    print()
    g = input("Enter the gate you would like to apply: (h, x, y, z, cx, cy, cz) ") 
    q = input("Enter the qubit you'd like to apply it on (target qubit): (1, 2) ")
    print()

    if q == '1':
    
        if g == 'h':
            q1 = hadamart(q1)
        
        elif g == 'x':
            q1 = pauliX(q1)
        
        elif g == 'y':
            q1 = pauliY(q1)
        
        elif g == 'z':
            q1 = pauliZ(q1)
        
        elif g == 'cx':
            q1 = cx1(q2, q1)
        
        elif g == 'cy':
            q1 = cy1(q2, q1)
        
        elif g == 'cz':
            q1 = cz1(q2, q1)
        
        else:
            print("Try again!")
            sleep(2)
            main(q1, q2)
            quit()
        
        reportq1(q1)
        
        go_again = input("Would you like to add another gate? (Y/n) ")
        if go_again == 'Y' or go_again == 'y':
            main(q1, q2)
        else:
            measurementStatement(q1, q2)
    
    if q == '2':
    
        if g == 'h':
            q2 = hadamart(q2)
        
        elif g == 'x':
            q2 = pauliX(q2)
        
        elif g == 'y':
            q2 = pauliY(q2)
        
        elif g == 'z':
            q2 = pauliZ(q2)
        
        elif g == 'cx':
            q2 = cx2(q1, q2)
        
        elif g == 'cy':
            q2 = cy2(q1, q2)
        
        elif g == 'cz':
            q2 = cz2(q1, q2)
            
        else:
            print("Try again!")
            sleep(2)
            main(q1, q2)
            quit()
        
        reportq2(q2)
        
        go_again = input("Would you like to add another gate? (Y/n): ")
        if go_again == 'Y' or go_again == 'y':
            main(q1, q2)
        else:
            measurementStatement(q1, q2)


main(q1, q2)
