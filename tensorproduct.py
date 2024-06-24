def tensor_product(A, B):
    """
    Computing the tensor product (Kronecker product) of two tensors A and B.

    Args:
        A (list): A tensor represented as a nested list.
        B (list): Another tensor represented as a nested list.

    Returns:
        list: The tensor product of A and B as a nested list.
    """
    # Get the number of rows and columns of tensor A
    m, n = len(A), len(A[0])
    # Get the number of rows and columns of tensor B
    p, q = len(B), len(B[0])

    # Initialize the result tensor with zeros
    result = [[0] * (n * q) for _ in range(m * p)]

    # Iterate over rows of A
    for i in range(m):
        # Iterate over rows of B
        for k in range(p):
            # Calculate the row offset in the result tensor
            row_offset = i * p + k
            # Iterate over columns of A
            for j in range(n):
                # Cache the value of A[i][j]
                a_ij = A[i][j]
                # Iterate over columns of B
                for l in range(q):
                    # Calculate the tensor product and assign to the result tensor
                    result[row_offset][j * q + l] = a_ij * B[k][l]

    return result


# Example usage
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = tensor_product(A, B)
print(C)
