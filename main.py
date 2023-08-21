import turtle

import pandas

# Create a screen object
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

# answer_state= screen.textinput(title="Guess the State", prompt="What's another state's name?")
# print(answer_state)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
game_is_on = True
total_states = len(all_states)
while game_is_on:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer_state in guessed_states:
        print("You already guessed that state.")
    elif answer_state not in all_states:
        print("That's not a state.")
    elif answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        if len(guessed_states) == total_states:
            game_is_on = False
        # t.write(state_data.state.item())
        # t.write(state_data.x.item())
        # t.write(state_data.y.item())
        # t.write(state_data.state.item())
        # t.write(state_data.x.item())
        # t.write(state_data.y.item())
        # t.write(state_data.state.item())
        # t.write(state_data.x.item())
        # t.write(state_data.y.item())
        # t.write(state_data.state.item())






screen.exitonclick()
