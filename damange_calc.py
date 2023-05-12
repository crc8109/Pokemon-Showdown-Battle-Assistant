def damanage_calc(opponent_type1, opponent_type2):
    
    # Dictionary to reference what each type is strong/weak against:
    type_chart = {"normal":
                            {"offensive": {"multiplier: ": [""]},
                            {"deals more damage against: ": [""]},
                            {"deals less damange against: ": ["fighting"], "immune": ["ghost"]},
                            {"Deals no damange against: ": ["ghost"]},

                            {"receives more damange from: ": ["fighting"]},
                            {"receives less damange from: ": [""]},
                            {"receives no damange from: ": ["ghost"]},

                  "fire":  
                            {"deals more damage against: ": ["grass", "ice", "bug", "steel"]},
                            {"deals less damange against: ": ["fire", "water", "rock", "dragon"]},
                            {"receives more damange from: ": ["water", "ground", "rock"]},
                            {"receives less damange from: ": ["fire", "grass", "ice", "bug", "steel", "fairy"]},
                            {"receives no damange from: ": [""]},

                  "water": 
                            {"deals more damage against: ": ["fire", "ground", "rock"]}, 
                            {"deals less damange against: ": ["water", "grass", "dragon"]},
                            {"receives more damange from: ": ["electric", "grass"]},
                            {"receives less damange from: ": ["fire", "water", "ice", "steel"]},
                            {"receives no damange from: ": [""]},

                "electric":
                            {"deals more damage against: ": ["water", "flying"]},
                            {"deals less damange against: ": ["electric", "grass", "dragon"]},
                            {"receives more damange from: ": ["ground"]},
                            {"receives less damange from: ": ["electric", "flying", "steel"]},
                            {"receives no damange from: ": [""]},

                "grass":
                            {"deals more damage against: ": ["water", "ground", "rock"]},
                            {"deals less damange against: ": ["fire", "grass", "poison", "flying", "bug", "dragon", "steel"]},
                            {"receives more damange from: ": ["fire", "ice", "poison", "flying", "bug"]},
                            {"receives less damange from: ": ["water", "electric", "grass", "ground"]},
                            {"receives no damange from: ": [""]},

                "ice":
                            {"deals more damage against: ": ["grass", "ground", "flying", "dragon"]},
                            {"deals less damange against: ": ["fire", "water", "ice", "steel"]},
                            {"receives more damange from: ": ["fire", "fighting", "rock", "steel"]},
                            {"receives less damange from: ": ["ice"]},
                            {"receives no damange from: ": [""]},

                "fighting":
                            {"deals more damage against: ": ["normal", "ice", "rock", "dark", "steel"]},
                            {"deals less damange against: ": ["poison", "flying", "psychic", "bug", "fairy"]},
                            {"deals no damange from: ": ["ghost"]},
                            {"receives more damange from: ": ["flying", "psychic", "fairy"]},
                            {"receives less damange from: ": ["bug", "rock", "dark"]},
                            

                            
                    
                             
                    "electric": {"deals more damage against: ": ["water", "flying"], "deals less damange against: ": ["electric", "grass", "dragon"], "immune": ["ground"]},
                    "grass": {"deals more damage against: ": ["water", "ground", "rock"], "deals less damange against: ": ["fire", "grass", "poison", "flying", "bug", "dragon", "steel"], "immune": []},
                    "ice": {"deals more damage against: ": ["grass", "ground", "flying", "dragon"], "deals less damange against: ": ["fire", "water", "ice", "steel"], "immune": []},
                    "fighting": {"deals more damage against: ": ["normal", "ice", "rock", "dark", "steel"], "deals less damange against: ": ["poison", "flying", "psychic", "bug", "fairy"], "immune": ["ghost"]},
                    "poison": {"deals more damage against: ": ["grass", "fairy"], "deals less damange against: ": ["poison", "ground", "rock", "ghost"], "immune": ["steel"]},
                    "ground": {"deals more damage against: ": ["fire", "electric", "poison", "rock", "steel"], "deals less damange against: ": ["grass", "bug"], "immune": ["flying"]},
                    "flying": {"deals more damage against: ": ["grass", "fighting", "bug"], "deals less damange against: ": ["electric", "rock", "steel"], "immune": []},
                    "psychic": {"deals more damage against: ": ["fighting", "poison"], "deals less damange against: ": ["psychic", "steel"], "immune": ["dark"]},
                    "bug": {"deals more damage against: ": ["grass", "psychic", "dark"], "deals less damange against: ": ["fire", "fighting", "poison", "flying", "ghost", "steel", "fairy"], "immune": []},
                    "rock": {"deals more damage against: ": ["fire", "ice", "flying", "bug"], "deals less damange against: ": ["fighting", "ground", "steel"], "immune": []},
                    "ghost": {"deals more damage against: ": ["psychic", "ghost"], "deals less damange against: ": ["dark"], "immune": ["normal"]},
                    "dragon": {"deals more damage against: ": ["dragon"], "deals less damange against: ": ["steel"], "immune": ["fairy"]},
                    "dark": {"deals more damage against: ": ["psychic", "ghost"], "deals less damange against: ": ["fighting", "dark", "fairy"], "immune": []},
                    "steel": {"deals more damage against: ": ["ice", "rock", "fairy"], "deals less damange against: ": ["fire", "water", "electric", "steel"], "immune": []},
                    "fairy": {"deals more damage against: ": ["fighting", "dragon", "dark"], "deals less damange against: ": ["fire", "poison", "steel"], "immune": []}
                    }
    
    # After the opponents' types are passed along to damage_calc(), the function will
    # return which types are strong/weak against the opponent's types 
    # as well as a multiplier value of each type match-up to indiciate how effective the type is against the opponent's types.
    # The output should look like this if the input was "flying" and "water":
    # "This Pokemon is strong against: 
    # (lists the individual types that are strong against the opponent's types, so long as they don't overlap/cancel out;
    # e.g. 
    # 
    # rass, fighting, bug, fire, ground, and rock; 
    # it's multiplier against these types is: 2.0""
    # "This Pokemon is VERY strong against: "none" (because there's no overlap in weakness between flying and water)"
    # "This Pokemon is weak against: electric, ice, and rock; it takes 2X damage from these types."



damage_calc(opponenttype1, opponenttype2)
