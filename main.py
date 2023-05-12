# -*- coding: utf-8 -*-
# Determine the opponent's type(s) and return them to the main function
def find_types():

    # Program's name:
    battle_assistant = "べろべろ"

    # Welcome the user and explain the program:
    print("Welcome to the Pokemon Showdown Battle Assistant!")
    print("\nThis program will help you determine the best Pokemon/move to use against your opponent.")
    print(f"\nI'm BeroBero ({battle_assistant}) or Bero for short; I'll be your battle assistant!")

    # List of all acceptable types to be checked against the user's input:
    acceptable_types = ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground",
                        "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]
    
    # Ask for first type and ensure type is valid:
    while True:
        opponent_type1 = input("\nWhat is the opponent's first type? > ").lower()
        if opponent_type1 in acceptable_types:
            break
        else:
            print(f"\nHere is a list of all acceptable types: {acceptable_types}")
            print(f"\nYou entered: {opponent_type1}")
            print("\nPlease enter a valid type.")
  
    # Ask for second type and ensure type is valid (in acceptable_types AND not the same as opponent_type1)
    # If the second type is "none", then the opponent only has one type and the program will continue:
    while True:
        opponent_type2 = input("\nWhat is the opponent's second type? (Enter 'none' if the opponent only has one type) > ").lower()
        if opponent_type2 in acceptable_types and opponent_type2 != opponent_type1:
            break
        elif opponent_type2 == "none":
            break
        else:
            print(f"\nHere is a list of all acceptable types: {acceptable_types}")
            print(f"\nYou entered: {opponent_type2}")
            # Double check that the user didn't enter the same type as the first type:
            if opponent_type2 == opponent_type1:
                print("\nYou entered the same type as the first type.") 
            print("\nPlease enter a valid type or 'none'.")
    
    # Return the opponent's types so the next function can use them, depending on whether there are 1 or 2 opponent types:
    if opponent_type2 == "none":
        return opponent_type1
    else:
        return opponent_type1, opponent_type2
    
# find_types()
# Test that everything works by printing the opponent types below:
print(find_types())
