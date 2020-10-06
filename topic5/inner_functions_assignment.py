"""
Program: inner_functions_assignment.py
Author: Ihsanullah Anwary
Last date modified: 10/04/2020
This is an example of program that accepts a list of measurements for a rectangle and returns a string
 with perimeter and area.
"""


def measurements(rectangle): # outer function.
    def area(a): # inner function
        total_area = ('Area  = ' + str(rectangle[0] * rectangle[1]))
        return total_area  # return statement.



if __name__ == '__main__':
    measurements([4, 3.4]) # calling outer function.