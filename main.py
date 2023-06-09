# -*- coding: utf-8 -*-
# import the other files
from type_input import find_types
from offense_calculator import offense_calculator
from defense_calculator import defense_calculator

# create a function to house all the other functions
def main():
    # Program's name:
    battle_assistant = "べろべろ"

    # Welcome the user and explain the program:
    print("Welcome to the Pokemon Showdown Battle Assistant!")
    print("\nThis program will help you determine the best Pokemon/move to use against your opponent.")
    print(f"\nI'm BeroBero ({battle_assistant}) or Bero for short; I'll be your battle assistant!")

    # Call function to determine the opponent's type(s):
    opponent_type1, opponent_type2 = find_types()

    # Call function to determine opponent's offensive multipliers for each type:
    offensive_analysis = offense_calculator(opponent_type1, opponent_type2)
    print(offensive_analysis)

    
    return


main()


