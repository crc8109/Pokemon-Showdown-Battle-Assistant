def offense_calculator(opponent_type1, opponent_type2):
    """This function will calculate the offensive multiplier for opponent Pokemon's type(s)"""

    opponent_types = [opponent_type1, opponent_type2]

    # Dictionary for the offensive multipliers for each of the types below:
    offense_multiplier_dict = {
        "normal": {
            1: ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "dragon", "dark", "steel", "fairy", "none"],
            0: ["ghost"]
        },
        "fire": {
            2: ["grass", "ice", "bug", "steel"],
            1: ["normal", "electric", "fighting", "poison", "ground", "flying", "psychic", "ghost", "dark", "fairy", "none"],
            0.5: ["fire", "water", "rock", "dragon"]
        },
        "water": {
            2: ["fire", "ground", "rock"],
            1: ["normal", "electric", "ice", "fighting", "poison", "flying", "psychic", "bug", "ghost", "dark", "steel", "fairy", "none"],
            0.5: ["water", "grass", "dragon"]
        },
        "electric": {
            2: ["water", "flying"],
            1: ["normal", "fire", "ice", "fighting", "poison", "psychic", "bug", "rock", "dark", "steel", "fairy", "none"],
            0.5: ["electric", "grass", "dragon", "ground"],
            0: ["ground"]
        },
        "grass": {
            2: ["water", "ground", "rock"],
            1: ["normal", "electric", "ice", "fighting", "psychic", "ghost", "dark", "fairy", "none"],
            0.5: ["fire", "grass", "poison", "flying", "bug", "dragon", "steel"]
        },
        "ice": {
            2: ["grass", "ground", "flying", "dragon"],
            1: ["normal", "electric", "fighting", "poison", "psychic", "bug", "rock", "ghost", "dark", "fairy", "none"],
            0.5: ["fire", "water", "ice", "steel"]
        },
        "fighting": {
            2: ["normal", "ice", "rock", "dark", "steel"],
            1: ["fire", "water", "electric", "grass", "fighting", "ground", "dragon", "none"],
            0.5: ["poison", "flying", "psychic", "bug", "fairy"],
            0: ["ghost"]
        },
        "poison": {
            2: ["grass", "fairy"],
            1: ["normal", "fire", "water", "electric", "ice", "fighting", "flying", "psychic", "bug", "dragon", "none"],
            0.5: ["poison", "ground", "rock", "ghost"],
            0: ["steel"]
        },
        "ground": {
            2: ["fire", "electric", "poison", "rock", "steel"],
            1: ["normal", "water", "ice", "fighting", "ground", "psychic", "ghost", "dragon", "dark", "fairy", "none"],
            0.5: ["grass", "bug"],
            0: ["flying"]
        },
        "flying": {
            2: ["grass", "fighting", "bug"],
            1: ["normal", "fire", "water", "ice", "poison", "ground", "flying", "psychic", "ghost", "dragon", "dark", "fairy", "none"],
            0.5: ["electric", "rock", "steel"],
            0: ["ground"]
        },
        "psychic": {
            2: ["fighting", "poison"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "ground", "flying", "bug", "rock", "dragon", "fairy", "none"],
            0.5: ["psychic", "steel"],
            0: ["dark"]
        },
        "bug": {
            2: ["grass", "psychic", "dark"],
            1: ["normal", "water", "electric", "ice", "ground", "bug", "rock", "dragon", "none"],
            0.5: ["fire", "fighting", "poison", "flying", "ghost", "steel", "fairy"]
        },
        "rock": {
            2: ["fire", "ice", "flying", "bug"],
            1: ["normal", "water", "electric", "grass", "fighting", "psychic", "rock", "ghost", "dragon", "dark", "fairy", "none"],
            0.5: ["fighting", "ground", "steel"]
        },
        "ghost": {
            2: ["psychic", "ghost"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "bug", "rock", "dragon", "steel", "fairy", "none"],
            0.5: ["dark"],
            0: ["normal"]
        },
        "dragon": {
            2: ["dragon"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "dark", "none"],
            0.5: ["steel"],
            0: ["fairy"]
        },
        "dark": {
            2: ["psychic", "ghost"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "poison", "ground", "flying", "bug", "rock", "dragon", "steel", "none"],
            0.5: ["fighting", "dark", "fairy"]
        },
        "steel": {
            2: ["ice", "rock", "fairy"],
            1: ["normal", "grass", "fighting", "poison", "ground", "flying", "psychic", "bug", "ghost", "dragon", "dark", "none"],
            0.5: ["fire", "water", "electric", "steel"]
        },
        "fairy": {
            2: ["fighting", "dragon", "dark"],
            1: ["normal", "water", "electric", "grass", "ice", "ground", "flying", "psychic", "bug", "rock", "ghost", "fairy", "none"],
            0.5: ["fire", "poison", "steel"]
        },
        "none": {
            1: ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "dragon", "dark", "steel", "fairy"]
        }
    }

    # This is the result of each type's offensive analysis (i.e its multiplier against each type)
    # It's a dictionary who's keys are multipiers (e.g. 2, 0.5, 0) 
    # and who's values are lists of types (e.g. ["grass", "ice", "bug", "steel"]
    battle_analysis = {}


    


    # This is the logic that will be used to fill out the temporary data structure for each type in opponent_types:
    for type in opponent_types:

        print(f"\nPrinting current type: {type}")

        # create a variable called "multiplier" 
        # it is just the current key in battle_analysis:
        for type in range(0, len(offense_multiplier_dict))
        # print current multiplier:
        print(f"Printing current multiplier: {multiplier}")
        

        
        # Look up the type in the dictionary
        # variable called "multiplier" will equal each key in the dictionary













        

       
        print(battle_analysis)

        return
