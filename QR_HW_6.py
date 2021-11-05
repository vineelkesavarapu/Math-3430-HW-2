from math import sqrt
import LA_HW_4 as LA



def stable_gram_schmidt(matrix_a):
    """Putting a list of numbers to test stable gram-schmidt.

    We will test the stable gram-schmidt by making a list with
    Q,V,R and use functions from LA.py. 

    Args:
        row: We are using rows to put the number of gram-schmidt.
        column: We are using columns to put the number of gram-schmidt.

    Returns:
        It returns the stable version of gram-schmidt.
    """
    ncols = len(matrix_a)
    nrows = len(matrix_a[0])

    #print(nrows,ncols)

    Q: list = [[0 for i in range(nrows)] for i in range(ncols)]
    
    #Q: list = [[0,0,0],[0,0,0],[0,0,0]]
    V: list = [[0,0,0],[0,0,0],[0,0,0]]
    R: list = [[0,0,0],[0,0,0],[0,0,0]]
    r = 0
    scalar = 0

    n = len(matrix_a)

    #for column in range(len(matrix_a)):
    for col in range(n):
        V[col] = matrix_a[col]
    
    for col in range(n):
        #r = LA.inner_product(Q[row], V[column])
        R[col][col] = LA.p_Norm((V[col]))
        Q[col] = LA.scalar_vec_multi(1/R[col][col],V[col])

        for j in range(col+1,n):
            r = LA.inner_product(Q[col], V[j])
            R[j][col] = r.real
            scalar = LA.scalar_vec_multi(-R[j][col],Q[col])
            V[j] = LA.add_vectors(V[j], scalar)

    return Q

Q = stable_gram_schmidt([[1,1,0],[1,0,1],[0,1,1]])

print(Q)

Qtrue = [[1/sqrt(2),1/sqrt(2),0],
         [1/sqrt(6),-1/sqrt(6),2/sqrt(6)],
         [-1/sqrt(3),1/sqrt(3),1/sqrt(3)]]

print(Qtrue)


