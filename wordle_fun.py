import os
from random_word import RandomWords
r = RandomWords()
a= r.get_random_word(minLength = 5, maxLength = 5).lower()

turn = 5
while(turn>0):
    b = input("Input: ")
    # os.system("cls")
    if a == b:
        print("Congrats!! You win in life!! This is all you had left!!\n")
        print('\u001b[32m'+b+'\u001b[37m')
        break
    else:
        result = []

        for k,v in enumerate(b):
            if v in a:
                indices = [i for i, x in enumerate(a) if x == v]
                # print(v," ",k," ", indices)
                if k in indices:
                    result.append('\u001b[32m'+v+'\u001b[37m')
                else:
                    result.append('\u001b[33m'+v+'\u001b[37m')
            else:
                result.append('\u001b[37m'+v+'\u001b[37m')
        print(''.join(result))
        turn -= 1
if(turn == 0):
    print('\u001b[37m'+"Bruh: "+a+'\u001b[37m')