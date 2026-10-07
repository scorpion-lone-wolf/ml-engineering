import numpy as np

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
total_element = dense_matrix.size
non_zero_elements = np.count_nonzero(dense_matrix)
zero_elements = total_element - non_zero_elements
# fraction of zero elements from the total number of elements
zero_fraction = zero_elements / total_element

print("Shape :", dense_matrix_shape)
print("Total element :", total_element)
print("Non-zero elements :", non_zero_elements)
print("Zero elements :", zero_elements)
print("Fraction of element that are zero :", zero_fraction)
