import numpy as np
from scipy.sparse import coo_array

SECTION_WIDTH = 72


def print_section(title):
    print(f"\n{'=' * SECTION_WIDTH}")
    print(title)
    print("=" * SECTION_WIDTH)


def create_dense_matrix():
    return np.array(
        [
            [0, 0, 5, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 8, 0, 0, 0],
            [0, 0, 0, 0, 3],
        ]
    )


def inspect_dense_matrix(dense_matrix):
    print_section("1. DENSE NUMPY ARRAY")

    total_elements = dense_matrix.size
    non_zero_elements = np.count_nonzero(dense_matrix)
    zero_elements = total_elements - non_zero_elements
    zero_fraction = zero_elements / total_elements

    print("Matrix:")
    print(dense_matrix)
    print()
    print("Shape            :", dense_matrix.shape)
    print("Total elements   :", total_elements)
    print("Non-zero elements:", non_zero_elements)
    print("Zero elements    :", zero_elements)
    print(f"Zero fraction    : {zero_fraction:.2f} ({zero_fraction:.1%})")


def create_coo_matrix():
    data = np.array([5, 8, 3])
    rows = np.array([0, 2, 3])
    columns = np.array([2, 1, 4])

    return coo_array(
        (data, (rows, columns)),
        shape=(4, 5),
    )


def inspect_coo_matrix(coo_matrix):
    print_section("2. COO — COORDINATE FORMAT")

    print("Sparse representation:")
    print(coo_matrix)
    print()
    print("Shape  :", coo_matrix.shape)
    print("nnz    :", coo_matrix.nnz)
    print("Data   :", coo_matrix.data)
    print("Rows   :", coo_matrix.row)
    print("Columns:", coo_matrix.col)

    print("\nReconstructed dense matrix:")
    print(coo_matrix.toarray())


def inspect_csr_matrix(csr_matrix):
    print_section("3. CSR — COMPRESSED SPARSE ROW")

    print("Sparse representation:")
    print(csr_matrix)
    print()
    print("Shape  :", csr_matrix.shape)
    print("nnz    :", csr_matrix.nnz)
    print("Data   :", csr_matrix.data)
    print("Indices:", csr_matrix.indices)
    print("Indptr :", csr_matrix.indptr)

    print("\nReconstructed dense matrix:")
    print(csr_matrix.toarray())


def inspect_csr_row(csr_matrix, row_index):
    print_section(f"4. INSPECT CSR ROW {row_index}")

    start = csr_matrix.indptr[row_index]
    end = csr_matrix.indptr[row_index + 1]

    print("Start boundary :", start)
    print("End boundary   :", end)
    print("Stored values  :", csr_matrix.data[start:end])
    print("Column indices :", csr_matrix.indices[start:end])
    print("Dense row      :", csr_matrix[row_index].toarray())


def demonstrate_csr_matrix_vector_product(csr_matrix):
    print_section("5. CSR MATRIX-VECTOR PRODUCT")

    # vector will be of shape (5,) as we have 5 features
    vector = np.array([1, 2, 3, 4, 5])

    result = csr_matrix @ vector

    print("Vector    :", vector)

    print("\nCSR matrix:")
    print(csr_matrix.toarray())

    print("\nResult of CSR matrix @ vector:")
    print(result)


def inspect_csc_matrix(csc_matrix):
    print_section("6. CSC — COMPRESSED SPARSE COLUMN")

    print("Sparse representation:")
    print(csc_matrix)
    print()
    print("Shape  :", csc_matrix.shape)
    print("nnz    :", csc_matrix.nnz)
    print("Data   :", csc_matrix.data)
    print("Indices:", csc_matrix.indices)
    print("Indptr :", csc_matrix.indptr)

    print("\nReconstructed dense matrix:")
    print(csc_matrix.toarray())


def inspect_csc_column(csc_matrix, column_index):
    print_section(f"7. INSPECT CSC COLUMN {column_index}")

    start = csc_matrix.indptr[column_index]
    end = csc_matrix.indptr[column_index + 1]

    print("Start boundary:", start)
    print("End boundary  :", end)
    print("Stored values :", csc_matrix.data[start:end])
    print("Row indices   :", csc_matrix.indices[start:end])

    dense_column = csc_matrix[:, column_index].toarray()
    print("Dense Column:")
    print(dense_column)


def compare_memory_usage(dense_matrix, csr_matrix):
    print_section("8. DENSE VS CSR MEMORY")

    dense_bytes = dense_matrix.nbytes
    csr_data_bytes = csr_matrix.data.nbytes
    csr_indices_bytes = csr_matrix.indices.nbytes
    csr_indptr_bytes = csr_matrix.indptr.nbytes

    print("Dense array storage:")
    print("  Total bytes :", dense_bytes)

    csr_total_bytes = csr_data_bytes + csr_indices_bytes + csr_indptr_bytes

    print("\nCSR array storage:")
    print("  Data bytes   :", csr_data_bytes)
    print("  Indices bytes:", csr_indices_bytes)
    print("  Indptr bytes :", csr_indptr_bytes)
    print("  Total bytes  :", csr_total_bytes)


def main():
    dense_matrix = create_dense_matrix()
    inspect_dense_matrix(dense_matrix)

    coo_matrix = create_coo_matrix()
    inspect_coo_matrix(coo_matrix)

    csr_matrix = coo_matrix.tocsr()
    inspect_csr_matrix(csr_matrix)
    inspect_csr_row(csr_matrix, row_index=2)

    demonstrate_csr_matrix_vector_product(csr_matrix)

    csc_matrix = coo_matrix.tocsc()
    inspect_csc_matrix(csc_matrix)

    inspect_csc_column(csc_matrix, column_index=1)

    compare_memory_usage(dense_matrix, csr_matrix)


if __name__ == "__main__":
    main()
