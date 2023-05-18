#Decryptor
mstr = input('What do you need decrypted: ')
scn = 5
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.,!:'

flag = 0

calpha = alpha
for i in range(scn):
    calpha = calpha[1:] + calpha[0]

counter = []
loop = 0
looper = []

for letter in mstr:
    for aletter in calpha:
        loop += 1
        if letter == aletter:
            looper.append(loop)
            loop = 0
            # print(letter)
            # print(mstr)
            mstr = mstr[1:]
            break

# print(looper)

sc = []
for num in looper:
    # print(num)
    x = alpha[num-2]
    # print(x)
    sc.append(x)

scw = ''.join(sc)
print('\n', scw, '\n')