# Code Generator
"""
Code will generate secret string from input string using a secret number to shift
 the alphabet by a certain amount. This will allow us to make the secret code. 
 The SC will come out in all caps. No symbols allowed
 """

instr = input('Type what you need encrypted: ')
scn = 5
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.,!:'

mstr = instr.upper()

mstr = mstr.replace(' ', '')
# mstr = mstr.replace(',', '')
# print(mstr)

flag = 0

# Shifting the alphabet
calpha = alpha
for i in range(scn):
    calpha = calpha[1:] + calpha[0]
# print(calpha)
# print(alpha)

# add counter to list of counts to count how many times the I have to itterate through the alphabet
counter = []
# count = 0
loop = 0
looper = []

for letter in mstr:
    for aletter in alpha:
        loop += 1
        if letter == aletter:
            looper.append(loop)
            loop = 0
            # print(letter)
            # print(mstr)
            mstr = mstr[1:]
            break
        

# print(counter)
# print(loop)
# print(looper)

sc = []
for num in looper:
    # print(num)
    x = calpha[num]
    # print(x)
    sc.append(x)

scw = ''.join(sc)
print('\n', scw, '\n')






