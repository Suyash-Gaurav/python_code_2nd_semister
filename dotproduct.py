def dot_product(u, v):
    """
    Calculate the dot product of two vectors u and v.

    Args:
    u (list of int/float): The first vector.
    v (list of int/float): The second vector.

    Returns:
    int/float: The dot product of the two vectors.
    """
    # Use a generator expression to calculate the product of corresponding elements
    # in u and v, and then sum these products to get the dot product.
    return sum(u_i * v_i for u_i, v_i in zip(u, v))


# Test cases to verify the function works as expected
print(dot_product([1, 1], [1, 1]))  # Expected output: 2
print(dot_product([1, 2], [1, 4]))  # Expected output: 9
print(dot_product([1, 2, 1], [1, 4, 3]))  # Expected output: 12


def cross_product(u, v):
    """
    Calculate the cross product of two 3-dimensional vectors u and v.

    Args:
    u (list of int/float): The first vector (must have 3 elements).
    v (list of int/float): The second vector (must have 3 elements).

    Returns:
    list of int/float: The cross product of the two vectors as a new 3-dimensional vector.
    """
    # Calculate each component of the cross product using the formula
    # [u2*v3 - u3*v2, u3*v1 - u1*v3, u1*v2 - u2*v1]
    return [
        u[1] * v[2] - u[2] * v[1],  # First component
        u[2] * v[0] - u[0] * v[2],  # Second component
        u[0] * v[1] - u[1] * v[0]  # Third component
    ]


# Test case to verify the function works as expected
print(cross_product([1, 2, 3], [4, 5, 6]))  # Expected output: [-3, 6, -3]
