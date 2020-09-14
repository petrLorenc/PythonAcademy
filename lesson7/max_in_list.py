# ask user for sequence of integers, use 'q' to quit from asking user for next number
def ask_user(propmt: str) -> list:
    pass


# get maximum, minimum and average of the integers in a list without a build in functions - define your own functions
def perform_on_list(fn, list) -> int:
    pass


def max(list):
    pass


def min(list):
    pass


def avg(list):
    pass


assert perform_on_list(max, [1, 2, 3, 4, 5, 6]) == 6
assert perform_on_list(max, [1, 2, 3, 4, 5, 100]) == 100
assert perform_on_list(min, [1, 2, 3, 4, 5, 100]) == 1
assert perform_on_list(avg, [1, 2, 3]) == 2
assert perform_on_list(avg, [100, 0]) == 50
