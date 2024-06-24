
import math

import cv2


year = [
    "January",
    "Feburary",
    "March",
    "April",
    "May",
    "em",
    "July",
    "August",
    "September",
    "Oct",
    "Nov",
    "Dec"
]






"""
for i in Year:
    print("One of the months of the year is ", i)

"""


def first_two_letter(x):
    for word in x:
        if len(word) == 2:
            return word
    return "no word found"


print(first_two_letter(year))