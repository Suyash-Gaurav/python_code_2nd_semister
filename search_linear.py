# Import the test function from the test module
from test import test

# Define a list of friends
friends = ["Joe", "Zoe", "Brad"]


def search_linear(xs, target):
    """
    Perform a linear search to find the index of target in xs

    Parameters:
    xs (list): The list in which to search.
    target: The item to search for.

    Returns:
    int: The index of target in xs if found, otherwise -1.
    """
    # Iterate over the list with index and value
    for (i, v) in enumerate(xs):
        # If the current value matches the target, return the index
        if v == target:
            return i
    # If the target is not found, return -1
    return -1


"""
friends = ["Joe", "Zoe", "Brad"]
# Test case: Check if the function correctly finds "Zoe" in the friends list
test(search_linear(friends, "Zoe") == 1)
# Test case: Check if the function correctly finds "Joe" in the friends list
test(search_linear(friends, "Joe") == 0)
"""
