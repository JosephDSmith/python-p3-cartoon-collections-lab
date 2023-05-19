def roll_call_dwarves(dwarves):
    numbers = range(1, len(dwarves) + 1)
    for number in numbers:
        print(f'{number}. {dwarves[number-1]}')

def summon_captain_planet(planeteer_calls):
    list = []
    for call in planeteer_calls:
        list.append(f'{call[0].upper()}{call[1:]}!')
    return list

def long_planeteer_calls(words):
    tf_list = []
    for word in words:
        if len(word) > 4:
            tf_list.append("True")
        else:
            tf_list.append("False")
    if "True" in tf_list:
        return True
    else:
        return False

def find_the_cheese(foods):
    for food in foods:
        if food == "cheddar":
            return "cheddar"
        elif food == "gouda":
            return "gouda"
        elif food == "camembert":
            return "camembert"
        
    return None
