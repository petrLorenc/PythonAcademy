import random
# Prepare the text into a list of words
file = open('./Lekce_8/Pride_Prejudice.txt')
text = str()
text = file.read()
file.close()
text = text.split()
#create a list of doubles
doubles = [(word1.lower().strip(' “”;').replace('_',''), word2.lower().strip(' _“”;').replace('_','')) for word1,word2 in zip(text,text[1:])]
#simulate user input
user_word = 'wife'
user_length = 20
#set up the variable needed for the algorithm
current_double = ('',user_word) #selected double
current_list = [] #list of possible doubles which can be used
answer_list = [user_word.title(),] #list of the output.

for i in range(user_length):
    current_list = []
    for double in doubles:
        if double[0] == current_double[1]:
            current_list.append(double)
    if not current_double:
        current_double.append(doubles.random.choice(doubles))
    current_double = random.choice(current_list)
    if answer_list[-1][-1] == '.' or answer_list[-1][-1] == '?' or answer_list[-1][-1] == '!':
        answer_list.append(current_double[1].title())
    else:
        answer_list.append(current_double[1])

print(current_list)
print(doubles)
print(' '.join(answer_list))