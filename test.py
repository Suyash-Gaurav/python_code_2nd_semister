import sys


def test(did_pass):
    """
    Print the result of a test.

    Parameters:
    did_pass (bool): Indicates if the test passed or failed.
    """
    # Get the caller's line number
    line_num = sys._getframe(1).f_lineno
    # Format the message based on the test result
    msg = f"Test at line {line_num} {'ok' if did_pass else 'failed'}."
    # Print the message
    print(msg)


