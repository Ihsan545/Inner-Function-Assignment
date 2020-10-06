"""
Program: set_age.py
Author: Ihsanullah Anwary
Last date modified: 10/04/2020
This program is example of calling a function to return the value.
"""


def multiply_string(string):  # declaring function and parameter string.
    message_string = "Nice!"  # string variable.
    for i in range(string):  # for loop
        print(message_string, end)  # print string.

    return string  # return statement.


if __name__ == '__main__':
    multiply_string(4)  # function call.
