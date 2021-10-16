# Problem #0

def add_vectors(vector_a: list[float],
                vector_b: list[float]) -> list[float]:
    """Adds the two input vectors.

    Creates a result vector stored as a list of 0's the same length as the input 
    then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result. 

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.

    Returns:
       The sum of the input vectors stored as a list. 
    """ 
    result: list[float] = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result

print(add_vectors(vector_a=[1,2,3],vector_b=[4,5,6]))


#Problem 1

def scalar_vec_multi(scalar: int,vector: list[float]) -> list[float]:
    """Multiply the given scalar and vector of the function.

    We will overright a vector with a scalar.
    The corresponding components of scalar and vector. 

    Args:
        scalar: It is called scalar and stored as a list.
        vector: A vector stored as a list.

    Returns:
        The multiplication of a scalar and vector stored as the list of elements.
    """
    result: list[float] = [0 for element in range(len(vector))]
    for index in range(len(result)):
      result[index] = scalar * vector[index]
    return result

print(scalar_vec_multi(2,[3,4]))


#Problem 2

def scalar_mat_multi(scalar: int,matrix: list[float]) -> list:
    """Multiply the given scalar and matrix of the function.

    We will multiply the columns of a scalar and matrix.
    The corresponding components of scalar and matrix. 

    Args:
        scalar: It is called scalar and stored as a list.
        matrix: A matrix stored as a list.

    Returns:
        The scalar and matrix will multiply the columns of scalar and matrix.
    """
    result: list[float] = []
    for vector in matrix:
        result.append(scalar_vec_multi(scalar,vector))
    return result

print(scalar_mat_multi(3, [[4, 5], [6, 7]]))

#Problem 3


def add_matrices(matrix_a: list[float],matrix_b: list[float]) -> list[float]:
    """Add the two indexes of the matrix in the function.

    We will multiply the columns of the matrix's.
    The corresponding components of matrix_a and matrix_b. 


    Args:
        matrix_a: matrix_a is stored as a list.
        matrix_b: Like matrix_a, matrix_b is stored as a list.

    Returns:
        The sum of the matricies are added in the list.
    """
    result_matrix: list[float] = []
    for index in range(0,len(matrix_a)):
        result_matrix.append(add_vectors(matrix_a[index],matrix_b[index]))
    return result_matrix

print(add_matrices(matrix_a=[[1, 2],[3, 4]],matrix_b=[[-1, -2],[-3, -4]]))

#Problem 4
def mat_vec_multi(matrix: list[float],vector: list[float]) -> list[float]:
    """Multiply the given matrix and vector of the function.

    We will multiply the rows of matrix and vector.
    The corresponding components of matrix and vector. 

    Args:
        matrix: matrix is stored as a list of lists.
        vector: A vector is stored as a list.

    Returns:
        The matrix and vector will add the columns and create result vectors of 0's.
    """
    result_vector: list[float] = [0 for index in range(0,len(matrix[0]))]

    for index in range(0,len(matrix)):
        result_vector= add_vectors(result_vector,scalar_vec_multi(vector[index],matrix[index]))
        
    return result_vector

print(mat_vec_multi(matrix=[[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]], vector=[2, 3, 5]))

#Problem 5
def vec_vec_multi(vector_a,vector_b):
    """Multiply the given vectors of the function.

    We will multiply the vector columns.
    The corresponding components of vector_a and vector_b. 

    Args:
        vector_a: vector_a is stored as a list.
        vector_b: Like vector_a, vector_b is stored as a list.

    Returns:
        The vectors will multiply the columns of the vectors.
    """
    return [vector_a[ind] * vector_b[ind] for ind in range(0, len(vector_a))]


def mat_mat_multi(matrix_a: list[float],matrix_b: list[float]):
    """Multiply the given matricies of the function.

    Args:
        matrix_a: matrix_a is stored as a .
        matrix_b: Like matrix_a, matrix_b is stored as a list.

    Returns:
        The matricies will multiply the columns and rows of the matricies.
    """
    result_matrix: list[list] = []
    for vector in matrix_b:
        result_matrix.append(mat_vec_multi(matrix_a,vector))

    return result_matrix

print(mat_mat_multi(matrix_a=[[1, 1, 2], [3, 5, 8], [13, 21, 34]], matrix_b=[[-2, 3, -5], [7, -11, 13], [-17, 19, -23]]))
