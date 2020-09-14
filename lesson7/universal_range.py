# create function universal_range, where we don't need to define step (it would be decide according to start and stop to have about 10 steps)
def universal_range(start, end):
    pass


assert list(universal_range(0, 100)) == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
assert list(universal_range(0, 1000)) == [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
assert list(universal_range(0, 500)) == [0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
