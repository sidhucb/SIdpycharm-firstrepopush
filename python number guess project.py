import random
tor=input("Please type a number : ")
if tor.isdigit():
    tor=int(tor)
else:
    print('Please type a number next time')
    quit()
r=random.randint(0,tor)
guesses=0
while True:
    ug=input('Please guess a number : ')
    guesses+=1
    if ug.isdigit():
        ug=int(ug)
    else:
        print("Please type a number next time")
        continue
    if ug==r:
        print(f"Your guess : {ug}    Random number : {r}    Number of Guesses : {guesses}")
        print("You got it right")
        break
    elif ug>r:
        print("Your guess is above the number")
    else:
        print('Your guess is below the number')
print(f'You got it right in {guesses} guesses')
