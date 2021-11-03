import LA_HW_4 as LA

def unstable_gram_schmidt(matrix_a):
    """Putting a list of numbers to test unstable gram-schmidt.

    We will test the unstable gram-schmidt by making a list with
    Q,V,R and use functions from LA.py. 

    Args:
        row: We are using rows to put the number of gram-schmidt.
        column: We are using columns to put the number of gram-schmidt.

    Returns:
        It returns the unstable version of gram-schmidt.
    """
    Q: list = []
    V: list = [[0,0,0],[0,0,0],[0,0,0]]
    R: list = [[0,0,0],[0,0,0],[0,0,0]]
    r = 0
    scalar = 0

    for column in range(len(matrix_a)):
        V[column] = matrix_a[column]
        for row in range(0,column):
            r = LA.inner_product(Q[row], V[column])
            R[column][row] = r.real
            scalar = LA.scalar_vec_multi(-R[column][row], Q[row])
            V[column] = LA.add_vectors(V[column], scalar)
            
        R[column][column] = LA.p_Norm((V[column]))
        Q.append(LA.scalar_vec_multi(1/R[column][column],V[column]))
    return [Q,R]

Q,R = unstable_gram_schmidt([[1,1,0],[1,0,1],[0,1,1]])

#print(Q)
#print(R)


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
    Q: list = [[0,0,0],[0,0,0],[0,0,0]]
    V: list = [[0,0,0],[0,0,0],[0,0,0]]
    R: list = [[0,0,0],[0,0,0],[0,0,0]]
    r = 0
    scalar = 0

    n = len(matrix_a)

    for col in range(n):
        V[col] = matrix_a[col]
    
    for col in range(n):
        R[col][col] = LA.p_Norm((V[col]))
        Q[col] = LA.scalar_vec_multi(1/R[col][col],V[col])

        for j in range(col+1,n):
            r = LA.inner_product(Q[col], V[j])
            R[j][col] = r.real
            scalar = LA.scalar_vec_multi(-R[col][j],Q[col])
            V[j] = LA.add_vectors(V[j], scalar)

        return [Q,R]

Q1,R1 = unstable_gram_schmidt([[1,1,0],[1,0,1],[0,1,1]])
Q2,R2 = stable_gram_schmidt([[1,1,0],[1,0,1],[0,1,1]])
#print('----')
#print(R1)
#print()
#print(R2)
