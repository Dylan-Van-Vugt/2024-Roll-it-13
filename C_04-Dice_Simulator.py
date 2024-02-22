import random


# Generates a integer between 1 and 6 to simulate the roll of a die

def roll_die():
    result = random.randint(1, 6)
    return result


# Main routine starts here

for item in range(1, 10):
    user_score = 0
    double_score= "no"

    # Roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # Check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points (so far)
    user_points = roll_1 + roll_2

    # Show the user the result
    print(f"Die 1: {roll_1} \t Die 2: {roll_2} \t Points: {user_points}")
    print(f"Double Score Opportunity: {double_score}")