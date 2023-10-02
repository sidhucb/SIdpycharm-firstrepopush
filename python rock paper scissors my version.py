import random
sdg = ["rock", "scissor", "paper"]
uscore = 0
cscore = 0
while True:
    us = input("""Please type 'Rock'/'Scissor'/'Paper' or Q to quit : """).lower()
    if us == 'q':
        break
    if us not in sdg:
        continue
    r = random.randint(0, 2)
    comch = sdg[r]
    if comch == sdg[0] and us == sdg[1]:
        print('You lost')
        cscore += 1
        print(f'Computer : {comch}   You : {us} ')
    elif comch == sdg[0] and us == sdg[2]:
        print('You won')
        uscore += 1
        print(f'Computer : {comch}   You : {us} ')
    elif comch == sdg[1] and us == sdg[0]:
        print('You won')
        uscore += 1
        print(f'Computer : {comch}   You : {us} ')
    elif comch == sdg[1] and us == sdg[2]:
        print('You lost')
        cscore+=1
        print(f'Computer : {comch}   You : {us} ')
    elif comch == sdg[2] and us == sdg[0]:
        print('You lost')
        cscore+=1
        print(f'Computer : {comch}   You : {us} ')
    elif comch == sdg[2] and us == sdg[1]:
        print('You won')
        uscore+=1
        print(f'Computer : {comch}   You : {us} ')
    elif comch==us:
        print(f'Computer : {comch}   You : {us} ')
        print('Play once more')
        continue
    if uscore+cscore==5:
        print(f'Your score : {uscore}   Computer score : {cscore}')
        if uscore==cscore:
            print("It's a draw")
        elif uscore>cscore:
            print('You won the entire game, Congrats !! ')
        elif uscore<cscore:
            print("You lost the whole game, better luck next time !!")
        break
print('Game ended')
