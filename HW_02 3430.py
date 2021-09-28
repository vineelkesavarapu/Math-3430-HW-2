#Problem 1
def scalar_vec_multi(scalar,vector):
    result = [0 for element in vector]
    for index in range(len(result)):
      result[index] = scalar * vector[index]
    return result

print(scalar_vec_multi(2,[3,4]))


    
#Problem 2
def scalar_mat_multi(scalar,matrix):
    result = [0 for element in matrix]
    for index in range(len(result)):
      result[index] = scalar * vector[index]
    return result

print(scalar_mat_multi(3, [[4, 5], [6, 7]]))

#Problem 3
def add_matrices(matrix_A,matrix_B):
    result = [0 for element in matrix]
    for index in range(len(result)):
      result[index] = matrix_A[index] + matrix_B[index]
    return result

#Problem 4
def mat_vec_multi(matrix,vector):
    result = [0 for element in matrix]
    for index in range(len(result)):
      result[index] = matrix * vector
    return result

#Problem 5
def mat_com_multi(matrix_A,component):
    result = [0 for element in matrix]
    for index in range(len(result)):
      result[index] = matrix * component
    return result
    
