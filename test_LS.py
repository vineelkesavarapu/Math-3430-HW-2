import LS
import LA
import QR

b = [1,2,3]
Q,R = QR.householder_QR([[1,1,0],[1,0,1],[0,1,1]])

#print(transpose([[1,2,3],[5,6,7]]))

Qt = LS.transpose(Q)

d = LA.mat_vec_multi(Qt,b)

x = LS.solve(R,d)

print(x)