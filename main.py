from qgates import *
import pdb


clear()


print("There are two qubits: q1 and q2.")

q1 = input("Enter the quantum state of q1: (0 for ket|0>, and 1 for ket|1>) ")
q1 = ket(int(q1))

q2 = input("Enter the quantum state of q2: (0 for ket|0>, and 1 for ket|1>) ")
q2 = ket(int(q2))

    
def main(q1, q2):

    g = input("Enter the gate you would like to apply: (h, x, y, z, cx, cy, cz): ") #have yet to add controlled gates
    q = input("Enter the qubit you'd like to apply it on: (1, 2): ")
    print()
    
    if q == '1':
    
        if g == 'h':
            q1 = hadamart(q1)
        
        if g == 'x':
            q1 = pauliX(q1)
        
        if g == 'y':
            q1 = pauliY(q1)
        
        if g == 'z':
            q1 = pauliZ(q1)
        
        report(q1)
        
        go_again = input("Would you like to add another gate? (Y/n): ")
        if go_again == 'Y' or go_again == 'y':
            main(q1, q2)
        else:
            print("The measurement of q1 is: ",measureQubit(q1))
            print("The measurement of q2 is: ",measureQubit(q2))
    
    if q == '2':
    
        if g == 'h':
            q2 = hadamart(q2)
        
        if g == 'x':
            q2 = pauliX(q2)
        
        if g == 'y':
            q2 = pauliY(q2)
        
        if g == 'z':
            q2 = pauliZ(q2)
        
        report(q2)
        
        go_again = input("Would you like to add another gate? (Y/n): ")
        if go_again == 'Y' or go_again == 'y':
            main(q1, q2)
        else:
            print("The measurement of q1 is: ",measureQubit(q1))
            print("The measurement of q2 is: ",measureQubit(q2))


main(q1, q2)
