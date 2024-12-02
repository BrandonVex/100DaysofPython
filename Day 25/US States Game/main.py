import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title("US States Game")

# Load the image of the US map
image = "Day 25/US States Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load the data of US states
data = pandas.read_csv("Day 25/US States Game/50_states.csv")

# Track correct answers
guessed_states = []

# Main game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name? (Type 'Exit' to quit)"
    )
    
    if answer_state is None or answer_state.lower() == "exit":
        # Identify missed states
        missed_states = [state for state in data.state if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states, columns=["state"])
        new_data.to_csv("Day 25/US States Game/states_to_learn.csv", index=False)
        print("Missed states saved to 'states_to_learn.csv'.")
        break

    
    answer_state = answer_state.title()
    # Check if the answer is correct and not already guessed
    if answer_state in data.state.values and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        
        # Get the state's coordinates
        state_data = data[data.state == answer_state]
        x_data = int(state_data.x.iloc[0])  
        y_data = int(state_data.y.iloc[0])  
        
        # Create a turtle to write the state name
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(x_data, y_data)
        tim.write(answer_state)

screen.exitonclick()  

# --__ -- __ -- __ -- notes -- __ -- __ -- __ -- 
# 1. convert the guess to title case
# 2. check if the guess is among the 50 states
# 3. record the correct guess on the map
# 4. use a loop to allow the user to keep guessing
# 5. record the correct guesses in a list
# 6. keep track of the score

