from test import test


def my_sum(sum):
    """sum of all numbers in the list sum, and return the total """
    running_total = 0
    for i in sum:
        running_total = running_total + i
        return running_total


def test_suite():
    """
    run the suite of test for code in this

    """

    test(my_sum([1, 2, 3, 4]) == 10)
    test(my_sum([1.25, 2.5, 1.75]) == 5.5)　
    test(my_sum([1, -2, 3]) == 2)
    test(my_sum([]) == 0)
    test(my_sum(range(11)) == 55)  # 11 is not included in the list.


test_suite()

