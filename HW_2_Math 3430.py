"""
Q1: What do we have?

A1: A scalar and vector that is stored. The names are scalar_a and vector_b. 

Q2: What do we want?

A2: Multiply the given vector and given scalar.

Q3: How will we get there?

A3: We will overright a vector with a scalar.
The corresponding components of scalar_a and vector_b. 


def scalar_multiplication(scalar_a,vector_b):

result = []

for element in vector_b:
  result.append(0)

for index in range(length(result)):
  result[index] = scalar_a * vector_b[index]

return result
"""

#Problem 1
def scalar_vec_multi(scalar,vector):
    result = [0 for element in vector]
    for index in range(len(result)):
      result[index] = scalar * vector[index]
    return result

print(scalar_vec_multi(2,[3,4]))

"""
Q1: What do we have?

A1: A scalar and matrix that is stored. The names are scalar_a and matrix_b. 

Q2: What do we want?

A2: Multiply the scalar and matrix.

Q3: How will we get there?

A3: We will multiply the columns of a scalar and matrix.
The corresponding components of scalar_a and matrix_b. 


def scalar_matrix_multiplication(scalar_a,matrix_b):

result = []

for row in matrix_b:
  result.append(scalar_multiplication(scalar_a,row))

return result
"""
    
#Problem 2
def scalar_mat_multi(scalar,matrix):
    result = []
    for vector in matrix:
        result.append(scalar_vec_multi(scalar,vector))
    return result

print(scalar_mat_multi(3, [[4, 5], [6, 7]]))

"""
Q1: What do we have?

A1: Two matrix's that are stored. The names are matrix_a and matrix_b. 

Q2: What do we want?

A2: Multiply the matrix inputs.

Q3: How will we get there?

A3: We will multiply the columns of the matrix's.
The corresponding components of matrix_a and matrix_b. 

def matrix_addition(matrix_a,matrix_b):

result = []

for index in range(length(matrix_a)):
  result.append(add_vectors(matrix_a[index],matrix_b[index]))

return result
"""

#Problem 3
def add_vector(vector_a,vector_b):
    return [vector_a[ind] + vector_b[ind] for ind in range(0, len(vector_a))]
    return result_vector


def add_matrices(matrix_a,matrix_b):
    result_matrix = []
    for index in range(0,len(matrix_a)):
        result_matrix.append(add_vector(matrix_a[index],matrix_b[index]))
    return result_matrix


print(add_matrices(matrix_a=[[1, 2],[3, 4]],matrix_b=[[-1, -2],[-3, -4]]))

"""
Q1: What do we have?

A1: A matrix and column stored. The names are matrix_a and column_b. 

Q2: What do we want?

A2: Multiply the matrix and column inputs.

Q3: How will we get there?

A3: We will multiply the rows of matrix and column.
The corresponding components of matrix_a and column_b. 

def matrix_vector_column(matrix_a,column_b)

result = []

for element in column_b:
  result.append(0)

for index in range(length(result)):
  result[index] = matrix_a[index] * column_b[index]
"""

#Problem 4
def mat_vec_multi(matrix,vector):
    result_vector = [0 for index in range(0,len(matrix[0]))]

    for index in range(0,len(matrix)):
        result_vector= add_vector(result_vector,scalar_vec_multi(vector[index],matrix[index]))
        
    return result_vector

print(mat_vec_multi(matrix=[[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]], vector=[2, 3, 5]))

"""
Q1: What do we have?

A1: The two matrix's are stored. The names are matrix_a and matrix_b. 

Q2: What do we want?

A2: Multiply the matrix inputs.

Q3: How will we get there?

A3: We will multiply the matrix columns.
The corresponding components of matrix_a and matrix_b. 


def matrix_matrix(matrix_a,matrix_b)

result = []

for element in column_b:
  result.append(0)

for index in range(length(result)):
  result[index] = matrix_a[index] * matrix_b[index]
"""

#Problem 5
def vec_vec_multi(vector_a,vector_b):
    return [vector_a[ind] * vector_b[ind] for ind in range(0, len(vector_a))]


def mat_mat_multi(matrix_a,matrix_b):

    result_matrix = []
    for vector in matrix_b:
        result_matrix.append(mat_vec_multi(matrix_a,vector))

    return result_matrix

print(mat_mat_multi(matrix_a=[[1, 1, 2], [3, 5, 8], [13, 21, 34]], matrix_b=[[-2, 3, -5], [7, -11, 13], [-17, 19, -23]]))
