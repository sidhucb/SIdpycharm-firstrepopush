print('Oh hello there, welcome to my computer quizz!! ')
playing=input('Before we begin, are you serious you sure wanna participate? ')
if playing.upper() !='YES':
    print("""Good choice boy, you are truly a coward""")
    quit()
print('Well done warrior, you can begin playing now ')
print('Here comes your first question')
score=0

wwq=input('What does www stands for? ')
if wwq.upper()=='WORLD WIDE WEB':
    print("""Correct""")
    score+=1
else:
    print('Incorrect')
wll=input('What does GPU stands for? ')
if wll.lower()=='graphics processing unit':
    print('Yes,you are correct ')
    score+=1
else:
    print('You are wrong')
bbl=input('What does RAM stands for? ')
if bbl.lower()=='random access memory':
    print('You are correct')
    score+=1
else:
    print("""That's incorrect""")
wwk=input('What does CPU stands for? ')
if wwk.lower()=='central processing unit':
    print('Correct answer!! ')
    score+=1
else:
    print("Wrong")
wwg=input('Who is the chief minister of kerala? ')
if wwg.lower()=='pinarayi vijayan':
    print("""Yup, that's correct""")
    score+=1
else:
    print('You are wrong')
print(f'You got {str(score)} questions correct ')
print(f'You got {int((score/5)*100)}%')
