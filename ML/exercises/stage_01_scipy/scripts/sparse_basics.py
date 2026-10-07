import numpy as np
from scipy.sparse import coo_array

dense_matrix = np.array(
    [
        [0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0],
        [0, 0, 0, 0, 3],
    ]
)
print("Dense matrix :\n", dense_matrix)

# * let's inspect the dense matrix
dense_matrix_shape = dense_matrix.shape
total_elements = dense_matrix.size
non_zero_elements = np.count_nonzero(dense_matrix)
zero_elements = total_elements - non_zero_elements
# fraction of zero elements from the total number of elements
zero_fraction = zero_elements / total_elements

print("Shape :", dense_matrix_shape)
print("Total elements :", total_elements)
print("Non-zero elements :", non_zero_elements)
print("Zero elements :", zero_elements)
print("Fraction of element that are zero :", zero_fraction)

# -----------------------------------------------------------------------------------------------------------------------------
data = np.array([5, 8, 3])
row = np.array([0, 2, 3])
col = np.array([2, 1, 4])

coo_matrix = coo_array(
    (data, (row, col)),  # values + coordinates
    shape=(4, 5),  # shape of the matrix
)

print("\n COO sparse array:")
print(coo_matrix)
print("COO shape :", coo_matrix.shape)
print("COO nnz(non-zero elements) :", coo_matrix.nnz)
print("COO data:", coo_matrix.data)
print("COO rows:", coo_matrix.row)
print("COO columns:", coo_matrix.col)

print("\nCOO converted back to dense matrix:")
print(coo_matrix.toarray())
