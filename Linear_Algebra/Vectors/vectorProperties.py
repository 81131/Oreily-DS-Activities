from typing import List
import math

Vector = List[float]

height_weight_age = [70,
                     170,
                     40]

grades = [95,
          80,
          75,
          62]


def add(vec1: Vector, vec2: Vector) -> Vector:
    """Adds corresponding elements"""

    assert len(vec1) == len(vec2), "Vectors should be same length to add"

    return [vec1_i + vec2_i for vec1_i, vec2_i in zip(vec1,vec2)]



def substract(vec1: Vector, vec2) -> Vector:
    """Substracts vector 1 from vector 2"""

    assert len(vec1) == len(vec2), "Vectors should be same length to substract"

    return [vec1_i - vec2_i for vec1_i, vec2_i in zip(vec1,vec2)]



def vector_sum(vectors: List[Vector]):
    """Sums all corresponding elements"""

    #Verify that vectors are not empty
    assert vectors, "No vectors found"
    
    #Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "Can not add different sized vectors"

    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

assert vector_sum([[1,2],[3,4],[5,6],[7,8]]) == [16,20]



def scalar_multiply(constant:float, vector: Vector) -> Vector:
    """Multiplies every element by the provided constant"""
    return[constant * vector_i for vector_i in vector]

assert scalar_multiply(2, [1,2,3]) == [2,4,6]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""

    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1,2],[3,4],[5,6]]) == [3,4]

def dot(vector1: Vector, vector2: Vector) -> Vector:
    """Computes vector1_1 * vector2_1 + ... +vector1_n * vector2_n"""
    assert len(vector1) == len(vector2), "Vectors must be same length in order to find the dot product"

    return sum(vec1_i * vec2_i for vec1_i, vec2_i in zip(vector1, vector2))

assert dot([1,2,3], [4,5,6]) == 32


def sum_of_squares(vec: Vector) -> float:
    """Returns vec_1 * vec_1 + ... + vec_n * vec_n"""
    return dot (vec, vec)

assert sum_of_squares([1,2,3]) == 14


def magnitude(vec: Vector) -> float:
    #Magnitude -> Displacement (Shortest distance between the given points)
    #Formula(Pythagorean Theroem) -> sqrt(v1^2 + v2^2 + v3^2 + ... + vn^2)
    """Returns the magnitude (length) of v"""

    return math.sqrt(sum_of_squares(vec))

assert magnitude([3,4]) == 5


def squared_distance(vector1: Vector, vector2: Vector) -> float:
    """Computes (vector1_1 - vector2_1)**2 + ... + (vector1_n - vector2_n) **2 """
    return sum_of_squares(substract(vector1, vector2))

def distance(vector1: Vector, vector2: Vector) -> float:
    """Computes the distance between vector1 and vector2"""
    return math.sqrt(squared_distance(vector1, vector2))
#OR
def distance(vector1: Vector, vector2: Vector) -> float:
    return magnitude(substract(vector1, vector2))


