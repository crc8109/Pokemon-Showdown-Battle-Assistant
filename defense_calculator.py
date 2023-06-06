def defense_calculator(opponent_type1, opponent_type2):
    """This function will calculate the offensive multiplier for opponent Pokemon's type(s)"""
    # Dictionary for the defensive multipliers for each of the types:
    defense_multiplier_dict = {
        "normal": {
            2: ["fighting"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "poison", "ground", "flying", "psychic", "bug", "rock", "dragon", "dark", "steel", "fairy"],
            0: ["ghost"]
        },
        "fire": {
            2: ["water", "ground", "rock"],
            1: ["normal", "electric", "fighting", "poison", "flying", "psychic", "ghost", "dragon", "dark"],
            0.5: ["fire", "grass", "ice", "bug", "steel", "fairy"]
        },
        "water": {
            2: ["electric", "grass"],
            1: ["normal", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "fairy"],
            0.5: ["fire", "water", "ice", "steel"]
        },
        "electric": {
            2: ["ground"],
            1: ["normal", "fire", "water", "ice", "fighting", "poison", "psychic", "bug", "rock", "ghost", "dragon", "dark", "fairy"],
            0.5: ["electric", "flying", "steel"]
        },
        "grass": {
            2: ["fire", "ice", "poison", "flying", "bug"],
            1: ["normal", "fighting", "psychic", "rock", "ghost", "dragon", "dark", "steel", "fairy"],
            0.5: ["water", "electric", "grass", "ground"]
        },
    }
