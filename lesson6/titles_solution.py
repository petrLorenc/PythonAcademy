def all_title(words):
    for word in words:
        if not word.istitle():
            return False
    return True


# return True if there are all word with first letter upper case, False othervise
assert True == all_title(['Bob', 'Frank', 'Mike', 'John'])
assert False == all_title(['Bob', 'Frank', 'Mike', 'john'])
