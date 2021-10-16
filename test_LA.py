import LA
import pytest

#test variables
vector_1 = [1, 2, 3]
vector_2 = [2, 4, 1]
vector_3 = [4, 5, 6]

scalar_1 = 4
scalar_2 = 3
scalar_3 = 2

matrix_1 = [[2, 4, 6],[3, 5, 7], [4, 6, 8]]
matrix_2 = [[3, 6, 9],[4, 7, 10], [5, 8, 11]]
matrix_3 = [[4, 8, 12],[5, 9, 13], [6, 10, 14]]



def test_add_vectors():
    #vector_1 = [1, 2, 3]
    #vector_2 = [2, 4, 1]
    assert LA.add_vectors(vector_1, vector_2) == [3, 6, 4]
    #vector_2 = [2, 4, 1]
    #vector_3 = [4, 5, 6]
    assert LA.add_vectors(vector_2, vector_3) == [6, 9, 7]

def test_scalar_vec_multi():
    #vector_1 = [1, 2, 3]
    #scalar_1 = 4
    assert LA.scalar_vec_multi(scalar_1, vector_1) == [4, 8, 12]
    #vector_2 = [2, 4, 1]
    #scalar_2 = 3
    assert LA.scalar_vec_multi(scalar_2, vector_2) == [6, 12, 3]
    #vector_3 = [4, 5, 6]
    #scalar_3 = 2
    assert LA.scalar_vec_multi(scalar_3, vector_3) == [8, 10, 12]

def test_scalar_mat_multi():
    #scalar_1 = 4
    #matrix_1 = [[2, 4, 6],[3, 5, 7], [4, 6, 8]]
    assert LA.scalar_mat_multi(scalar_1, matrix_1) == [[8, 16, 24], [12, 20, 28], [16, 24, 32]]
    #scalar_2 = 3
    #matrix_2 = [[3, 6, 9],[4, 7, 10], [5, 8, 11]]
    assert LA.scalar_mat_multi(scalar_2, matrix_2) == [[9, 18, 27], [12, 21, 30], [15, 24, 33]]
    #scalar_2 = 2
    #matrix_2 = [[4, 8, 12],[5, 9, 13], [6, 10, 14]]
    assert LA.scalar_mat_multi(scalar_3, matrix_3) == [[8, 16, 24], [10, 18, 26], [12, 20, 28]]

def test_add_matrices():
    #matrix_1 = [[2, 4, 6],[3, 5, 7], [4, 6, 8]]
    #matrix_2 = [[3, 6, 9],[4, 7, 10], [5, 8, 11]]
    assert LA.add_matricies(matrix_1, matrix_2) == [[5, 10, 15], [7, 12, 17], [9, 14, 19]]
    #matrix_2 = [[3, 6, 9],[4, 7, 10], [5, 8, 11]]
    #matrix_3 = [[4, 8, 12],[5, 9, 13], [6, 10, 14]]
    assert LA.add_matricies(matrix_2, matrix_3) == [[7, 14, 21], [9, 16, 23], [11, 18, 25]]

def test_mat_vec_multi():
    assert LA.mat_vec_multi(matrix_1, vector_1) == [20, 32, 44]
    assert LA.mat_vec_multi(matrix_2, vector_2) == [27, 48, 69]
    assert LA.mat_vec_multi(matrix_3, vector_3) == [77, 137, 197]

def test_mat_mat_multi():
    assert LA.mat_mat_multi(matrix_1, matrix_2) == [[60, 96, 132], [69, 111, 153], [78, 126, 174]]
    assert LA.mat_mat_multi(matrix_2, matrix_3) == [[104, 176, 248], [116, 197, 278], [128, 218, 308]]
