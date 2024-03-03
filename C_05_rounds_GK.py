import random


# Generates an integer between 1 and 6 to simulate the roll of a die

def roll_die():
    result = random.randint(1, 6)
    return result


# Rolls two dice and returns total and whether we had a double roll

def two_rolls():
    double_score = "no"

    # Roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # Check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points (so far)
    user_points = roll_1 + roll_2

    # Show the user the result
    print(f"Die 1: {roll_1} \t Die 2: {roll_2}")

    return user_points, double_score


# Main routine starts here

# initialise 'pass' variables
user_pass = "no"
computer_pass = "no"

print("Press <enter> to begin this round: ")
input()

# Get initial dice rolls for user
user_first = two_rolls()
user_points = user_first[0]
double_points = user_first[1]

# Tell the user if they are eligible for double points
if double_points == "no":
    double_feedback = " "
else:
    double_feedback = "If you win this round, you gain double points!"

# Out put initial move results
print(f"You rolled a total of {user_points}.  {double_feedback}")
print()

# Get initial dice rolls for computer
computer_first = two_rolls()
computer_points = computer_first[0]

print(f"The computer rolled a total of {computer_points}.")

# Score update....
print(f"\nℹℹℹ You have a score of {user_points} vs {computer_points} ℹℹℹℹ")

# Loop (while both user / computer have <= 13 points)...
while computer_points < 13 and user_points < 13:

    # Ask user if they want to roll again, update
    # points / status
    print()

    if user_pass == "no":
        roll_again = input("Do you want to roll the dice (Type 'no' to pass): ")

    else:
        roll_again = "no"

    if roll_again == "yes":
        user_move = roll_die()
        user_points += user_move

        if user_points > 13:
            print(f"Oops! You rolled a {user_move} so your total is {user_points}.  "
                  f"Which is over 13 points.")

            # Reset user points to zero so that we update their score
            user_points = 0

            break

        else:
            print(f"You rolled a {user_move} and now have a total score of {user_points}")

    # if roll_again is not "yes"...
    else:
        # If user passes, we don't want to let them roll again!
        user_pass = "yes"

        # if computer has 10 points or more (and is winning), it should pass!
        if computer_points >= 10 and computer_points >= user_points:
            computer_pass = "yes"

        # Don't let the computer roll again if the pass condition
        # has been met in a previous iteration through the loop.
        elif computer_pass == "yes":
            pass

        else:
            computer_pass = "no"

    if computer_pass != "no":

        # Roll die for computer and update computer points
        computer_move = roll_die()
        computer_points += computer_move

        # check computer has not gone over...
        if computer_points > 13:
            print(f"💥💥💥The computer rolled a {computer_move}, taking their points"
                  f" to {computer_points}.  This is over 13 points so the computer loses!💥💥💥")
            computer_points = 0
            break

        else:
            print(f"The computer rolled a {computer_move}.  The computer"
                  f" now has {computer_points}.")

    print()

    # Tell user if they are winning, losing or if it's a tie.
    if user_points > computer_points:
        result = "🙂🙂🙂 You are ahead. 🙂🙂🙂"
    elif user_points < computer_points:
        result = "😯😯😯 The computer is ahead! 😯😯😯"
    else:
        result = "👀It's currently a tie.👀"

    print(f"{result} \tUser: {user_points} \t | \t Computer: {computer_points}")

    # if both the user and the computer have passed,
    # we need to exit the loop.
    if computer_pass == "yes" and user_pass == "yes":
        break

# Outside loop - double user points if they won and are eligilble

# Show rounds result
if user_points < computer_points:
    print("Sorry - you lost this round and no points "
          "have been added to your total score.  The computer's score has "
          f"increased by {computer_points} points.")

# Currently does not include double points!
else:
    print(f"Yay!  You won the round and {user_points} have "
          f"been added to your score")
