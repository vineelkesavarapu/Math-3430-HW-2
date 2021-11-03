import QR
import LA

from math import sqrt

#test variables
Q1,R1 = QR.unstable_gram_schmidt([[1,1,0],[1,0,1],[0,1,1]])
Q2,R2 = QR.stable_gram_schmidt([[1,1,0],[1,0,1],[0,1,1]])

Qtrue = [[1/sqrt(2),1/sqrt(2),0],
         [1/sqrt(6),-1/sqrt(6),2/sqrt(6)],
         [-1/sqrt(3),1/sqrt(3),1/sqrt(3)]]

print(Q1)
print(R1)
print('----')
print(Q2)
print(R2)