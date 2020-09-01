text = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.'''


target = input("What word should I look for?")

words = text.split()
found = False
position = 0

for word in words:
    word = word.strip(';,._/:')
    if word == target:
        print('POSITION: ' + str(position))
        found = True
    position += 1


if not found:
    print('NO SUCH WORD')