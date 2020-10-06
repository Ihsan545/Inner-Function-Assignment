"""
Program: u.py
Author: Ihsanullah Anwary
Last date modified: 10/04/2020
Function Default Values Assignment
"""


def score_input(test_name, test_score=0, invaild_message="Invalid test score, try again!"):  # declaring function.
    try:  # try exception.
        if 0 <= int(test_score) <= 100:  # validates test score.
            print(test_name)
            return invaild_message
    except ValueError:
        print("That's not a number")
    else:
        print(invaild_message)  # print out


if __name__ == '__main__':
    score_input("Unit_4", 6, "Try again")  # calling the functio