word='narges'
guesses=[]
allowed_errores= 7
done=False  
while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end='')
           
        else:
            print("_", end='')
    print('')

    guess=input(f'allowed error left {allowed_errores} next guess:')
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errores -= 1

        if allowed_errores == 0 :
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses :
            done=False

if done:
    print (f'you fonde in {word}')
else:
    print('game over')                   



