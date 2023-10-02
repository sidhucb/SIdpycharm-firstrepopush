# Equation of the line is y=2x+4
while True:
    a = int(input("Please type the x co-ordinate : "))
    b = int(input("please type the y co-ordinate : "))


    def omseevu(x, y):
        right = 0
        if ((2 * x) - y + 4) == 0:
            print(f"""The point ({x},{y}) is on the line""")
            right += 1
        else:
            print(f'The point ({x},{y}) is not on the line y=2x+4 ')


    omseevu(a, b)
    if ((2 * a) - b + 4) == 0:
        break
    else:
        continue
print('Alright you gave a point on the line')
