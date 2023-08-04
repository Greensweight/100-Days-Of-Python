import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
tee = turtle.Turtle()
tee.penup()
tee.hideturtle()
game_is_on = True

df = pd.read_csv("50_states.csv")

correct_guesses = []

## my implementation, it works!!!

# while game_is_on:
#     answer_state = screen.textinput(title=f"{len(correct_guesses)} / 50 States Correct", prompt="What's another state's name?")
#     answer = str(answer_state.title())
#     print(answer)
#     filtered_row = df.loc[df['state'] == answer]
#     if not filtered_row.empty:
#         correct_guesses.append(answer)
#         x = int(filtered_row['x'].values[0])
#         y = int(filtered_row['y'].values[0])
#         tee.goto(x, y)
#         tee.write((answer), align="center", font=("Courier", 8, "normal"))
#     elif len(correct_guesses) == 50:
#         game_is_on = False


#Udemy Implementation
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 States Correct", 
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_df = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

for correct_state in all_states:
    state_data = data[data.state == correct_state]
