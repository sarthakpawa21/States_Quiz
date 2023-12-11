
from turtle import Turtle, Screen

import pandas

pen = Turtle()
pen.hideturtle()



def writestatename(name , x , y):
    pen.penup()
    pen.hideturtle()
    pen.goto(x,y)

    pen.write(name , align='center', font=('Arial', 10,'bold'))

image='map.gif'

screen = Screen()
screen.setup(1000, 1000, 10, 10)
screen.bgpic(image)
screen.title('States Game')
pen = Turtle()

with open('states.csv') as data_file:
    df = pandas.read_csv(data_file)

game_on = True
guessed_states_list = []
while game_on:
    name = screen.textinput(title= f'Guess State({len(guessed_states_list)}/28)', prompt='Enter the name of a state')
    name = name.title()

    states_list = list(df['state'])

    if name in states_list :
        index = states_list.index(name)
        x = df.iloc[index][1] - 380
        y = -df.iloc[index][2] +450
        writestatename(name,x,y)
        if name not in guessed_states_list:
            guessed_states_list.append(name)
    if len(guessed_states_list)== 28:
        game_on = False
        pen.goto(0,0)
        pen.write("CONGRATULATIONS !!!! \n You Win !", align='center', font=('Arial', 40, 'bold'))








screen.exitonclick()

