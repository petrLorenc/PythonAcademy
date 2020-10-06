# filter out all integers to one array and rest to another
def divide(*items):
    result_int = []
    result_other = []
    for item in items:
        try:
            val = int(item)
        except (ValueError, TypeError):
            result_other.append(item)
        else:
            result_int.append(val)
    return result_other, result_int


print(divide('Hello', '23', '12', 'Bob', 'new', []))
print(divide('Hello', '23', '12', 'Bob', 'new', '4312', '5'))

