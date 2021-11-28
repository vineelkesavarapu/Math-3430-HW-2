import LA
import QR_HW_7 as QR

def solve(R,d):
    """We are creating a matrix that is stored in a list of lists from HW 7. 
    Using a ncols and nrows as len(R) to help find length of the matrix.

    Args:
        tot+: This function is used to for eq_number.
        tot=: This function is used for col_number and eq_number.

    Returns:
       It gives us the eq_number and returns the total. 
    """

    ncols = len(R)
    nrows = len(R[0])

    x = [0 for i in range(ncols)]

    for i in range(nrows):
        tot = 0
        eq_number = -(i+1)

        for col_number in range(i):
            #print('col_number',col_number)

            tot += -R[col_number+1][eq_number]*x[col_number+1]
            #print(-R[col_number+1][eq_number]*x[col_number+1])

            #print(tot)
        #print('eq_num',eq_number)

        tot += d[eq_number]
        tot /= R[eq_number][eq_number]

        x[eq_number] = tot
    return x

def transpose(A):
    """We are using householders from QR to have a running function. 
    Using a ncols and nrows as len(A) to find the range in i.

    Args:
        ncols: This function is used to find the range At[j][i].
        nrows: This function is used to find A[i][j].

    Returns:
       It gives us a transpose function. 
    """

    ncols = len(A)
    nrows = len(A[0])

    At = [[0 for i in range(ncols)] for j in range(nrows)]

    for i in range(ncols):
        for j in range(nrows):
            At[j][i] = A[i][j]

    return At

b = [1,2,3]
Q,R = QR.householder_QR([[1,1,0],[1,0,1],[0,1,1]])

#print(transpose([[1,2,3],[5,6,7]]))

Qt = transpose(Q)

d = LA.mat_vec_multi(Qt,b)

x = solve(R,d)

#print(x)