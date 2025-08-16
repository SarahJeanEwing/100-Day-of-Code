import turtle
import pandas

score = 0
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")

#screen.update()
guessed_correctly = []
while len(guessed_correctly) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_correctly)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    if (answer_state in states_data.state.tolist()) and (answer_state not in guessed_correctly):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_data[states_data.state == answer_state]
        t.setpos(int(state_data.iloc[0].x), int(state_data.iloc[0].y))
        t.write(answer_state)
        guessed_correctly.append(answer_state)


states_to_learn = list(set(states_data.state.tolist()) - set(guessed_correctly))
print(states_to_learn)
df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")

