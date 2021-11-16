import LA
from math import sqrt

from LA import inner_product, p_Norm


def stable_gram_schmidt(matrix_a):
    """Creating a vector and inner_product with LA.py

    Using a ncols and nrows to help the function create a product and pvector.

    Args:
        product: Inner product from the function LA.
        pvector: scalar vector multiplication from the function LA.

    Returns:
       It gives us the columns and rows of the function. 
    """
    ncols = len(matrix_a)
    nrows = len(matrix_a[0])
    V = []
    for col in range(ncols):
        i = ncols - col - 1
        Vcol = matrix_a[col]
        while(i < (ncols - 1)):
            Q = ncols - i
            Q = Q - 1
            product = LA.inner_product(matrix_a[col], V[col - Q])
            pvector = LA.scalar_vec_multi(product, V[col - Q])

            for j in range(nrows):
                Vcol[j] = Vcol[j] - pvector[j]
            i = i + 1
        p_Norm = LA.p_Norm(Vcol)
        Vcol = LA.scalar_vec_multi((1/p_Norm), Vcol)
        V.append(Vcol)
    
    R = [[0 for i in range(nrows)] for i in range(ncols)]
    for i in range(ncols):
        for i in range(nrows):
            if j > i:
                R[i][j] = 0
            elif i > j:
                R[i][j] = V[j][ncols - i - 1]
            else:
                R[i][j] = inner_product(matrix_a[i], V[j])
    
    return[V,R]
    #print(nrows,ncols)



def orthonormal_vectors(matrix_a):
    """Finding length of the matrix with rows and columns.

    Using a ncols and col to help the function with columns.

    Args:
        product: Inner product from the function LA.
        pvector: scalar vector multiplication from the function LA.

    Returns:
       It gives us the columns of the function. 
    """
    ncols = len(matrix_a)
    nrows = len(matrix_a[0])
    V = []
    for col in range(ncols):
        i = ncols - col - 1
        Vcol = matrix_a[col]

        while(i < (ncols - 1)):
            Q = ncols - i
            Q = Q - 1

            product = LA.inner_product(matrix_a[col], V[col - Q])
            pvector = LA.scalar_vec_multi(product, V[col - Q])
            for j in range(nrows):
                Vcol[j] = Vcol[j] - pvector[j].real
            i = i + 1

        p_Norm = LA.p_Norm(Vcol)

        Vcol = LA.scalar_vec_multi((1/p_Norm), Vcol)
        V.append(Vcol)
    
    return[V]

def householder_QR(matrix_a):
    """Using the householder QR to find the function

    We get the final result of the householder QR function to run. 

    Args:
        Qmat: Finding the range in the Qmat.
        Qlist: We use this list to put out the numbers.

    Returns:
       It gives us the householder QR that we need to run the function. 
    """
    ncols = len(matrix_a)
    nrows = len(matrix_a[0])

    A = matrix_a
    R = matrix_a

    Qlist = []

    Qmat = [[0 for element in range(ncols)] for element in range(ncols)]
    for i in range(len(Qmat)):
        Qmat[i][i] = 1
    
    for k in range(ncols-1):
        A1_norm = LA.p_Norm(A[0])

        I = [[0 for element in range(ncols-k)] for element in range(ncols-k)]
        for i in range(len(I)):
            I[i][i] = 1
        
        b1 = LA.scalar_vec_multi(A1_norm, I[0])

        if A[0][0] >= 0:
            sign = 1
        else:
            sign = -1

        #print(k,b1)
        vk = LA.add_vectors(LA.scalar_vec_multi(sign,A[0][k:]),b1)

        ipv = LA.inner_product(vk,vk).real

        Fk = [[]]
        for i in range(ncols-k):
            for j in range(nrows-k):
                #print(I[i][j],vk[i])
                Fk[i].append(I[i][j] - 2*vk[i]*vk[j]/ipv)
            if i < ncols-1:
                Fk.append([])

        Qk = [[0 for element in range(ncols)] for element in range(ncols)]
        for i in range(k):
            Qk[i][i] = 1
        
        for i in range(k,ncols):
            for j in range(k,nrows):
                #print(k,i,j,i-k,j-k)
                Qk[i][j] = Fk[i-k][j-k]
        
        #print(k,Qk)
        Qlist.append(Qk)

        Qmat = LA.mat_mat_multi(Qmat,Qk)
        A = LA.mat_mat_multi(Qk,A)

    R = A

    return Qmat, R

#householder_QR([[1,0,0],[0,1,0],[0,0,1]])
Q2,R2 = householder_QR([[1,1,0],[1,0,1],[0,1,1]])
print(Q2)
print(R2)
