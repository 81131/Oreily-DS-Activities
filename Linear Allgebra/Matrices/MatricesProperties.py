from typing import List
from typing import Tuple
from typing import Callable

Vector = List[float]
Matrix = List[List[float]]

A = [[1,2,3],
     [4,5,6]]
#A has 2 rows + 3 columns -> Shape = (2,3)




B = [[1,2],
     [3,4],
     [5,6]]
#B has 3 rows + 2 columns -> Shape = (3,2)


def shape(Matrix1:Matrix) -> Tuple[int, int]:
    """Returns (# of rows of A, # of columns of B)"""

    #Get the row count
    numOfRows = len(Matrix1)
    numOfCols = len(Matrix1[0]) if Matrix1 else 0
    return numOfRows, numOfCols

assert shape(A) == (2,3)



def get_row(Matrix1:Matrix, i:int) -> Vector:
    """Returns the ith row of the provided matrix"""
    return Matrix1[i]
assert(get_row(A, 0)) == [1,2,3]


def get_column(Matrix1: Matrix, j:int) -> Vector:
    """Returns the jth column of a matrix as a vector"""
    return [Matrix1_i[j] for Matrix1_i in Matrix1]
assert (get_column(A, 1)) == [2,5]

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int,int], float]) -> Matrix: #Callable[[int,int], float] means we are passing another function to the make matrix function.
    return [[entry_fn(i,j)
            for j in range(num_cols)]
            for i in range(num_rows)]

mat1 = make_matrix(3,3, lambda i,j: i*j)

def printMatrix(mat: Matrix) -> None:
    for vec in mat:
        print(*vec, "\n")
print("Matrix 1:")
printMatrix(mat1)
print("\n\n")

def identity_matrix(n: int) -> Matrix:
    """Returns the n*n identity matrix"""
    return make_matrix(n,n, lambda i,j: 1 if i==j else 0)

mat2 = identity_matrix(5)
print("Identity Matrix 1:")
printMatrix(mat2)

